#!/usr/bin/env bash
# Finish through a GitHub PR, or squash locally in explicit offline mode.
set -euo pipefail

fail() {
    printf 'finish-branch: %s\n' "$*" >&2
    exit 1
}

offline=${FINISH_OFFLINE-0}
[[ "$offline" == 0 || "$offline" == 1 ]] || fail 'OFFLINE must be 0 (GitHub PR) or 1 (local squash).'
[[ "$offline" == 1 || -z "${FINISH_MESSAGE:-}" ]] || fail 'MESSAGE applies only to OFFLINE=1.'
branch=$(git symbolic-ref --quiet --short HEAD) || fail 'Check out the branch you want to finish.'
[[ "$branch" != main ]] || fail 'Check out a feature branch, not main.'
cd "$(git rev-parse --show-toplevel)"
[[ -z "$(git status --porcelain)" ]] || fail 'Commit or stash local changes, including untracked files, first.'
for state in MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD rebase-merge rebase-apply; do
    [[ ! -e "$(git rev-parse --git-path "$state")" ]] || fail 'Finish the current Git operation first.'
done
head=$(git rev-parse HEAD)
if [[ "$offline" == 1 ]]; then
    git show-ref --verify --quiet refs/heads/main || fail 'Create a local main branch before using offline mode.'
    git merge-base --is-ancestor "$head" main && fail 'The feature branch is already merged into local main.'
    message=${FINISH_MESSAGE:-$(git log -1 --format=%s)}
    [[ "$message" == *[![:space:]]* ]] || fail 'MESSAGE must contain a commit subject.'
    main_head=$(git rev-parse main)
    printf 'LIVE RUN | OFFLINE | squash %s into local main; no fetch, push, or PR changes\n' "$branch"
    # Preflight the merge without changing the index, checkout, or branch refs.
    if ! preview=$(git merge-tree --write-tree "$main_head" "$head"); then
        printf '%s\n' "$preview" >&2
        fail 'Offline squash preflight failed. Resolve conflicts on the feature branch, or check Git supports merge-tree --write-tree.'
    fi
    git switch main
    [[ "$(git rev-parse HEAD)" == "$main_head" ]] || fail 'Local main changed during preflight. Feature branch retained.'
    git merge --squash "$head" || fail "Squash failed on main. '$branch' is retained; resolve and commit, or run git reset --merge HEAD before switching back."
    if git diff --cached --quiet; then
        git switch "$branch"
        fail 'No changes to squash. Feature branch retained.'
    fi
    git commit -m "$message" || fail "Commit failed on main. Staged squash and '$branch' retained; fix and commit, or run git reset --merge HEAD before switching back."
    [[ -z "$(git status --porcelain)" ]] || fail 'Worktree changed during commit. Feature branch retained for inspection.'
    [[ "$(git rev-parse "refs/heads/$branch")" == "$head" ]] || fail 'Feature branch changed during squash. It is retained for inspection.'
    git branch -D "$branch"
    printf 'LIVE RUN COMPLETE | OFFLINE | squash %s on local main; deleted local %s; remote refs and PR unchanged\n' "$(git rev-parse HEAD)" "$branch"
    exit 0
fi

command -v gh >/dev/null || fail 'Install and authenticate GitHub CLI (gh) first.'
repo=$(git remote get-url origin)
pr=$(gh pr view "$branch" --repo "$repo" --json baseRefName,headRefOid,isCrossRepository,state,isDraft \
    --jq '[.baseRefName, .headRefOid, .isCrossRepository, .state, .isDraft] | @tsv') || \
    fail 'Could not read the branch PR. Authenticate gh, push the branch, and open a PR targeting main.'
IFS=$'\t' read -r base pr_head cross_repository state draft <<< "$pr"
[[ "$base" == main ]] || fail "The PR targets '$base'; it must target main."
[[ "$cross_repository" == false ]] || fail 'Use a branch in this repository; fork branch cleanup is not supported.'
[[ "$head" == "$pr_head" ]] || fail 'Local HEAD differs from the PR. Sync and push the intended commits before finishing.'
[[ "$state" == OPEN && "$draft" == false ]] || fail 'The PR must be open and ready for review, not a draft.'

printf 'LIVE RUN | squash PR for %s into origin/main, then delete the branch\n' "$branch"
git fetch origin --prune
git merge-base --is-ancestor main origin/main || fail 'Local main has unpublished commits. Reconcile main before merging the PR.'
# Pin the reviewed head and honor GitHub checks, reviews, and merge queues.
# A queued or deferred merge must never trigger branch cleanup.
gh pr merge "$branch" --repo "$repo" --squash --match-head-commit "$head"
merged=$(gh pr view "$branch" --repo "$repo" --json state,mergeCommit \
    --jq '[.state, (.mergeCommit.oid // "")] | @tsv') || \
    fail 'Could not verify the merge. Feature branch retained; inspect the PR before cleanup.'
IFS=$'\t' read -r state squash <<< "$merged"
[[ "$state" == MERGED && -n "$squash" ]] || fail 'PR is not merged yet (possibly queued). Feature branch retained; wait for the merge before cleanup.'

git fetch origin --prune
git merge-base --is-ancestor "$squash" origin/main || fail 'Squash commit is not on origin/main. Feature branch retained.'
git switch main
git merge --ff-only origin/main
remote_head=$(git ls-remote --heads origin "refs/heads/$branch")
if [[ -n "$remote_head" ]]; then
    [[ "$remote_head" == "$head"$'\t'"refs/heads/$branch" ]] || fail 'Remote feature branch changed after merge. It is retained for inspection.'
    git push --force-with-lease="refs/heads/$branch:$head" origin ":refs/heads/$branch" || \
        fail 'PR merged and main updated, but remote branch deletion failed. Local feature branch retained.'
fi
[[ "$(git rev-parse "refs/heads/$branch")" == "$head" ]] || fail 'Local feature branch changed after merge. It is retained for inspection.'
# Squashing replaces commit IDs, so Git cannot infer that the source is merged.
git branch -D "$branch"
printf 'LIVE RUN COMPLETE | PR squash %s on main; deleted %s\n' "$squash" "$branch"
