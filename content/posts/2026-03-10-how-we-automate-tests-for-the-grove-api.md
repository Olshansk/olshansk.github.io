---
title: "How we automate tests for the Grove API"
date: 2026-03-10T17:52:21-0700
draft: false
description: "A walkthrough of how we use Claude Code skills to automate reviews, E2E tests, and PR sweeps for the Grove API."
tags: ["AI", "Claude Code", "Testing", "Automation", "Developer Tools", "Grove"]
categories: ["Posts"]
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

We've been building a development workflow for the [Grove API](https://grove.city) that leans heavily on Claude Code skills and slash commands.

The goal: run a single command and have the agent spin up local services, run E2E tests, review its own code, pull in GitHub comments, and sweep for issues — all before a human ever looks at the PR.

Here's how it works.

## Step 1: Kick off the review

We have three custom skills that handle different phases of a review:

- `grove_api_review` — context gathering and code analysis
- `grove_api_review` (phase 2) — content and pattern checking
- `grove_extension_review` — extension-specific review that gathers context and runs tests in parallel

![Kicking off the three review skills in parallel](/images/posts/2026-03-10-grove-api-1-grove-review.png)

Each skill starts by checking out the branch, collecting diffs, and listing changed files.
They run in parallel across three terminal panes — one per review phase.

## Step 2: Do all the things

Once the review skills are running, Claude spins up a local server and runs the full suite.

This is the "do all the things" step:

- Spin up a local development server
- Run E2E tests against it
- Follow best practices and patterns from our `AGENTS.md`

![Running local server, E2E tests, and best practice checks](/images/posts/2026-03-10-grove-api-2-do-all-the-things.png)

The key here is that the agent doesn't just run tests blindly.
It reads the project's conventions and applies them as part of the review.

## Step 3: Review results

After the review skills finish, each one reports back with findings organized by severity.

![Review results with categorized findings](/images/posts/2026-03-10-grove-api-3-review-results.png)

Findings are tagged as blockers, warnings, or suggestions.
The agent leaves comments on the GitHub PR as a self-review — and on the next run, it pulls those comments back in as context.

## Step 4: E2E test results

The E2E tests report back with a clear pass/fail matrix.

![E2E test results showing pass/fail status](/images/posts/2026-03-10-grove-api-4-e2e-test-results.png)

If something fails, the agent tries to diagnose the root cause before surfacing it.
No "test failed" without context — it tells you _why_.

## Step 5: PR sweep

Before marking a PR ready for human review, we run a sweep.

The sweep cross-references the changes against:

- Known patterns in the codebase
- Previous review comments
- Common pitfalls we've documented

![PR sweep running across the changeset](/images/posts/2026-03-10-grove-api-5-pr-sweep.png)

## Step 6: Sweep results

The sweep produces a final summary with actionable items.

![Sweep results with final summary and action items](/images/posts/2026-03-10-grove-api-6-sweep-results.png)

This is the last gate before a human looks at the PR.

## Step 7: Prepare and upload the PR

Once everything passes, we run `/cmd-pr-description` to generate the PR description.

The skill reads the full diff, commit history, and review findings, then drafts a structured description with a summary, feature diff table, and technical details.

![Running /cmd-pr-description to generate the PR](/images/posts/2026-03-10-grove-api-7-cmd-pr-description.png)

The result is a clean, well-structured PR on GitHub — ready for human review without any manual write-up.

![The final PR description on GitHub](/images/posts/2026-03-10-grove-api-8-pr-description.png)

## Cross-referencing with other models

Depending on the complexity of the change, we periodically cross-reference across Codex and Gemini for other points of view.

Not every change needs this, but for architectural decisions or tricky edge cases, it's useful to get a second (and third) opinion from a different model.
It catches blind spots that come from any single model's training distribution.

## Keeping the workflow fresh

We use a personal `/session-commit` skill to capture learnings from each coding session and update our `AGENTS.md`.

This means the review skills, test patterns, and sweep rules evolve over time.
Every session that surfaces a new pattern or gotcha gets folded back into the instructions the agent follows next time.

---

The end result: by the time a human reviews the PR, the obvious stuff is already handled.
The reviewer can focus on design decisions and business logic instead of style nits and test coverage gaps.
