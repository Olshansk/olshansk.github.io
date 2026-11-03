#!/usr/bin/env bash
# Use real temporary repositories; replace only the GitHub API boundary.
set -euo pipefail
script="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/finish-branch.sh"
test_root=$(mktemp -d)
trap 'result=$?; if [[ $result != 0 && -f "$test_root/output" ]]; then cat "$test_root/output" >&2; git status --short >&2; fi; rm -rf "$test_root"' EXIT
mkdir -p "$test_root/bin" "$test_root/hooks"
export FAKE_GH_LOG="$test_root/gh.log"
export REAL_GIT
REAL_GIT=$(command -v git)
export OFFLINE_NETWORK_LOG="$test_root/network.log"
cat > "$test_root/bin/git" <<'GIT'
#!/usr/bin/env bash
set -euo pipefail
if [[ "${BLOCK_NETWORK:-0}" == 1 ]]; then
    case "$1" in
        fetch|pull|push|ls-remote|remote)
            printf 'git %s\n' "$*" >> "$OFFLINE_NETWORK_LOG"
            exit 99
            ;;
    esac
fi
exec "$REAL_GIT" "$@"
GIT
chmod +x "$test_root/bin/git"
export PATH="$test_root/bin:$PATH"
cat > "$test_root/bin/gh" <<'GH'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$*" >> "$FAKE_GH_LOG"
if [[ "${BLOCK_NETWORK:-0}" == 1 ]]; then
    printf 'gh %s\n' "$*" >> "$OFFLINE_NETWORK_LOG"
    exit 99
fi
case "$1 $2" in
    'pr view')
        [[ "${FAKE_GH_VIEW_FAIL:-0}" == 0 ]] || exit 1
        if [[ "$*" == *'--json state,mergeCommit'* ]]; then
            printf '%s\t%s\n' "${FAKE_GH_STATE:-MERGED}" "$(git rev-parse origin/main)"
        else
            printf '%s\t%s\t%s\t%s\t%s\n' "${FAKE_GH_BASE:-main}" \
                "${FAKE_GH_HEAD:-$(git rev-parse HEAD)}" "${FAKE_GH_CROSS:-false}" \
                "${FAKE_GH_OPEN:-OPEN}" "${FAKE_GH_DRAFT:-false}"
        fi
        ;;
    'pr merge')
        [[ "${FAKE_GH_MERGE_FAIL:-0}" == 0 ]] || exit 1
        [[ "${FAKE_GH_STATE:-MERGED}" == MERGED ]] || exit 0
        squash=$(printf 'feat: squash PR\n' | git commit-tree "HEAD^{tree}" -p origin/main)
        git push --quiet origin "$squash:refs/heads/main"
        ;;
    *) exit 2 ;;
esac
GH
chmod +x "$test_root/bin/gh"
cd "$test_root"
git init --quiet --bare --initial-branch=main remote.git
git clone --quiet remote.git repo 2>/dev/null
cd repo
git config user.name Test
git config user.email test@example.invalid
# Fixture-only hook directories do not alter the user's managed Git hooks.
git config core.hooksPath "$test_root/hooks"
git --git-dir=../remote.git config core.hooksPath "$test_root/hooks"
git commit --quiet --allow-empty -m base
git push --quiet origin main
base=$(git rev-parse HEAD)
git switch --quiet -c feature/finish
printf 'one\n' > feature.txt
git add feature.txt
git commit --quiet -m first
printf 'two\n' >> feature.txt
git commit --quiet -am second
head=$(git rev-parse HEAD)
git push --quiet origin HEAD:feature/finish

reject() {
    local label=$1 message=$2
    shift 2
    : > "$FAKE_GH_LOG"
    if "$@" bash "$script" > "$test_root/output" 2>&1; then
        printf 'FAIL: %s unexpectedly succeeded\n' "$label" >&2
        exit 1
    fi
    grep -Fq "$message" "$test_root/output" || { cat "$test_root/output"; exit 1; }
    if grep -q '^pr merge ' "$FAKE_GH_LOG"; then
        printf 'FAIL: %s attempted a merge\n' "$label" >&2
        exit 1
    fi
    printf 'PASS: %s rejected before merge\n' "$label"
}

