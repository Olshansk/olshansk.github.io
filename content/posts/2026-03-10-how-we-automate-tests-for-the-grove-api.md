---
title: "What Semi-Automated Code Reviews with Claude Code Look Like at Grove"
date: 2026-03-10T17:52:21-0700
draft: false
description: "Streamlining code reviews for a content earnings platform with agents."
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

_P.S. I took the images on my widescreen monitor while working on a real feature. If there's interest, I'm happy to put together smaller screenshots or a walkthrough video._

---

## TL;DR

Our workflow today looks roughly like this:

- Kick off an agent review locally via `/grove_*_review`
- The agent reviews the diff, runs best-practice checks, and spins up the system locally
- Full **E2E flows run automatically** (happy, sad, chaotic paths)
- Failures are diagnosed with context instead of just “test failed”
- A **PR sweep** catches regressions and tech-debt risks
- Humans review mission-critical logic manually
- A final PR description is generated automatically

![Semi-automated code review workflow](/images/posts/2026-03-10-grove-api-workflow.png)

**The key idea**: Leverage tools off the shelf, semi (not completely) automate things specific to your domain, and do as much of it locally as possible.

---

## Code Reviews are ~~the new~~ still the Bottleneck

It seems like everyone is talking about how code reviews are the new bottleneck in the era of agentic software development.

There is some truth to it, but if you've been around long enough, you know it's not new. The problem just looks a little different now. The approach and the solutions are evolving. **They're not the same, but they rhyme.**

There are lots of approaches, tools, and companies tackling this problem.

We've tried or looked into [Claude CodeReview](https://code.claude.com/docs/en/code-review), [CodeRabbit](https://www.coderabbit.ai), and [PropelCode](https://www.propelcode.ai). They're all good and will get you at least halfway there.

However, the other half is the hard one.

**It's the part that's specific to your domain, your product, your tech stack, your culture, and your taste.**

This is just a quick show-and-tell of our lightweight workflow around Claude Code. It's simple, custom-tailored, and easy to use.

**Most importantly, it meets developers where they already are.**

---

## The Stack

Three repos:

- **Grove API** (Backend)
- **Grove App** (Frontend)
- **Grove Extension** (Chrome Extension)

The majority of these codebases were developed in an agent-first environment.

The code in the frontend and extension is what some would refer to as _”vibe-coded”_.

The backend is a bit more mature and reviewed in depth because it deals with fund management. **I still review the core logic line-by-line, but I haven't written a single line of it myself.**

---

## CI vs Local Automation

We still run traditional CI, but the role has changed.

Traditional CI only runs **linting and unit tests**.

The heavier work happens locally, and integrate (not replace) the human. The agent spins up the stack, runs E2E flows, and performs the review before a PR even exists.

