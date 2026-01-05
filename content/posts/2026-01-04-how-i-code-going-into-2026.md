---
title: "How I code going into 2026"
date: 2026-01-04T09:08:01-0500
draft: true
description: "RIP 22 years of writing code by hand"
tags: []
categories: ["Posts"]
medium_url: ""
substack_url: ""
ShowToc: false
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

## My First Lines of Code <!-- omit in toc -->

At the age of 11 in 2003, I wrote my first line of code. I was a Game Master for a DragonBall Z MMORPG on [byond.com](https://www.byond.com/). Other than creating a cool-looking pixel art item, I do not remember the language or many of the details.

At the age of 14 in 2007, I had to take a programming course as part of my high school’s [Math and Computer Science (MaCS)](https://schoolweb.tdsb.on.ca/wlmac/MaCS-Program) curriculum. We used a language called [Turing](<https://en.wikipedia.org/wiki/Turing_(programming_language)>), which is likely unknown to many.

At the age of 16 in 2009, I took the Advanced Placement (AP) Computer Science course after spending a full year coding in Java.

From there, I wrote code in a wide range of languages across academic and professional settings: Prolog, JavaScript, Objective-C, C++, Erlang, Elixir, Swift, Python, Go, and a few others that do not immediately come to mind. This spanned roles including iOS development at ModiFace, Android at Google, full stack at Twitter, backend ML infrastructure at Magic Leap, AI eval at Waymo, and blockchain R&D at Pocket Network.

It has been about six months since I manually wrote a line of code. It is hard to believe I may never write code by hand again. If I do not have access to the internet and leading frontier models, I simply will not be writing code.

Some people struggle with this transition. I do not find it bittersweet. From my perspective, we can finally focus on what matters: product and engineering.

## Table of Contents <!-- omit in toc -->

- [How I code going into 2026](#how-i-code-going-into-2026)
- [Orchestrating Agent Personalities](#orchestrating-agent-personalities)
- [My Tech Stack](#my-tech-stack)
- [Reviewing Code](#reviewing-code)
- [Modes of Operation](#modes-of-operation)
- [AI Driven Software Engineering](#ai-driven-software-engineering)
- [Use TODOs to Move Fast TODO Everything](#use-todos-to-move-fast-todo-everything)
- [Makefiles](#makefiles)
- [Skills Feedback Loop](#skills-feedback-loop)
- [Documentation](#documentation)
- [How will teams change?](#how-will-teams-change)
- [A handful of random pro tips:](#a-handful-of-random-pro-tips)
- [My favorite blogs](#my-favorite-blogs)
- [Personal Followups](#personal-followups)

## How I code going into 2026

I wanted to capture how I do software engineering going into 2026. Partly to share my workflow, and partly to have something to reflect on in the future.

Prior to our pivot at [Grove](https://grove.city/) in October 2025, I had five senior engineers on my team. It is worth mentioning that I and the rest of the C-suite are fully hands-on across the entire stack.

Today, a pyramid of agents reports to me:

![Agent Directory](/images/posts/how-i-code-going-into-2026/agent_pyramid.jpeg)

I no longer write code by hand from scratch at all.

I will dive into tips and patterns, but four Claudes, two Geminis, and one Codex via the CLI capture the majority of how I operate day to day.

## Orchestrating Agent Personalities

Managing agents is not just about direction or automation. It is about orchestration.

In a symphony, the conductor makes the decisions, but the musicians do the work. No matter how skilled they are, they follow the conductor’s direction.

I do not believe this part will ever be automated away. It is the irreplaceable piece people now refer to as taste.

A big part of orchestration is understanding strengths, weaknesses, and personalities. This is no different from working with humans, except agents do not get tired and are unencumbered by emotion.

I have noticed that the personality and capabilities of each agent reflect the organizations that built them.

**Codex (OpenAI)**: The manager or director type. Strong at planning, scaffolding, and setting direction. Roughly an L8+ profile.

**Gemini (Google)**: The architect or principal engineer. Strong at solving hard problems, from AI implementation to low-level optimization. Good at design docs, complex bug fixing, security issues, and refactor planning. Typically L6 or L7.

**Claude (Anthropic)**: The junior-to-senior engineer workhorse. This is the army that does most day-to-day execution across the stack, from scripts and integrations to APIs and mobile apps. Typically L4 or L5.

People often ask how I split tasks across Codex, Gemini, and Claude. I do it manually. I am intentionally avoiding over-engineering this part for now.

_Side note: CLI UX ranking from best to worst is Gemini, then Claude, then Codex. This may be the only time Google wins on product, and it is because the target user is a developer._

## My Tech Stack

- **CLI**: [iTerm2](https://iterm2.com/) with over a decade of configs, powered by the Codex CLI, Gemini CLI, and Claude Code.
- **Desktop Apps**: ChatGPT as my daily partner, Google Gemini primarily for images.
- **GitHub**: I strongly prefer reviewing code on GitHub. Beyond code review, it is an underrated suite: issues, pull requests, discussions, gists, workflows, permissions, secrets, and the CLI.
- **IDE**: I was a big fan of Windsurf, but switched to [Antigravity](https://antigravity.dev/). The acquisition of the founding team seems to have brought parity.

## Reviewing Code

One topic I am unsure how will evolve is code review.

When I was 19, my manager Ryan Perry told me:

> "You're going to spend a lot more time reading code than writing code."

That became obvious in engineering leadership. I did not anticipate how extreme it would become.

For solo projects, I neither write code by hand nor review it unless there is a serious issue.

For shared codebases, it depends on business criticality and maturity.

There is a saying:

> "You are the average of the five people you spend the most time with."

Applied to agents:

> "Your agents are the average of the five contributors making the most changes to your codebase."

Agents behave exactly as carefully as you teach them to. The closer code is to critical paths, such as payments or core business logic, the more I review it.

For fast-moving frontend code, I often skip review entirely and ask another agent to ensure it is idiomatic, clean, and good enough.

## Modes of Operation

There is never a single answer to how you operate or how you split your time.

It depends on team state, product maturity, customer needs, and market conditions. Sometimes you wear one hat all week. Other times, many at once.

With agents, I operate in a few distinct modes:

- **Pairing**: One agent and me. I read everything line by line. This is for high-focus, high-stakes work.
- **Orchestrating**: I act as the conductor. Three to ten agents work in parallel on tasks of varying size.
- **Gizmoducking**: Like rubber ducking, but the duck is much smarter. Used for planning, brainstorming, and building domain context.

## AI Driven Software Engineering

We keep inventing new terms.

Prompt engineering. Vibe coding. Context engineering. More will follow.

Previously, we had coding, programming, software engineering, architecture, and everything in between.

At the end of the day, the goal is a product people love and pay for. Everything else is just a means to that end.

That is why I call this **AI Driven Software Engineering**.

## Use TODOs to Move Fast TODO Everything

I previously wrote [Move Fast and Document Things](https://olshansky.substack.com/p/move-fast-and-document-things).

The core idea is simple: capture side thoughts without derailing execution.

- No implementation required
- No issue or doc creation
- No broadcast to the team
- Just add `TODO_<REASON>: <description>` in the code

This makes context sharing trivial. You get it out of your head, share intent, and leave breadcrumbs for later.

## Makefiles

Anyone who has worked with me knows I love Makefiles. Possibly too much.

I treat them as a universal CLI. In every repo, the first thing I run is `make help`.

![Make targets](/images/posts/how-i-code-going-into-2026/make_targets.png)

They are useful beyond humans:

- **Onboarding**: New contributors can run `make help` and start building immediately.
- **Agents**: I instruct agents to run make targets, iterate, and test until conditions are met. I also ask them to create new targets.
- **Smoke tests**: The same targets can drive end-to-end infrastructure checks.

My bet is that Makefiles are due for a comeback.

## Skills Feedback Loop

I keep my Gemini, Claude, and Codex prompts in a public [prompts repo](https://github.com/Olshansk/prompts).

The most mature skill is my [Makefile skill](https://github.com/Olshansk/prompts/tree/main/claude/skills/makefile), with templates for different project types. Another favorite is my [code review prepare](https://github.com/Olshansk/prompts/blob/main/claude/commands/cmd_code_review_prepare.md) prompt.

The key idea: prompts and skills are living artifacts.

They require continuous maintenance, just like docs, scripts, and internal tools. The difference is you can and should ask your agent to improve them at the end of every session.

## Documentation

Anyone who has worked with me knows I am relentless about documentation.

I am equally relentless when reviewing docs written by agents.

Nobody wants to read. Everyone wants copy-paste.

My documentation rules are simple:

- Short sentences or bullets
- Copy-paste friendly commands
- Low cognitive overhead
- No filler
- Start with a quickstart
- Bias toward section headers

## How will teams change?

This deserves a longer piece, so I will keep it brief.

The gap between product managers and engineers will shrink. Product managers who cannot prototype will struggle. Engineers without product taste will struggle.

Engineering leaders will be hands-on to varying degrees.

Best practices will shift from how to write code to how to improve agents.

## A handful of random pro tips:

A grab bag of things I do daily:

1. **Planning**: Ask the model to produce a plan, then review it.
2. **Thinking**: Tell the model to spend at least X minutes deeply investigating before responding.
3. **Compounding**: When you find a gap, ask the agent to update its memory, skill, or command.
4. **Logging**: Logs matter more now. I use emojis, colors, and rich metadata.
5. **Take your time**: Explicitly tell agents to slow down for complex tasks.
6. **Be idiomatic**: Teach patterns intentionally. Reinforcement compounds.
7. **Simplify**: Ask agents to reduce branching, surface area, and over-engineering.
8. **Resuming**: Use resume mode in agent CLIs.
9. **Yoloing**: I use Arq backups and embrace `--yolo`.
10. **Feedback**: Ask agents where you are wrong or what you are overlooking.

## My favorite blogs

- [Simon Willison](https://simonwillison.net/): Founder of Django and a leading independent AI researcher.
- [Will Larson](https://andrew.wilson.io/): Excellent content, dense but worth the effort.
- [xuanwo](https://xuanwo.io/): Direct and fluff-free.
- [cra.mr](https://cra.mr/): Founder of Sentry.
- [Boris Cherny](https://x.com/bcherny): Creator of Claude Code.
- [Andrej Karpathy](https://x.com/karpathy): Clear explanations of how LLMs work.

## Personal Followups

Personal TODOs after the holidays:

- Boris Cherny’s thread on Claude Code
- https://xuanwo.io/2025/09-2025-review/
- Experiment with orchestration tools like conductor
- Improve shared `CLAUDE.md` patterns
- Reduce large copy-paste blocks
- Invest time in CLI hotkey muscle memory
