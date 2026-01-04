---
title: "How I code going into 2026 - Having written my first line of code in 2004"
date: 2026-01-04T09:08:01-0500
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

## What do I want people to really take away?

### Old / Present:

- I don't write code by hand
- I review code when I need to:
- I don't look at code by hand
- Creating commands if I repeat myself
- Only skill I have is for makefiles

### New / upcoming:

- Review all the pro tips
- Making use of CLAUDE better in shared environments
- Trying out tools like conductor

## My First Lines of Code

At the age of 11 in 2003, I wrote my first line of code. I was a Game Master for DragonBall Z MMORPG on [byond.com](https://www.byond.com/). Other than creating a cool looking pixel art item, I don't remember the language it was in or any of the details.

At the age of 14 in 2007, I had to take a programming course as part of my highschool's [Math and Computer Sciences (MaCS)](https://schoolweb.tdsb.on.ca/wlmac/MaCS-Program) curriculum. We used a language called [Turing](<https://en.wikipedia.org/wiki/Turing_(programming_language)>) that is likely unknown to manny.

At the age of 16 in 2009, I took the Advanced Placement (AP) Computer Science course after spending a whole year coding in Java.

From there, I had experience writing code in a variety of languages spanning both academic and professional settings: Prolog, JavaScript, Objective-C, C++, Erlang, Elixir, Swift, Python, Go, and probably a few others that don't pop to mind right away. This spanned roles including iOS development at ModiFace, Android at Google, Full Stack At Twitter, backend ML infrastructure at Magic Leap, AI eval at Waymo, Blockchain R&D at Pocket Network, etc...

It's been about 6 months since I have manually written a line of code, and it's hard to believe that I may never write a line of code by hand again.

Some are struggling with the transition, but I don't find it bittersweet. From my perspective, we can finally just focus on what matters: product & engineering.

- [What do I want people to really take away?](#what-do-i-want-people-to-really-take-away)
  - [Old / Present:](#old--present)
  - [New / upcoming:](#new--upcoming)
- [My First Lines of Code](#my-first-lines-of-code)
- [How I code going into 2026](#how-i-code-going-into-2026)
- [Orchestrating Agent Personalitites](#orchestrating-agent-personalitites)
- [My Tech Stack](#my-tech-stack)
- [Reviewing Code](#reviewing-code)
- [Modes of Operation](#modes-of-operation)
  - [What more do I want of agents?](#what-more-do-i-want-of-agents)
  - [What more do I want of agents?](#what-more-do-i-want-of-agents-1)
- [Other pro tips:](#other-pro-tips)
- [My Stack](#my-stack)
- [All About I/O](#all-about-io)
- [Vibe Coding vs AI-Driven](#vibe-coding-vs-ai-driven)
- [Code Reviews](#code-reviews)
- [Slash Commands](#slash-commands)
- [Makefiles](#makefiles)
- [Tests:](#tests)
- [Documentation](#documentation)
- [What is AI really **Good** at?](#what-is-ai-really-good-at)
- [How will teams change?](#how-will-teams-change)
- [Make commands](#make-commands)
- [A handful of random pro tips:](#a-handful-of-random-pro-tips)
- [Rough Notes](#rough-notes)
  - [My favorite blogs](#my-favorite-blogs)
  - [TODO](#todo)

## How I code going into 2026

I wanted to capture how I do Software Engineering going into 2026. In part, to share my workflow with others. In part, to have something to reflect on in the future.

Prior to our pivot at [Grove](https://grove.city/) in October of 2025, I had 5 senior engineers on my team; _it's worth mentioning that myself and rest of the C-suite are all hands on across the entire stack_

Today, this pyramid of agents are reporting to me:

![Agent Directory](/images/posts/how-i-code-going-into-2026/agent_pyramid.jpeg)

I no longer write any code by hand from scratch, at all.

I'll dive into some of my tips and tricks, but 4 Claudes, 2 Geminis and 1 Codex via the CLI captures tha majority of how I operate day-to-day.

## Orchestrating Agent Personalitites

Manging agents isn't just about specifying the direction and developing automation, it's about orchestration.

In a symphony, the conductor is the one who is making the decisions, but the musicians are the ones who are doing the work. No matter how skilled the musicians are, they are following the conductor's direction and order.

I do not believe this part will ever be automated away. It's the irreplaceable piece people refer to as **taste** nowadays.

A big part of orchestrating agents is understanding their strengths, weaknesses and personalities. No different than how you learn to work with a team of people, with the exception that they don't get tired and are unemcubred by emotion.

I've realized that the personality and abilities of each agent reflect the organizations by which they are built.

**Codex (OpenAI)**: The Manager, Director, or VP. Great for planning, scaffolding, and setting direction. In tech firms, it's commonly known as L8+.
**Gemini (Google)**: The Architect or Principal Engineering. Great at solving hard problems from AI implementation to low-level optimizations. Great at design docs, fixing complex bugs, identifying security vulnerabilities, and laying out out code should be refactored. In tech firms, it's usually the L6 or L7.
**Claude (Anthropic)**: The Junior-Senior Software Engineer. This is the army of developers that do the majority the day-to-day work. This spans across the entire stack, writing scripts, building integrations, and everything from implementing APIs to mobile apps. In tech firms, it's usually the L4 or L5.

Some people have asked me how I split and assign tasks from Codex -> Gemini -> Claude. Right now, I don't have a formal process and do it manually. I don't want to over-engineer this part, so we'll see if it changes.

## My Tech Stack

- **CLI**: [iTerm 2](https://iterm2.com/) with over a decade of configs powered by the [Codex CLI](https://chatgpt.com/features/codex), [Gemini](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli), and [Claude](https://claude.com/product/claude-code).
- **Desktop Apps**: [ChatGPT](https://chatgpt.com/) as my daily partner [Google Gemini](https://gemini.google.com/) for images.
- **GitHub**: When I review code, I prefer to review it on [GitHub](https://github.com/). Aside from code review, GitHub is a suite we take for granted: Issues, Pull Requests, Code Reviews, Discussions, aGists, Workflows, Permissions, Secrets, CLI, etc...s
- **IDE**: I was a big fan of WindSurf, but switched to [Antigravity](https://antigravity.dev/). It seems that the acquisition of the founding team brough parity to the IDE.

## Reviewing Code

One of the topics that I'm not sure how it'll evolve is reviewing code.

When I was 19 years old, my manager, [Ryan Perry](https://www.linkedin.com/in/ryperry/) told me:

> "You're going to spend a lot more time reading code than writing code."

I realized this was the case when I moved into engineering leadership, but little did I know the turn it would take.

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

- For solo projects, you don't need code
- When development, don’t look at the code until it works
- The more people there are working on a codebase, the more time you should spend reviewing. Their agenda will pick up on bad patterns that you may or have not asked your agent to fix

## Modes of Operation

As with work, there's never a simple answer to **"how do you operate"** or **"how do you split your time"**?

It really depends on the state of the team, the product, the customer needs, and even external market conditions. Sometimes you wear the same single hat for an entire week, other times you might be juggling multiple hats all at once.

When it comes to software engineering with agents, I'd split it into the following modes:

- **Pairing**: Me and one agent go at it together. I spend a lot of time reading every line of output it produces and thinks through. This is when there is one large chunk of work that needs my utmost focus.
- **Orchestrating**: I'm the conductor making making the decisions. There are anywhere from 3-10 agents working on tasks of varying sizes. This is when there are a lot of little things that need to get done.
- **Gizmoducking**: Like rubber ducking but with a much more intelligent duck. This is primarily used for planning, brainstorming, ideating or building context in a new domain.

### What more do I want of agents?

### What more do I want of agents?

- See [this](https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code)

- Not seeing the bigger picure of an existing repo
- Writing useless tests
- Biasing to addition over deletion
- Not good at desining and implementing end-to-end tests
- Solving global problems
- Solving long term problems
- Solving problems that require a lot of context
- Knowing what problem to solve
- Overdoing it with interfaces
- Adding unncessary features. They're one-day nice-to-haves, but reducing the surface area of chanes, features, and code is how you prevent noise or feature creep.
- Reimplmenting things rather than reusing, refactoring or consolidating things, if not prompting.

There is a common saying:

> "You are the average of the 5 people you spend the most time with."

Extending this to agents:

> "Your agents are the average of the 5 people making the most contributions to your codebase"

## Other pro tips:

There's no going back to a world where we write code.

If I don't access to an internet connection where I can leverage the leading models from frontier labs, I use it

This blog post is going to be pretty long and mainly act as a reference of tools, tips and tricks I use for software developement.

If you're just a casual reader, the only section I recommend you don't skip is the first one

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

## Slash Commands

My most commonly used slash commands:

- I have a command for resolving merge conflicts
- I have a command for reviewing code
- I have a command for building context to prepare for code reviews
- A helper to prepare for code reviews
- A helper to clean code
- A helper to write documentation the way you want it

## Makefiles

Anyone who has ever worked with me knows how much I love my makefiles. Maybe too much.

Personally, I see it as a universal CLI if configured correctly. In any repo I work in, whenever I clone the repo, the first thing I do is run `make help` and it shows me all the commands available:

![Make targets](/images/posts/how-i-code-going-into-2026/make_targets.png)



- Make command for E2E tests that exercises everything
- You can use this in smoke tests in your CI and for your agent to make sure thngs work

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

## How will teams change?

Meta takeaways on how teams will change:

- You won’t need anyone who doesn’t have agency of their own
- But, it’s a very great sounding board. No longer do we need to use people as rubber ducks, because we have digital gizmoducks
- It’s still your job to get a picture of the product, codebase, and and user problem

Engineering leaders

- Often graduate from writing code to giving directions and making plans.
- Periodically check in
- Now that’s everyone

## Make commands

Anyone

## A handful of random pro tips:

To keep this short, I figured I'd just make a bullet point list of a bunch of micro "pro tips" I use on a day-to-day basis:

1. **Planning** - Ask the LLM to build a plan and review it.
2. **Thinking** - Tell the LLM to spend at least X minutes on a task, and not come back to you until it spent that much time deeply investigating a problem, solution or building a plan
3. **Remembering** -
4. **Logging** -
5. **Give it time** -
6.

- Some paradigms is working with humans, except you don’t have to account for their lives, emotions or energy levels
- Good code is key in some parts (critical workflows) or mature codebases with lots of people: https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code
- E.g. We spend a lot of time there on ourbackend, but less so on the frontend (for now)

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

### My favorite blogs

- Simon Willison: Ahead of everyone all the time
- Xiaw asian dude: Very real take without fluff
- Andrew Wilson (irrational exuberance): Great content, but hard to read and a little dense
- Sentry
- Founder of claude code

### TODO

My personal list of things to review after the holidays is:
