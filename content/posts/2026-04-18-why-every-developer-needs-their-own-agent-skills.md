---
title: "Why every developer needs their own agent skills"
date: 2026-04-18T22:06:46-0700
draft: false
description: "And how I code in april of 2026"
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

The great thing about recent AI development is that we're entering into a _"Show, don't tell"_ era.

**Got an idea?** Show a prototype.
**Frustrated by a bug?** Send a fix.
**Need to explain something?** Put together some materials.

It's finally possible to capture and extend the best practices and preferences of any individual to an organization.

## Agent Skills - They are actually useful

What started as sharing markdown files across teams turned into an [open standard](https://agentskills.io/home) maintained by Anthropic.

Remember finding yourself in a situation where somebody puts together a documentation explaining _"The official way to do X?"_

It never worked. The docs were often long, verbose, boring, and quickly got outdated because they were not fun to maintain. The cognitive load of reading them was too high and unenjoyable.

The exception were docs that _codified_ existing procedures and acted as required reading for onboarding. If it wasn't part of the process, it didn't happen.

Nowadays, using another person's skill is as simple as learning Kung Fu in the matrix.

![I know kung fu](/images/posts/2026-04-18-i-know-kung-fu.jpg)

## Skills Contexts - Applicable in all contexts

Skills is a one-fits-all solution that easily transfers across different contexts. Skills can be personal, repository specific, product specific, team specific or company specific. They can be closed or open source.

Sharing, explaining or teaching how you do something was either an abstract conversation or a non-trivial commitment of time. That is not the case anymore.

Skills are widespread in the software engineering community, but it's not just for developers. Anyone can share skills in any domain.

**The clearest example of this than 77.5K GitHub stars** on [Garry Tan's gstack](https://github.com/garrytan/gstack). If I do end up meeting the CEO of YCombinator one day, we'll be able to talk about things that aren't transfareable between organizations. Could be strategy, novel ideas, or life. It won't be about the cookie-cutter advice that you can get anywhere because that problem is officially solved.

The context in whcih skills are accessed also doesn't matter. Since it's just a markdown file, it can be tailored to be used on a server, a local machine, a CLI, a brwoser, a desktop app, a phone, etc...

As one concrete example for the power of using skills locally, I'll reference [DHH](http://twitter.com/dhh)'s [blog on local CI](https://world.hey.com/dhh/we-re-moving-continuous-integration-back-to-developer-machines-3ac6c611) from 2024. Putting aside all the conversations around the cost of token usage, I've spoken to friends operating organizations ranging from 50 people to 5,000 people, and everyone's CI/CD costs are going through the roof given the increase in RPs. Rather than building complex decentralized systems that coordinate, we can just download a skill that runs locally; _I'm oversimplifying but you get the point_.

## Skills Telemetry - Don't tell, just show

Rather than asking how an individual or an entity does X, we should be able to point to **github.com/{user}/agent-skills**. I adopted the pattern started by [Vercel](https://github.com/vercel-labs/agent-skills) and keep my personal skills up to date at [Olshansk/agent-skills](https://github.com/Olshansk/agent-skills).

If you want to get Sequoia's feedback on your deck, or Linus Torvalds' feedback on your code, or AirBnB's feedback on your product design, you should be able to leverage their agent skills.

The missing piece of the puzzle is the telemetry.

Marketing and vanity metrics like stars are a good start, but they don't show real usage. How many unique downloads does a skill have? How often is it being used? What is the distribution of that usage across different contexts?

There are too many "skill marketplaces" popping up, but it's only a matter of time until one becomes the canonical source of truth. It's too early to tell, but I believe Vercel is leading the charge here with [skills.sh](https://skills.sh/). I can begin seeing `npx skills add github.com/{user}/{repo}` in more places in the wild, which leverages their [CLI for the open agent ecosystem](https://github.com/vercel-labs/skills).

A couple of months ago I published [Signal vs Noise in the Skills Ecosystem](https://olshansky.info/posts/2026-02-28-signal-vs-noise-in-the-skills-ecosystem). Between February and April, the ecosystem has grown significantly:

![Before and after skills ecosystem](/images/posts/2026-04-18-before-and-after-skills-ecosystem.png)

The dashboard updates daily if you're interested in following along: [Skills.sh Ecosystem Dashboard](https://skills-dashboard.olshansky.info).

---

If you're an individual with your set of skills, publish them under an `agent-skills` repo! If you're an organization that's willing to open source your best practices, do the same. I only have a couple dozen downloads myself, but it's fun to know that someone else discovered - and is hopefully benefiting from - the skills I published; [skills.sh/?q=olshansk](https://skills.sh/?q=olshansk).

If you're curious for a few of my most recent changes in my day-to-day workflow, along with some other ideas, checkout the sections below.

Otherwise, [subscribe to my substack](https://olshansky.substack.com/) to get notified of future posts, or my [rss feed](https://olshansky.info/index.xml) for a firehouse of everything that pops into my mind.

---

## How I Code in April of 2026

1. **Forking sessions**: I've been using `/resume`, but recently learnt about `/rewind` and `/fork` to take a single conversation in different direction. Not all agent CLIs have feature parity here, but it's just a matter of time.
2. **GitHub Comments**: Leave comments on GitHub -> Tell the agent using the `gh` CLI to pull all the comments and tend to them -> Rinse & repeat. Same as a human workflow, but you can be more verbose and direct since agents won't take it personally.
3. **Less is more**: I went through a phase of kicking off an agent for every idea, but reverted back to a more focused approach. I've found that reading, reviewing and working with the agents on one task at a time is more productive than trying to do everything at once. It also creates an opportunity to improve the quality of any skills I used during the work session.
4. **Preffered agents**: Gemini searchers. Codex plans and reviews. Claude implements. There's a lot of nuance here that I'm not writing out, but I believe it has to do with the culture that each frontier lab brings into its models. I might write a full post on some of the details here, but wouldn't be surprised if everything changes, _again_ by the time that I do.
5. **Terminal**: I've moved from [iTerm2](https://iterm2.com/) to [ghostty](https://github.com/ghostty/ghostty). The performance comparison is night and day.
6. **Deep Breaths**: I've started noticing how much shallow breathing I do when I work with agents. Two deep breaths have become a game changer for me.
7. **Naming is important**: Naming and documentating TODOs is more important than tever. No matter how intelligent AI becomes, it still needs context. No matter how much context it can search or take in, it'll be a cost and latency tradeofs. There's no reason we shouldn't help agents be efficient and productive through proper naming and documenting TODOs or techdebt along the way. What I wrote in [Move Fast and Document Things](https://olshansky.substack.com/p/move-fast-and-document-things) is more true than ever.

Do you remember the infamous programmer joke from [Leon Bambrick](https://x.com/secretGeek/status/7269997868) in 2010?

> "There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors."

My 2026 agent-era follow-up joke is:

> Agents have helped us solve off-by-1 errors. Unfortunately, we replaced them with AI slop. Two hard problems remain.

### How I Think Coding will Evolve in April of 2026

A lot of engineering effort is going into democrazigin and scaling the usage of skills. I persnoally believe that a large, orthogonal, opportunity lies in understanding cognitive human behaviour to compound on that effort.

1. **Gamification of verification**: I published [a thought on this idea](https://olshansky.info/thoughts/2026-04-08-gamification-of-verification) that I can't let go of. The act of generation is rewarding. The act of verification is not. Writing code was always "the fun part" delegated to more junior engineers, while the act of verification was a chore delegated to more senior engineers. We'll need to find a way to make the process of QA and verification as fun as engaging as generation was for things to be sustainable. I don't know what this experience or modality will look like yet, but it'll take shape over time.
2. **Interactive skills**: Online surveys and questionaires are more tolerable when there's just a few questions per page. The same thing applies to reviewing the output of agentic CLIs. I've started making some (not yet public) skills that interact with the human step-by-step to make it easy and engaging. It's beginning to feel like old-school CLI games rather than work. I believe there's a big opportunity here.
3. **Semi-automated skills**: Extending the point above is the idea of semi-automation. Automating something 100% is hard, and often unnecessary. [Elon Musk's](https://www.corporate-rebels.com/blog/musks-algorithm-to-cut-bureaucracy) 5-step algorithm involves automation only when `"all the requirements had been questioned, parts and processes deleted, and the bugs were shaken out".` I agree, but with skills we can get 90% of the benefit with 10% of the effort, by keeping the human-in-the-loop.

> "Automation comes last. The big mistake in [my factories] was that I began by trying to automate every step. We should have waited until all the requirements had been questioned, parts and processes deleted, and the bugs were shaken out."

- Elon Musk
