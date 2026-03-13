---
title: "How we automate tests for the Grove API"
date: 2026-03-10T17:52:21-0700
draft: false
description: "Streamlining code reviews on a few repositories with a few developers in Claude Code."
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

_P.S. I took the images on my widescreen monitor while working on a real feature. If this tracks interest, happy to put together small screenshtos or a walkthrough video._

---

## Code Reviews are ~~the new~~ still the Bottleneck

Seems like everyone is talking about how code reviews are the new bottleneck in the era of agentic software development.

There is some truth to it, but if you've been aroud long enough, you know it's not new news. It's just that the problem, approach and solution look a little differently. They're not the same, but they rhyme.

There are lots of approaches, tools and companies out there tackling this problem.

We've tried or looked into [Claude CodeReview](https://code.claude.com/docs/en/code-review), [CodeRabbit](https://www.coderabbit.ai), [ProperlCode](https://www.propelcode.ai). They're all good, and will get you at least half of the way there. However, the other half is the hard one. It's the one that's specific to your domain, your product, your tech stack, your culture, your taste.

This is just a quick show-and-tell of our lightweight, custom tailored, simple, and easy to use. Most imporantly, it meets the developer where they are.

---

## The Stack

Backend: Grove API
Frontend: Grove API
Chrome Extension: Grove Extension

The majority of these codebases were developed in an agent-first environment.

The code from the frontend and extension is what some would refer to as "vibe coded".

The backend is a bit more mature and reviewed in depth because it deals with transferring funds. I personally still review the core logic line by line, but haven't written a single line of it myself.

## Step 1: Kick off the review via `/grove_*_review`

Each repo I mentioned has a custom local slash command that kicks off the review:

- `/grove_app_review`
- `/grove_api_review`
- `/grove_extension_review`

The command does a handful of things: git diff against the default branch, build context, cosmetic changes, following our best practices, etc.

Let's assume you just ~~vibe-coded~~ engineered a big new feature with the help of agents, and it's time to start reviewing your work.

‼️ Like any `AGENTS.md` file, this is not a one-and-done. Documentation is a living being. It's the responsibiliy of both the human and the agent to update and review these commands and files on a regular (daily?) basis whenever something new is learned, a pattern is observed, or a change takes place.

![Kicking off the three review skills in parallel](/images/posts/2026-03-10-grove-api-1-grove-review.png)

## Step 2: DO ALL THE THINGS

Once the initial review is complete, it comes back with a report, a summary, and a list of actionables.

The list of actionables covers a lot of things that we've learnt we need to manage: update docs or flows, fix terminology, add unit/integration/e2e tests, add logs, follow other patterns, linting, etc. Running end-to-end tests is one of the most imporant things it does.

Usually I tell it to `DO ALL THE THIHNGS`, but it really depends on a case-by-case basis.

![Running local server, E2E tests, and best practice checks](/images/posts/2026-03-10-grove-api-2-do-all-the-things.png)

## Step 3: Review the results

Here, the human is responsible to actually review the results and see what happened and jump in to help.

In this particular case, docker wasn't running, so the end-to-end tests couldn't start. Not a big deal, but something I prefer to avoid delegating to an agent.

![Review results with categorized findings](/images/posts/2026-03-10-grove-api-3-review-results.png)

## Step 4: E2E Test Results

This is one of my favorite parts of the API.

It spins up a database, spins up the server and starts running realistic end-to-end flows against it. Happy paths, sad paths, chaotic paths. You name it!

If something fails, the agent tries to diagnose the root cause before surfacing it. No "test failed" without context — it tells you _why_.

Claude also fixes some of them (if trivial) along the way, and is informed not to fix it if the change in the business logic is qusiontable or requires another opinion.

The E2E tests report back with a clear pass/fail matrix.

![E2E test results showing pass/fail status](/images/posts/2026-03-10-grove-api-4-e2e-test-results.png)

## Step 5: Pull Request Sweep

From here, I use my personal agent skills before I go into manual review.

In particular, I've found that `cmd-pr-sweep` from [Olshansk/agent-skills](https://github.com/Olshansk/agent-skills) has been great at catching major regressions, bugs and limiting how much tech debt we're taking on.

![PR sweep running across the changeset](/images/posts/2026-03-10-grove-api-5-pr-sweep.png)

I review it manually and choose if/what to fix.

If something feels like too big of a change and out of scope for the work, I ask the agents to add TODOs with a lot of contenxt. Havin it inline is a great way to give future agents contexts on the techdebt.

This is the last gate before a human looks at the PR.

![Sweep results with final summary and action items](/images/posts/2026-03-10-grove-api-6-sweep-results.png)

## Step 6: Prepare and upload the PR

Once everything passes, I commit, push and generate a PR description using `/cmd-pr-description`.

The skill reads the full diff, commit history, and review findings, then drafts a structured description with a summary, feature diff table, and technical details.

![Running /cmd-pr-description to generate the PR](/images/posts/2026-03-10-grove-api-7-cmd-pr-description.png)

Here is what it looks like on GitHub:

![The final PR description on GitHub](/images/posts/2026-03-10-grove-api-8-pr-description.png)

## Other Specical Mentions

This isn't intended to be a "how I code" post, but I wanted to call out some of the other biggest patterns I found useful right now:

- **Cross-referencing with other models**: Depending on the size and complexity, I like to cross-reference plans and bugs with Gemini and Codex. I've found Gemini to be very idiomatic and great at frontend. Codex is great at architecture and challenging requirements.
- **Manual Review**: I don't review frontend code manually, but I still review mission critical business logic line-by-line on GitHub. I leave comments (locally or remotely) and have agents pick it up. I put a lot of focus on reduce code surface area, regression testing important edges cases, naming (functions, variables, etc) and ensuring TODOs with explanations are in place.
- [`/session-commit`](https://github.com/Olshansk/agent-skills/blob/main/skills/session-commit.md): I leverage this quite a lot to keep `AGENTS.md` updated based on learnings from the most recent agent session.

Depending on how much work happened during this part of the review, I might go back and start the process over again.

Not every change needs this, but for architectural decisions or tricky edge cases, it's useful to get a second (and third) opinion from a different model.
