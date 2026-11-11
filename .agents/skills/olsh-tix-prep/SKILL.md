---
name: olsh-tix-prep
description: Pull this website checkout and all remote branches, check repository health, and return the three most recent open TIX PRs for Daniel to review. Use for TIX review preparation, not content close-out.
---

# Prepare the TIX review queue

Refresh this repository and return three recent TIX entries with verified GitHub
PR links. Preparation does not authorize editing content, marking PRs ready,
merging, deleting branches, or deploying. Follow a separately requested skill
change through the repository's normal validation and publication workflow.

## Sync safely

1. Run `make help` first. Read `AGENTS.md` and `README_DEV.md`; inspect status,
   staged changes, branch/upstream, remotes, worktrees, and unfinished Git operations.
   Read `LOCAL_PR_TRACKER.md` if present for completed reviews and discarded items;
   confirm those historical records against live PR states and commits.
2. Pull the current branch with `git pull --ff-only` when its worktree and upstream
   permit it. Preserve edits and unpublished commits. If it cannot fast-forward,
   report the branch's ahead/behind counts; do not reset or rebase content branches
   merely to prepare a review queue. Continue independent read-only checks.
3. Run `git fetch --all --prune`. Ensure each remote's fetch covers all heads;
   if it is narrow, fetch `refs/heads/*` explicitly into that remote's tracking
   namespace without replacing unrelated configuration. Compare `git ls-remote
   --heads <remote>` with fetched refs by name and SHA. Report shallow history.
4. Make every origin branch available locally: create missing tracking branches
   with `git branch --track <name> origin/<name>`. Fast-forward existing branches
   only when the local tip is an ancestor of its verified upstream. For branches
   checked out in another worktree, leave them untouched and report their status.
   For an unchecked-out branch, use `git update-ref` with the expected old SHA to
   guard the update. Preserve ahead, diverged, local-only, and conflicting-name
   branches and report them. Do not merge main into every branch. Verify local
   tips/upstreams and remote-tracking SHAs after the sync.

## Check health

- Check for unresolved conflicts, incomplete Git operations, unexpected worktree
  changes, branch divergence, and submodule status. Run `git diff --check`.
- Read `vercel.json` and CI for the pinned Hugo version; compare `hugo version`
  before running `make test` and `make test_workflow`. Use a matching temporary
  binary via command-scoped PATH if necessary, preserving the global toolchain.
  Keep `uv.lock` unchanged. If inherited `PYTHONSAFEPATH` breaks sibling imports,
  clear it for the check. If an inherited uv index conflicts with the lockfile,
  select the lockfile's registry for that command only.
- Inspect the selected PRs' live heads, changed content, reviews, mergeability,
  and checks. A local main build does not validate unmerged PR content. Label
  draft PRs, missing/pending checks, and content that a production build would
  hide (e.g. `draft: true` or a future date). Inspect without changing it.
- Report observed failures and unavailable checks separately. Retry transient
  network errors with a bounded retry; never describe missing evidence as passing.

## Select the three most recent TIXs

1. Query all open PRs with authenticated `gh`, using pagination or a sufficiently
   large verified limit. Include drafts. Collect number, title, URL, creation time,
   head/base refs, and head SHA. If the list reaches the limit, paginate further.
2. Identify TIXs from the changed content and frontmatter, not only PR titles or
   branch names. Include `content/tix/`, TIX-tagged individual captures, and legacy
   reading captures under `content/reading/`; inspect dated log additions when
   relevant. Exclude blog-only, tooling-only, merged, closed, discarded, and
   unrelated old writing PRs. Treat the local tracker as a hint, not live state.
3. Rank by entry date descending, then PR creation time descending, then PR number
   descending. Use America/Los_Angeles for timestamps. An updated check or comment
   must not make old content appear new. Explain this ordering in the result.
   For a PR with multiple entries, name the entries and use its newest entry date;
   return distinct PRs. Return fewer than three if fewer eligible PRs exist.
4. Fetch/read each shortlisted entry at its live head and match that SHA to the
   fetched ref. Use the entry's actual title and date. Recheck PR state/head and
   report check summaries; unknown mergeability or missing checks stays unverified.

## Return

Give a compact sync/health result and a table with rank, entry title, entry date,
GitHub PR link, and any material review concern. State the number of remote and
local branches verified and disclose preserved divergence or failed checks.
End with the resulting checkout branch and cleanliness. Do not claim there are
no issues unless the named checks support that conclusion. Do not merge TIX PRs.
