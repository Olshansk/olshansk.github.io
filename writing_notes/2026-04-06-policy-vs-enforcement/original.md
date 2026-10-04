---
title: "Policy vs Enforcement"
date: 2026-04-06T15:55:05-0700
draft: false
description: ""
tags: ["AI", "Agents", "Workflows"]
categories: ["Thoughts"]
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

Policy and enforcement are two very different things.

I asked both Claude and GPT to follow specific rules during a session. Both needed reminders. The instructions were there. The policy was clear. But neither agent enforced it on its own.

![Policy vs Enforcement](/images/2026-04-06-policy-vs-enforcement.png)

This is the same pattern everywhere:

- A `CLAUDE.md` or `AGENTS.md` file is a policy doc, not an auto-linter
- A code review skill is a workflow, not a guardrail that prevents bad code from being written
- Documentation tells you what _should_ happen, not what _will_ happen

I wrote about this before in the context of [`/session-commit`](/posts/2026-02-27-one-agent-skill-to-replace-a-5m-raise/) — the whole point of that skill is to capture learnings so agents don't repeat mistakes. But even that is policy. If the agent doesn't run it, or the human forgets to invoke it, the knowledge is lost.

The instruction was already there. The implementation slipped past it. The enforcement layer is where things actually get caught — or don't.
