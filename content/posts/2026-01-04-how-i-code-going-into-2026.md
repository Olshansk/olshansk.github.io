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

At the age of 11 in 2003, I wrote my first line of code. I was a Game Master for DragonBall Z MMORPG on [byond.com](https://www.byond.com/). Other than creating a cool looking pixel art item, I don't remember the language it was in or any of the details.

At the age of 14 in 2007, I had to take a programming course as part of my highschool's [Math and Computer Sciences (MaCS)](https://schoolweb.tdsb.on.ca/wlmac/MaCS-Program) curriculum. We used a language called [Turing](<https://en.wikipedia.org/wiki/Turing_(programming_language)>) that is likely unknown to manny.

At the age of 16 in 2009, I took the Advanced Placement (AP) Computer Science course after spending a whole year coding in Java.

From there, I had experience writing code in a variety of languages spanning both academic and professional settings: Prolog, JavaScript, Objective-C, C++, Erlang, Elixir, Swift, Python, Go, and probably a few others that don't pop to mind right away. This spanned roles including iOS development at ModiFace, Android at Google, Full Stack At Twitter, backend ML infrastructure at Magic Leap, AI eval at Waymo, Blockchain R&D at Pocket Network, etc...

It's been about 6 months since I have manually written a line of code, and it's hard to believe that I may never write a line of code by hand again. If I don't have access to an internet connection where I can leverage the leading models from frontier labs, I won't be writing code.

Some are struggling with the transition, but I don't find it bittersweet. From my perspective, we can finally just focus on what matters: product & engineering.

## Table of Contents <!-- omit in toc -->

- [How I code going into 2026](#how-i-code-going-into-2026)
- [Orchestrating Agent Personalitites](#orchestrating-agent-personalitites)
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

_Side note: I'd rank the CLI UX from best to worst as follows: Gemini -> Claude -> Codex. This might be the only time Google is superior on a product front, and it's only because the target customer is a developer._

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

For solo projects, I don't write any code by hand, nor do I review any of it unless there's a serious issue.

For shared codebases, it really depends on how critical the business logic is and the maturity of the codebase.

There's a common saying:

> "You are the average of the 5 people you spend the most time with."

Extending this to agents:

> "Your agents are the average of the 5 people making the most contributions to your codebase."

Very simply put, the amount of effort that an eng team will put into asking agents to set or follow patterns across docs, tools, interfaces, etc, is exactly how the agent will behave. This is where code reviewing agent work requires a very delicate balance.

The closer the work is to critical code paths, such as updating database rows related to payments, the more I review it. If it's your businesse's moat, you'll likely need

If the code is realted to some frontend chaanges that are always moving, I don't review it at all, but ask another agent to ensure it's idiomatic, clean, and good enough.

## Modes of Operation

As with work, there's never a simple answer to **"how do you operate"** or **"how do you split your time"**?

It really depends on the state of the team, the product, the customer needs, and even external market conditions. Sometimes you wear the same single hat for an entire week, other times you might be juggling multiple hats all at once.

When it comes to software engineering with agents, I'd split it into the following modes:

- **Pairing**: Me and one agent go at it together. I spend a lot of time reading every line of output it produces and thinks through. This is when there is one large chunk of work that needs my utmost focus.
- **Orchestrating**: I'm the conductor making making the decisions. There are anywhere from 3-10 agents working on tasks of varying sizes. This is when there are a lot of little things that need to get done.
- **Gizmoducking**: Like rubber ducking but with a much more intelligent duck. This is primarily used for planning, brainstorming, ideating or building context in a new domain.

## AI Driven Software Engineering

Feels like we have a new term for coding these days.

We've moved from **Prompt Engineering**, to **Vibe Coding**, to **Context Engineering**, and who knows what's next.

Previously, we had everything from Coding, to Programming, to Software Engineering, Architecture and everything in between.

At the end of the end, the goal is a product people love and are willing to pay for. Everything in between is just a means to an end.

That's why I like to call it **AI Driven Software Engineering**.

## Use TODOs to Move Fast TODO Everything

A little while ago I published a blog post titled [Move Fast and Document Things](https://olshansky.substack.com/p/move-fast-and-document-things).

It's a simple tool that enables engineers to stay focused without tending to side quests, while getting the satisfcation of getting something of their mind:

- It doesn't involved implenenting the side quest
- It doesn't involve creating an issue or a document for it
- It doesn't involve sharing it with everyone
- It simply involves adding a `TODO_<REASON>`: <description>` in the codebase.

It makes sharing and picking up context really easy. You get the dopamine relief of getting it off your mind. You get to share youe thoughts, learnings and ideas with other engineers.

## Makefiles

Anyone who has ever worked with me knows how much I love my makefiles. Maybe too much.

Personally, I see it as a universal CLI if configured correctly. In any repo I work in, whenever I clone the repo, the first thing I do is run `make help` and it shows me all the commands available:

![Make targets](/images/posts/how-i-code-going-into-2026/make_targets.png)

It's a lot more powerful than just helping us humans.

- **Quick onboarding** - Rather than reading a README, anyone new to the codebase can run `make help` to get started and avoid needing to learn anything, just get into building.
- **Agents**: I can instruct agents to run certain make targets to run things, test things, and iterate until a certain E2E test passes. I can also instruct them to create new targets so I don't have to remember complex commands or configurations
- **Smoke Tests** - I can reuse the targets for end-to-end smoke tests in our infrastructure.

My personal bet is that Makefiles are going to make a comeback. Let's see how that evolves.

## Skills Feedback Loop

I keep my Gemini, Claude and Codex prompts and skills in a public [prompts repo](https://github.com/Olshansk/prompts)

The only mature skill I have right now is for my [Makefiles](https://github.com/Olshansk/prompts/tree/main/claude/skills/makefile), with templates for different types of projects. I also have a handful of others that I use regularly. One of my favorite ones is the [code review prepare](https://github.com/Olshansk/prompts/blob/main/claude/commands/cmd_code_review_prepare.md) prompt.

The most important piece here: **prompts and skills are not once and done, they're something you maintain on a day-to-day basis**.

Documentation, scripts, tools and best practices at any organization must be updated on a daily basis. Tehse are not any different.

The only difference is that you could, **and should**, ask your agent to improve them at the end of every session.

You can either tell it how to improve the script in detail, or use the contents of your conversation for that direction.

## Documentation

Anyone who has ever worked with me know how much of a 🥙 I am when it comes to documentation.

I'm equally as much a PITA (Pain In The Ass) when Ir eview documentation from agents.

No one wants to read, and everyone just wants to copy-pasta (📠-🍝).

Very simply, any documentation I ask AI to write involves:

- Short sentences or bullet points
- Copy-pasta friendly commands
- Reduce cognitive overhead for agent and human readers
- No filler or fluff
- Start with a quickstart and only dive into "how" related details at the end
- Bias to section headers when possible.

## How will teams change?

This is a bigger topic. It requires a much bigger discussion so I'll keep it short.

The divergence between prodcut managers and software engineers will grow smaller. You won't need product managers who cannot build prototypes on their own, and you don't need software engineers who do not have product taste. You'll still need domain experts in both.

All engineering leaders and managers will be hands on to varying degrees.

Best practices in engineering orgs will evolve from best practices of how to write code, to best practices of how to improve their agents.

## A handful of random pro tips:

To keep this short, I figured I'd just make a bullet point list of a bunch of micro "pro tips" I use on a day-to-day basis:

1. **Planning** - Ask the LLM to build a plan and review it.
2. **Thinking** - Tell the LLM to spend at least X minutes on a task, and not come back to you until it spent that much time deeply investigating a problem, solution or building a plan.
3. **Remembering and compounding** - Whenever you have a long back-and-forth with an agent and you identify one of its gaps, ask it to either update its agents.md file, or update/create a new skill or slash command you can reuse. Small changes every day compound very quickly.
4. **Logging** - Now that we don't have to write logs anymore, logs are so much more important because that's your windo into what's happening. I've fully longs log lines with emojis, colors and all the metadata.
5. **Take your time** - When you know you're giving the agent a complex task, tell it to take it its, or to spend "At least X minutes" working on something before returning to you.
6. **Be idiomatic** - Periodically tell CLAUDE to remember patterns. E.g. I really like emojis and colors in my log lines, so I build patterns along the way. "Teaching it" to your team is as simple as #memorize
7. **Simplify** - A simple note asking the agent to put effort into avoidign code branching, reduce the code surface area, and over-engineering and keeping things Elon-like simple goes a surpinsingly long way.
8. **Resuming** - Every agent CLI has a `resume` option to pick up conversations where you left off. Use it.
9. **Yoloing** - I bought a license to [Arq](https://www.arqbackup.com/) backup and have embraced [`--yolo`](https://developers.openai.com/codex/cli/reference/) mode.
10. **Ask for feedback** - Giving the agent permission to tell you what your blind spots are can be very helpfu. Ask it things like `tell me why I'm wrong` or `what am I overlooking`.

## My favorite blogs

- [Simon Willison](https://simonwillison.net/): Founder of Django and leading independent researcher on AI. He coined things like [The Lethal Trifecta For AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), [Prompt Injection](https://simonwillison.net/series/prompt-injection/), the [Pelican on a bycicle](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/) LLM benchmark, and so much more. He's been blogging for decades and you should [support him](https://github.com/sponsors/simonw/) if you read his stufff.
- [Will Larson](https://andrew.wilson.io/): Great content, but hard to read and a little dense
- [xuanwo asian dude](https://xuanwo.io/): Very real take without fluff
- [cra.mr](https://cra.mr/): founder of sentry
- [Boris Cherny](https://x.com/bcherny): Creator of Claude Code.
- [Andrej Karpahy](https://x.com/karpathy): The leading voice on explaining how LLMs work. Founder @EurekaLabsAI, ex-director of AI at Tesla, co-founder at OpenAI.

## Personal Followups

These are a few of my personal TODOs to go through after the holidays:

- [Boris Cherny's Thread on X](https://x.com/bcherny/status/2007179832300581177) on how to use Claude Code
- https://xuanwo.io/2025/09-2025-review/
- Play around with orchestration tools like [conductor](https://www.conductor.build/) to spawn multiple agents at once.
- [The "definitive" guide on how to use Claude Code](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
- Think through ways of how to make `CLAUDE.md` better in shared codebases
- Think through ways of how to do less copy-pasting of large chunks of text
- Spending a bit of time on the hotkeys (e.g. switching plan mode on/off) has been useful, but I haven't developed the muscle memory for it yet.
