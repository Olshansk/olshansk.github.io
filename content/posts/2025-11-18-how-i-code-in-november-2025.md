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

Visual to create:

- Create an image of a tree show me, codex, Gemini and then Claude
- 1 codex
- 2 Gemini
- 4 claude
- In the future, many more

IDE:

- Was on VSCode
- Switched to Windsurf
- Now on antigravity

When do I look at the code:

- It works and I'm ready to review
- It's in a non working spiral and there's no need to keep burning tree

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

## Personalities & Responsibilities

Claude

- Claude for implementation and features
- You have an army of Claude mi/senior engineers. You have a dozen Gemini principals. You have a handful of hands on codex directors and managers.
- Claude has style and taste.
- Easier tasks AND more tasks

Codex

- Codex for me planning and scaffolding
- Codex is the best orchestration.

Gemini

- Gemini for bug tracking
- Gemini is smart and can go into the details (bugs, security, hard problems).
- TODO finder

## Roles

CLI:

- Gemini, codex, claude

UI:

- Gemini: yes, for nano banna
- ChatGPT: Main driver. Lots of projects where I can just copy-paste stuff and it knows what to do
- Claude: used to use it but no more.

Engineering leaders

- Often graduate from writing code to giving directions and making plans.
- Periodically check in
- Now that’s everyone

Rough

- Ryan Perry, when I was 19: "You will review a lot more code than youw rite"
- Up until recently, I had 5 senior engineers on my team, and I was reveiwign a lot of cod
- Today, I:
  - Write a long prompt/spec
  - Ask it to review the code in depth
  - take its time
  - Build a plan
  - Ask quesitons
- We go back and forth
- I focu on:
  - not shitty documentaiton
  - Good toold & make commands
  - Easy for me to run tets
- Once the product works
  - I start reviewing on githb
  - I tell it how to rename, refactor, rewrite
  - I go line by line
  - I structure it well
- This is very necesary so future lLMs follow good pattens
- BUT, I don't write code myself...
- It kind of feels like how tony stark operated
- I don't write code anymore
- Par