This approach is similar to the direction described by [DHH when moving CI back to developer machines](https://world.hey.com/dhh/we-re-moving-continuous-integration-back-to-developer-machines-3ac6c611).

Our end-to-end tests also double as **production smoke tests** that run on GitHub after deployment. 🔥

---

## Step 1: Kick off the review via `/grove_*_review`

Each repo has a custom local slash command that kicks off the review:

- `/grove_app_review`
- `/grove_api_review`
- `/grove_extension_review`

The command does a handful of things:

- runs `git diff` against the default branch
- builds context for the agent
- checks cosmetic changes
- validates best practices
- prepares E2E testing

Let's assume you just ~~vibe-coded~~ engineered a big new feature with the help of agents, and it's time to start reviewing your work.

‼️ Like any `AGENTS.md` file, this is not one-and-done. I use [`/session-commit`](https://github.com/Olshansk/agent-skills/blob/main/skills/session-commit/SKILL.md) to keep it updated.

**Documentation is a living thing. It's the responsibility of both the human and the agent to update and review these commands and files regularly whenever something new is learned, a pattern emerges, or a change happens.**

![Kicking off the three review skills in parallel](/images/posts/2026-03-10-grove-api-1-grove-review.png)

---

## Step 2: DO ALL THE THINGS

Once the initial review completes, it returns a report, a summary, and a list of actionables.

The actionables cover many things we've learned we need to manage:

- updating docs or flows
- fixing terminology
- adding unit/integration/e2e tests
- adding logs
- following existing patterns
- linting

Running end-to-end tests is one of the most important steps.

Usually I tell it to `DO ALL THE THINGS`, but it really depends on the situation.

![Running local server, E2E tests, and best practice checks](/images/posts/2026-03-10-grove-api-2-do-all-the-things.png)

---

## Step 3: Review the results

Here the human actually reviews the results and jumps in where needed.

In this particular case, Docker wasn't running, so the end-to-end tests couldn't start. Not a big deal, but something I prefer not to delegate to an agent.

![Review results with categorized findings](/images/posts/2026-03-10-grove-api-3-review-results.png)

---

## Step 4: E2E Test Results

This is one of my favorite parts of the API.

It spins up a database, starts the server, and runs realistic end-to-end flows against it.

Happy paths, sad paths, chaotic paths. 🎢

Everything.

If something fails, the agent tries to diagnose the root cause before surfacing it.

**No “test failed” without context. It tells you _why_.** 🔍

Claude also fixes some of them (if trivial) along the way, and is instructed not to fix anything where the business logic change is questionable or requires another opinion.

The E2E tests report back with a clear pass/fail matrix.

![E2E test results showing pass/fail status](/images/posts/2026-03-10-grove-api-4-e2e-test-results.png)

---

## Step 5: Pull Request Sweep

From here, I use my personal agent skills before moving into manual review.

In particular, I've found that `cmd-pr-sweep` from [Olshansk/agent-skills](https://github.com/Olshansk/agent-skills) is great at catching major regressions, bugs, and limiting how much tech debt we're taking on.

If you're curious, the skills can be installed with:

```bash
npx add skills olshansk/agent-skills
```

![PR sweep running across the changeset](/images/posts/2026-03-10-grove-api-5-pr-sweep.png)

I review it manually and decide what to fix.

If something feels too big or out of scope for the work, I ask the agents to add TODOs with a lot of context.

**Having that inline is a great way to give future agents context about the tech debt.**

This is the last gate before a human looks at the PR. 🚧

![Sweep results with final summary and action items](/images/posts/2026-03-10-grove-api-6-sweep-results.png)

---

## Step 6: Prepare and upload the PR

Once everything passes, I commit, push, and generate a PR description using `/cmd-pr-description`.

The skill reads the full diff, commit history, and review findings, then drafts a structured description with a summary, feature diff table, and technical details.

![Running /cmd-pr-description to generate the PR](/images/posts/2026-03-10-grove-api-7-cmd-pr-description.png)

Here is what it looks like on GitHub:

<img src="/images/posts/2026-03-10-grove-api-8-pr-description.png" alt="The final PR description on GitHub" style="max-width: 75%;" />

---

## Other Special Mentions

This isn't intended to be a “how I code” post, but I wanted to call out some of the patterns I've found useful lately:

- **Cross-referencing with other models**
  Depending on the size and complexity, I like to cross-reference plans and bugs with Gemini and Codex. Gemini tends to be very idiomatic and strong at frontend work. Codex is great at architecture and challenging requirements. Not every change needs this, but for architectural decisions or tricky edge cases, **it's useful to get a second or third opinion from another model.**

- **Manual review**
  I don't review frontend code manually, but I still review mission-critical business logic line-by-line on GitHub. I leave comments (locally or remotely) and have agents pick them up. **I focus heavily on reducing code surface area, regression testing important edge cases, naming, and ensuring TODOs with explanations are in place.**

- [`/session-commit`](https://github.com/Olshansk/agent-skills/blob/main/skills/session-commit.md)
  I use this frequently to keep `AGENTS.md` updated based on learnings from the most recent agent session.

Depending on how much work happened during this stage of the review, I might go back and start the process again.

<!--
```mermaid
flowchart

A["👨‍💻 Developer finishes feature"]

A -\->|/grove_*_review| B["🤖 Build context<br/>→ Review diffs<br/>→ Suggest fixes<br/>→ Suggest updates<br/>→ tests<br/>→ docs<br/>→ logs"]

B -\->|👨‍💻 DO ALL THE THINGS| D["🤖 Apply fixes + run checks<br/>→ Spin up local stack<br/>→ Run E2E flows<br/>→ Diagnose failures with context"]

D -\->|/cmd-pr-sweep| G["🤖 Regression + tech-debt sweep"]

G -\-> H["👨‍💻 Manual review<br/>→ business logic<br/>→ naming<br/>→ edge cases<br/>→ reduce surface area<br/>→ TODOs with context"]

H -\->|/cmd-pr-description| I["🤖 Generate PR description"]

I -\-> J["📦 GitHub PR"]

J -. optional: iterate again .-> A

%% Styles
classDef human fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#0d47a1
classDef agent fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#1b5e20
classDef output fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#e65100

class A,H human
class B,D,G,I agent
class J output
```
-->
