---
title: "How I code in 2025 - Having written my first line of code in 2004"
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

Other pro tips:

- Hotkeys for switching between plan & thinkin mode
- Telling the AI to spend a bunch of time
- Show a diagram but also a tree screenshot of codex, gemini and claudes
- --yolo mode in codex is great
- Resuming conversations is great.
- People ask how I automate communication between agents. I just ask thhem to give me a blurb that I cpy opaste
- Periodically tell CLAUDE to remember patterns. E.g. I really like emojis and colors in my log lines, so I build patterns along the way. "Teaching it" to your team is as simple as #memorize
- Link to the person who create claude code
- Codex has the worse UI
- Gemini has the best UI

There's no going back to a world where we write code.

If I don't access to an internet connection where I can leverage the leading models from frontier labs, I use it

This blog post is going to be pretty long and mainly act as a reference of tools, tips and tricks I use for software developement.

If you're just a casual reader, the only section I recommend you don't skip is the first one

- [Orchesstrating an ensemble: Codex, Geminis \& Claudes](#orchesstrating-an-ensemble-codex-geminis--claudes)
- [My Stack](#my-stack)
- [All About I/O](#all-about-io)
- [Vibe Coding vs AI-Driven](#vibe-coding-vs-ai-driven)
- [Code Reviews](#code-reviews)
- [Slash Commands](#slash-commands)
- [Make Targets](#make-targets)
- [Tests:](#tests)
- [Documentation](#documentation)
- [What is AI really **Good** at?](#what-is-ai-really-good-at)
- [What is AI really **Bad** at?](#what-is-ai-really-bad-at)
- [How will teams change?](#how-will-teams-change)
- [Some Meta Points](#some-meta-points)
- [Rough Notes](#rough-notes)

## Orchesstrating an ensemble: Codex, Geminis & Claudes

- It’s not automation, and not semi automation, it’s orchestration.
- Like a conductor with a lot of skilled musicians

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

## My Stack

- Gemini: yes, for nano banna
- ChatGPT: Main driver. Lots of projects where I can just copy-paste stuff and it knows what to do
- Claude: used to use it but no more.

IDE:

- Was on VSCode
- Switched to Windsurf
- Now on antigravity

## All About I/O

- I define the inputs and outputs
- I use make commands
- I have extensive integration tests
- I only look in the code when something works, is stuck or it’s time for a major checkpoint
- I don’t look at code for front end frameworks but also don’t work on big he’s

## Vibe Coding vs AI-Driven

AI Driven engineering is not vibe coding

- One is for backend, core Haines logic and production
- The other is for front end (simple) and prototypes
- Caveat is large frontend codebases that need to scale

- Create an image of a tree show me, codex, Gemini and then Claude
- 1 codex
- 2 Gemini
- 4 claude
- In the future, many more

## Code Reviews

At the age of 19, on my first day On of my first of my

- Ryan Perry, when I was 19: "You will review a lot more code than youw rite"

- Bandaids vs solutions
- Deleting vs writing code

- I still review all the code
- I don’t write any code by hand
- Even if I need to rename something, I usually ask an LLM to do it.

When do I look at the code?

- It works and I'm ready to review
- It's in a non working spiral and there's no need to keep burning tree

## Slash Commands

My most commonly used slash commands:

- I have a command for resolving merge conflicts
- I have a command for reviewing code
- I have a command for building context to prepare for code reviews
- A helper to prepare for code reviews
- A helper to clean code
- A helper to write documentation the way you want it

## Make Targets

Orchestrator

Make targets:

- Make targets for everything

- Add todos everywhere, more important than before
- Be careful of production code vs prototypes, different mindsets

## Tests:

- I ask to add unit tests, but I don't look at the code of unit tests anymore.
- I iterate heavily on the input/output of E2E tests, but I don't look at the code.
  - Good toold & make commands
  - Easy for me to run tets

Things I find myself doing often:

## Documentation

Anyone who has ever worked with me know how much of a :pita: I am when it comes to documentation.

This is what I ask for:

- Bullet Points
- Copy-pasta friendly
- Reduce cognitive overhead
- No filler
- The "how" should be at the end, optional or in an expandable section

I've found AI to be good at editing documentation, but I personally hate the documentation it writes.

It feels like the difference of how I was taught to write in school, with a focus on page and word counts rather than delivering value.

## What is AI really **Good** at?

- Ai is really good at following instructions
- Scaffolding and solving micro problems
- Solving local problems
- Doing the things that "you have to do"

## What is AI really **Bad** at?

- Solving global problems
- Solving long term problems
- Solving problems that require a lot of context
- Knowing what problem to solve

- Overdoing it with interfaces
- Adding unncessary features. They're one-day nice-to-haves, but reducing the surface area of chanes, features, and code is how you prevent noise or feature creep.
- Reimplmenting things rather than reusing, refactoring or consolidating things, if not prompting.

## How will teams change?

Meta takeaways on how teams will change:

- You won’t need anyone who doesn’t have agency of their own
- But, it’s a very great sounding board. No longer do we need to use people as rubber ducks, because we have digital gizmoducks
- It’s still your job to get a picture of the product, codebase, and and user problem

Engineering leaders

- Often graduate from writing code to giving directions and making plans.
- Periodically check in
- Now that’s everyone

## Some Meta Points

A friend of mine says that the release of ChatGPT is like letting a "Geniue out of the bottle". Once you do, there's no going back.

1. **Planning** - Ask the LLM to build a plan and review it.
2. **Thinking** - Tell the LLM to spend at least X minutes on a task, and not come back to you until it spent that much time deeply investigating a problem, solution or building a plan

## Rough Notes

- Reduce branching
- Add logging (And don't overdo it)
- Use dataclasses
- Don't overimplement things I don't need
- Don't overnegineer
- Copy-paste a lot of error logs into the CLI

- Clean interfaces
- Following patterns
- Reusing rather than reimplementing
- Reducing the code surface area

- Today, I:

  - Write a long prompt/spec
  - Ask it to review the code in depth
  - take its time
  - Build a plan
  - Ask quesitons

- Up until recently, I had 5 senior engineers on my team, and I was reveiwign a lot of cod

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
-
- Make command for E2E tests that exercises everything
- You can use this in smoke tests in your CI and for your agent to make sure thngs work
- Modes of implementation
  - Working closely with one agent (pair coding)
  - Managing many agents (managing)
  - Planning (planning, thinking, writing and prioritizing has not gone away)
  - Gizmoducking: like rubber ducking but with a much more intelligent duck. This is the common "give me 10 ideas for X" but you are the one who comes up with X.