git switch --quiet main
reject 'main branch' 'Check out a feature branch' env
git switch --quiet --detach
reject 'detached HEAD' 'Check out the branch' env
git switch --quiet feature/finish
printf 'unfinished\n' > work.txt
reject 'untracked work' 'Commit or stash local changes' env
git add work.txt
reject 'staged work' 'Commit or stash local changes' env
git reset --quiet
rm work.txt
reject 'missing PR or unavailable GitHub' 'Could not read the branch PR' env FAKE_GH_VIEW_FAIL=1
reject 'wrong base branch' 'it must target main' env FAKE_GH_BASE=release
reject 'unpublished or outdated commits' 'Local HEAD differs from the PR' env FAKE_GH_HEAD=deadbeef
reject 'fork PR' 'fork branch cleanup is not supported' env FAKE_GH_CROSS=true
reject 'draft PR' 'PR must be open and ready' env FAKE_GH_DRAFT=true
reject 'closed PR' 'PR must be open and ready' env FAKE_GH_OPEN=CLOSED
git switch --quiet main
git commit --quiet --allow-empty -m unpublished
git switch --quiet feature/finish
reject 'unpublished main' 'Local main has unpublished commits' env
git branch --force main "$base" >/dev/null

if env FAKE_GH_MERGE_FAIL=1 bash "$script" > "$test_root/output" 2>&1; then
    printf 'FAIL: GitHub merge rejection was ignored\n' >&2
    exit 1
fi
[[ "$(git branch --show-current)" == feature/finish ]]
[[ "$(git rev-parse origin/main)" == "$base" ]]
printf 'PASS: merge rejection preserves feature branch and main\n'

if env FAKE_GH_STATE=OPEN bash "$script" > "$test_root/output" 2>&1; then
    printf 'FAIL: queued PR triggered cleanup\n' >&2
    exit 1
fi
grep -Fq 'PR is not merged yet' "$test_root/output"
[[ "$(git branch --show-current)" == feature/finish ]]
[[ "$(git --git-dir=../remote.git rev-parse feature/finish)" == "$head" ]]
printf 'PASS: queued PR retains both feature refs and current checkout\n'

: > "$FAKE_GH_LOG"
bash "$script" > "$test_root/output" 2>&1
expected="pr merge feature/finish --repo $(git remote get-url origin) --squash --match-head-commit $head"
grep -Fxq "$expected" "$FAKE_GH_LOG"
[[ "$(git branch --show-current)" == main ]]
[[ "$(git rev-parse main)" == "$(git --git-dir=../remote.git rev-parse main)" ]]
[[ "$(git rev-list --count "$base..main")" == 1 ]]
[[ "$(cat feature.txt)" == $'one\ntwo' ]]
! git show-ref --verify --quiet refs/heads/feature/finish
[[ -z "$(git ls-remote --heads origin refs/heads/feature/finish)" ]]
[[ -z "$(git status --porcelain)" ]]
printf 'PASS: verified squash updates main, preserves content, and deletes both feature refs\n'

# Offline fixtures run the public Make target with Git/GitHub network calls denied.
project=$(dirname "$(dirname "$script")")
offline_setup() {
    local label=$1
    mkdir -p "$test_root/$label"
    cd "$test_root/$label"
    git init --quiet --initial-branch=main
    git config user.name Test
    git config user.email test@example.invalid
    git config core.hooksPath "$PWD/.git/hooks"
    mkdir scripts
    cp "$project/Makefile" Makefile
    cp "$script" scripts/finish-branch.sh
    printf 'base\n' > base.txt
    git add Makefile scripts base.txt
    git commit --quiet -m base
    base=$(git rev-parse HEAD)
    git switch --quiet -c feature/offline
    printf 'one\n' > feature.txt
    git add feature.txt
    git commit --quiet -m first
    printf 'two\n' >> feature.txt
    git commit --quiet -am 'feat: offline finished'
    head=$(git rev-parse HEAD)
    : > "$OFFLINE_NETWORK_LOG"
}

