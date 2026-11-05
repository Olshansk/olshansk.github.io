---
name: close-out-tix
description: Finish explicitly selected, reviewed blog or Today I X PRs with a final proofreading pass, validated pushes, squash merges, exact-branch cleanup, and an updated local main. Inspection-only requests remain read-only.
---

# Close out reviewed content

Use the current user request to select the PRs and allowed actions. Read
`LOCAL_PR_TRACKER.md` for review history and branch mappings, then verify them
against Git and GitHub. The tracker is evidence of past work, not new approval.
Do not include other queued or discarded entries unless the request covers them.

## Identify and proofread

1. Run `make help`, read `AGENTS.md`, and inspect the clean/dirty worktree,
   worktrees, branch upstreams, and unpublished commits on local `main`.
2. Fetch/prune and refresh each selected PR's head, base, state, draft flag,
   reviews, and checks. Match its file and title to the recorded review and
   inspect any changes since that reviewed commit. Local and remote branch
   names may differ, such as `tir-...` and `codex/tir-...`.
3. Read each complete post, including frontmatter. Check spelling, word usage,
   grammar, syntax, punctuation, agreement, tense, parallel structure, and
   accidental repetition. Apply only requested mechanical fixes, then reread
   the complete revised prose. Do not invent edits if it is already clean.
4. Check source links, filenames, dates, captions, and assets when present.
   Separate optional structural or substantive suggestions from corrections;
   preserve the author's voice, claims, title, dates, tags, and assets.

**Content selected for merge/publication must use `draft: false`.** The user's
standing preference is non-draft content. Convert any selected entry's
`draft: true` to `draft: false` before validating and merging; Hugo hides
`draft: true`. A GitHub PR's draft/ready state is separate from this frontmatter.
Do not change unrelated existing drafts. Inspection-only requests remain read-only.

## Validate and push

- Inspect the entire diff against fetched `origin/main`, including shared
  tooling inherited from unpublished local-main commits. Do not stage unrelated
  changes or add the local tracker to a commit. Keep the tracker excluded through
  `.git/info/exclude`, not the shared `.gitignore`.
- Use the Hugo version pinned in `vercel.json` and CI. Run `make test`,
  `make test_workflow`, and `git diff --check`. Build without draft/future
  overrides and verify each selected entry's page, section listing, and feed
  in the generated output. Entries under `content/reading/` appear in Reading
  and its feed, not the Posts list. A future date can also hide an entry;
  report it rather than silently changing its date. Use `uv` for Python and
  keep `uv.lock` unchanged during checks.
- Commit only the approved changes. Push with an explicit local-source to
  existing-PR-head refspec, without force-pushing. Verify GitHub's live head is
  exactly the validated SHA, then wait for fresh checks on that SHA.
- With merge approval established, mark selected draft PRs ready. Honor checks,
  reviews, protections, and organizational hooks. A denied or uncertain action
  is not a success: record its result and retain branches until resolved.

## Merge serially and reconcile main

Read `scripts/finish-branch.sh`. Prefer `make finish-branch-online` when its
prerequisites hold: clean worktree, open/non-draft PR targeting `main`, matching
local/PR heads and branch names, and no unpublished local-main commits. The
helper verifies the squash, updates main, and deletes both exact branch names.

Handle these two cases before using the helper:

- **Different local and remote names:** rename the local branch to the verified
  PR head name only if that destination name is unused and no other worktree
  uses it. Record both names. Never guess a remote name for deletion.
- **Unpublished local main included in the selected PR:** preserve its pinned
  tip and verify its changes belong to the approved diff. Merge through
  `gh pr merge <number> --squash --match-head-commit <validated-sha>` instead of
  weakening the helper's guard. Retain all other helper guards: same-repository
  open/ready PR targeting `main`, clean worktree, no unfinished Git operation,
  and a local tip matching the validated live PR head. Verify `MERGED`, fetch,
  and verify the squash
  SHA is reachable from `origin/main` and retains every unpublished change.
  If all old local-main changes are represented and local main still equals
  the pinned tip, `git rebase --onto origin/main <pinned-old-main-tip> main`
  moves the empty remaining range to remote main. Do not use this when any
  change is missing or uncertain; never discard or force-push unpublished main.

After each squash, fetch main and reassess the remaining PR. If needed, merge
main into its published branch without rewriting its history, inspect the
result, rerun checks, push, and wait for checks on the new head before merging.
A queued merge is still pending and does not permit cleanup.

## Verify cleanup and finish

- Delete a kept branch only after its PR is confirmed merged and its squash
  SHA is reachable from fetched main. Check the live remote tip and use an
  exact-SHA lease for remote deletion. A changed tip requires inspection.
- Switch off the local branch and verify its tip and worktree usage before
  deleting it. `git branch -D` is appropriate only for the verified merged
  source, since squash merges replace its commit IDs.
- Handle explicitly discarded PRs separately: close without merging and delete
  only their authorized, verified branches. Leave unrelated PRs untouched.
- End on `main`, run `git pull --ff-only`, and verify a clean tracked worktree,
  `main == origin/main`, intended PR states, and absence of each selected branch
  both locally and remotely. Remote-tracking refs alone do not prove deletion.
- Update the existing local tracker with reviewed/validated head, push result,
  squash SHA, separate local/remote cleanup results, final main SHA, and any
  remaining blocker. Report the outcome, content draft flags, generated URLs,
  and live deployment verification. A successful build alone does not establish
  that the selected content is visible.
