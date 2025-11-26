---
title: "Poor Man's Merge Conflict Resolver"
date: 2025-11-26T10:40:19-0500
draft: false
description: "A claude tool to help resolve merge conflicts"
tags: ["claude", "merge conflict resolver", "git", "coding", "ai"]
categories: ["post"]
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

One thing I am building a muscle in is converting repetative tasks into [Claude Slash Commands](https://code.claude.com/docs/en/slash-commands).

Even though I don't write code by hand, I still direct and architect how the critical parts of the code are written.

Part of this involves resolving merge conflicts. I'm sharing that slash command below.

**A general purpose trick which I've found to work very well is to permit AI agents to ask for clarification, help and direction if they are unsure**. It enables me to avoid doing the work myself, while preventing the ping-pong back and forth of errors.

Here is how I ended my prompt for reference:

> If you are not sure how a conflict should be resolved, stop and ask me for direction or clarification.
>
> 1. Show me the conflicting chunks
> 2. Explain what you believe you should do
> 3. Wait for confirmation

The full `~/.claude/commands/cmd_merge_conflict_resolver.md` is below:

<details>
<summary>Click to slash command</summary>

```markdown
# Resolve Merge Conflicts <!-- omit in toc -->

Your job is to resolve merge conflicts in the current branch of the current repo.

- [1. Preparation](#1-preparation)
- [2. Build context](#2-build-context)
- [3. Resolve conflicts](#3-resolve-conflicts)
- [Very Important: Don't be afraid to ask for help](#very-important-dont-be-afraid-to-ask-for-help)

## 1. Preparation

Assume I already ran:

\`\`\`bash
git checkout main
git pull
git checkout <current_branch>
git merge main
\`\`\`

If this command is being invoked, there are unresolved merge conflicts you need to fix.

## 2. Build context

1. Run `git diff main` to understand the changes in this branch relative to `main`.
2. Run `rg "<<<<<<<"` to find all merge conflicts.

## 3. Resolve conflicts

For each conflict, decide whether to:

1. Keep **our** changes (the current branch)
2. Keep **their** changes (`main`)
3. Use a careful, intelligent combination of both

In most cases you should aim for (3), but correctness matters more than cleverness.

When you are confident about how to resolve a conflict:

1. Edit the file to the desired final state
2. Remove all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Save the file and run any relevant checks or tests if practical
4. Stage the resolved files with `git add`

## Very Important: Don't be afraid to ask for help

If you are not sure how a conflict should be resolved, stop and ask me for direction or clarification.

1. Show me the conflicting chunks
2. Explain what you believe you should do
3. Wait for confirmation

Now go resolve the conflicts.
```

</details>