offline_reject() {
    local label=$1 message=$2
    shift 2
    if env BLOCK_NETWORK=1 make finish-branch OFFLINE=1 "$@" > "$test_root/output" 2>&1; then
        printf 'FAIL: %s unexpectedly succeeded\n' "$label" >&2
        exit 1
    fi
    grep -Fq "$message" "$test_root/output" || { cat "$test_root/output"; exit 1; }
    git show-ref --verify --quiet refs/heads/feature/offline
    [[ ! -s "$OFFLINE_NETWORK_LOG" ]]
    printf 'PASS: %s; source branch retained, no network calls\n' "$label"
}

offline_setup 'offline success'
git switch --quiet main
printf 'main-only\n' > main.txt
git add main.txt
git commit --quiet -m 'local main change'
main_head=$(git rev-parse HEAD)
git switch --quiet feature/offline
git init --quiet --bare --initial-branch=main "$test_root/offline-remote.git"
git --git-dir="$test_root/offline-remote.git" config core.hooksPath "$test_root/hooks"
git remote add origin "$test_root/offline-remote.git"
git push --quiet origin main feature/offline
subject='feat: literal $(shell touch SHOULD_NOT_EXIST) and `backticks`'
BLOCK_NETWORK=1 make finish-branch OFFLINE=1 MESSAGE="$subject" > "$test_root/output" 2>&1
[[ "$(git branch --show-current)" == main ]]
[[ "$(git log -1 --format=%s)" == "$subject" ]]
[[ ! -e SHOULD_NOT_EXIST ]]
[[ "$(git rev-list --count "$main_head..main")" == 1 ]]
[[ "$(git rev-parse main^)" == "$main_head" ]]
[[ "$(cat feature.txt)" == $'one\ntwo' && "$(cat main.txt)" == main-only ]]
! git show-ref --verify --quiet refs/heads/feature/offline
[[ "$(git --git-dir="$test_root/offline-remote.git" rev-parse main)" == "$main_head" ]]
[[ "$(git --git-dir="$test_root/offline-remote.git" rev-parse feature/offline)" == "$head" ]]
[[ -z "$(git status --porcelain)" && ! -s "$OFFLINE_NETWORK_LOG" ]]
printf 'PASS: offline Make target squashes two commits, preserves main changes, deletes local branch only, and treats MESSAGE literally\n'

offline_setup offline-no-remote
BLOCK_NETWORK=1 make finish-branch OFFLINE=1 > "$test_root/output" 2>&1
[[ "$(git branch --show-current)" == main ]]
[[ "$(git log -1 --format=%s)" == 'feat: offline finished' ]]
[[ ! -s "$OFFLINE_NETWORK_LOG" ]]
printf 'PASS: offline mode needs no remote and defaults to latest commit subject\n'

offline_setup offline-conflict
printf 'feature\n' > base.txt
git commit --quiet -am feature-conflict
head=$(git rev-parse HEAD)
git switch --quiet main
printf 'main\n' > base.txt
git commit --quiet -am main-conflict
main_head=$(git rev-parse HEAD)
git switch --quiet feature/offline
offline_reject 'offline conflict' 'Offline squash preflight failed'
[[ "$(git branch --show-current)" == feature/offline ]]
[[ "$(git rev-parse main)" == "$main_head" && "$(git rev-parse HEAD)" == "$head" ]]
[[ -z "$(git status --porcelain)" ]]

offline_setup offline-guards
printf 'unfinished\n' > dirty.txt
offline_reject 'offline uncommitted work' 'Commit or stash local changes'
rm dirty.txt
offline_reject 'invalid offline mode' 'OFFLINE must be 0' OFFLINE=invalid
git branch --delete main >/dev/null
offline_reject 'missing local main' 'Create a local main branch'
git branch main "$head"
offline_reject 'already merged offline branch' 'already merged into local main'

offline_setup offline-commit-failure
cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
exit 1
HOOK
chmod +x .git/hooks/pre-commit
offline_reject 'offline commit hook rejection' 'Commit failed on main'
[[ "$(git branch --show-current)" == main ]]
[[ "$(git rev-parse main)" == "$base" ]]
! git diff --cached --quiet
