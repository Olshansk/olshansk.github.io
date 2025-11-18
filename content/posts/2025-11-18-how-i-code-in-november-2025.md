---
title: "How I code in November 2025"
date: 2025-11-18T09:08:01-0500
draft: true
description: ""
tags: []
categories: []
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

Potential Titles:

- Reflections on coding in 2025
- 3 years of ChatGPT (follow on)
- All of my tips & tricks for using claude code and codex
-

Verifiably blog post

- https://karpathy.bearblog.dev/verifiability/

Introduction:

- I still review all the code
- I don’t write any code by hand

My goals are:

- Clean interfaces
- Following patterns
- Reusing rather than reimplementing
- Reducing the code surface area

Things I find myself doing often:

- Reduce branching
- Add logging (And don't overdo it)
- Use dataclasses
- Don't overimplement things I don't need
- Don't overnegineer
- Copy-paste a lot of error logs into the CLI

Common tips:

- A helper to prepare for code reviews
- A helper to clean code
- A helper to write documentation the way you want it

Pro tips:

- Make command for E2E tests that exercises everything
- You can use this in smoke tests in your CI and for your agent to make sure thngs work
- Modes of implementation
  - Working closely with one agent (pair coding)
  - Managing many agents (managing)
  - Planning (planning, thinking, writing and prioritizing has not gone away)
  - Gizmoducking: like rubber ducking but with a much more intelligent duck. This is the common "give me 10 ideas for X" but you are the one who comes up with X.

What AI is good at:

- Ai is really good at following instructions
- Scaffolding and solving micro problems
- Solving local problems
- Doing the things that "you have to do"

AI is bad at:

- Solving global problems
- Solving long term problems
- Solving problems that require a lot of context
- Knowing what problem to solve

Meta takeaways on how teams will change:

- You won’t need anyone who doesn’t have agency of their own
- But, it’s a very great sounding board. No longer do we need to use people as rubber ducks, because we have digital gizmoducks
- It’s still your job to get a picture of the product, codebase, and and user problem
