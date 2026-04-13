---
title: "Achieving your full potential, safely"
date: 2026-04-11T08:21:20-0700
draft: false
description: "How AI safety intersects with network protocols, sensor data, construction, and cryptoeconomics — and why it has to be studied empirically."
tags: ["AI Safety", "Anthropic", "Network Protocols", "Sensor Data", "Construction", "Cryptoeconomics", "Mission"]
categories: ["Thoughts"]
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Why this matters](#why-this-matters)
- [Achieving your potential requires guardrails](#achieving-your-potential-requires-guardrails)
- [Getting practical about the mission](#getting-practical-about-the-mission)
- [1. Network Protocols - How AI talks to the world](#1-network-protocols---how-ai-talks-to-the-world)
- [2. Sensor Data - How AI perceives the physical world](#2-sensor-data---how-ai-perceives-the-physical-world)
- [3. Construction - Where it all converges in a lagging industry](#3-construction---where-it-all-converges-in-a-lagging-industry)
- [4. Cryptoeconomics - What happens when you give an agent money](#4-cryptoeconomics---what-happens-when-you-give-an-agent-money)
- [Putting it all together](#putting-it-all-together)
- [Closing thoughts](#closing-thoughts)

I was recently talking to someone about the importance of AI safety in today's rapidly changing world. They asked me: _"So what's your mission? What would be on Daniel's desk Monday morning to tackle this?"_

## Why this matters

It's not a simple question, especially for someone who lives to work, with appropriate (necessary) breaks in between. My experience spans immigrating between countries with very disparate cultures, facing a handful of harsh personal realities in life, working on bleeding-edge tech that is still too early for mainstream adoption, and tackling problems in [industries that haven't changed in decades](https://a16z.com/every-building-youve-ever-been-in-was-designed-by-software-built-in-1997/).

A few years ago, before AI entered its current phase of exponential improvement, I formulated my mission in life as: _"To enable every human in achieving their full potential."_

This doesn't mean that _"anyone can do anything"_, nor does it mean that _"everyone will do everything"_. Rather, it means that each human, if they choose to, should have the opportunity and ability to achieve their full potential. They would need to bring the will, drive, and effort, but should not be limited by tools, circumstances, resources, support or other factors that are outside of their control.

For now, I'm still working on achieving my own full potential. The path to doing so enables and involves others as well. As I progress through my career and life, I anticipate that the balance will continue shifting more and more towards enabling others.

This post isn't about my mission, but rather how the recent and future advances in Artificial Intelligence play into it.

My mission hasn't changed. In fact, AI is the most powerful accelerant for this. However, it introduced a new set of risks that need to be taken into account. A lot of individuals talk about ensuring this can be done in a safe manner. The more I learn about Anthropic, their culture, and their approach, the more I am convinced that they're one of very few organizations that truly embodies this principle and is actively doing something about it.

[A recent statement from Dario Amodei](https://www.anthropic.com/news/statement-dario-amodei-american-ai-leadership) captures this as it relates to AI being a force for human progress, not peril:

> "That means making products that are genuinely useful, speaking honestly about risks and benefits, and working with anyone serious about getting this right."

The hard problem in AI safety is not _just_ abstract alignment in the lab, but learning empirically from systems that are useful enough to deploy in high-stakes physical environments. Tying this into things I've seen first hand, I believe critical but adversarial environments, like cryptoeconomics, or high-stakes real-world environments like constructions, are critical places to study emergent behavior before it reaches the real world in practice. Moving a level up from theory, the technical stack spanning APIs, RPCs, raw sensor data, and physical peripherals, can result in small failures that will compound into irreversible harm.

That means safety work can be organized by surface area and stakes: protocols first, then resources, then sensors, then actuators.

This post is my attempt to lay out what I'd focus on across multiple Mondays.

In an Anthropic like style, I'll first boil it down to a few convictions:

1. **AI communicates with the world through APIs and network protocols.** An air-gapped AI on a disconnected server is _arguably safe_, but it's also not useful, like a car that doesn't move. The protocols that connect AI to humans, to other AIs, and to external systems are where safety and utility collide. Today it's digital networking protocols, in the future it'll be biological interfaces. Both are forms of [Remote Procedure Calls (RPCs)](https://en.wikipedia.org/wiki/Remote_procedure_call) that will communicate via [Application Programming Interfaces (APIs)](https://en.wikipedia.org/wiki/API).

2. **AI perceives and acts on the physical world through sensor data.** When AI processes drone imagery to detect landslides, or navigates a car through traffic, the stakes become physical. Industries like construction, which have waited decades for a technology upgrade, are about to get one, and there are people in the industry already concerned about whether it'll be done safely.

3. **AI will have access to financial resources and economic incentives.** Give an agent money, and you enter the domain of cryptoeconomics: adversarial networks, [Byzantine Fault Tolerance](https://en.wikipedia.org/wiki/Byzantine_fault), and [Sybil Resistance](https://en.wikipedia.org/wiki/Sybil_attack). The question isn't whether AI will participate in economies, it's whether the incentive structures will be aligned.

4. **AI acts on the world through peripherals and actuators.** A model that can see but not move is limited. The moment it can trigger tools, machines, robots, or other downstream systems, the safety envelope changes again; this one builds on top of the three previous points.

## Achieving your potential requires guardrails

As humans, we have laws, social norms, self-discipline, and consequences to keep society functioning. These aren't just restrictions, they're enablers. You can drive anywhere you want, but only if you follow traffic laws. You can say almost anything, but there are different ways to say the same things, some of which are more constructive than others.

AI will need something analogous. Actions taken by AI have consequences, but on a scale that's incomparable to what any single individual can have. A human making a bad decision affects a few people. An AI making a bad decision at scale affects millions. Unfortunately, AI will also be making tradeoffs.

The balance is delicate: AI needs to be abundantly available, but with appropriate guardrails. Safe AI will be able to do anything, but should not be able to do everything. Universally available, but aligned to the individual. The issue is that everything is a tradeoff, and tradeoffs mean optimizing for upside while understanding that there are consequences. **How you do so safely is difficult to answer, but it has to be answered empirically, not theoretically.**

## Getting practical about the mission

Grandiose mission statements are easy to come up with. They're critical for guiding action, but action still needs to be taken in small, granular, incremental steps.

What follows is a slightly more tactical approach. For better or for worse, it is quite broad in its discipline. It builds on top of my prior work, interests, experience, and expertise. I have a gut feeling that the last 12 multidisciplinary years of my career have been the foundation for what's to come.

I've always liked Charlie Munger perspective of those who choose to take a multidisciplinary approach to life:

> "If you skillfully follow the multidisciplinary path, you will never wish to come back. It would be like cutting off your hands."

Multidisciplinary thinking helps engage different parts of the brain, building neural connections, surfacing a wide range of perspectives, and triggering new ideas. It's not only helpful, but it's also a fun way to live life.

Multidisciplinary also doesn't mean different topics, but also taking on different roles in different circumstances. Knowing when to step up, and when to step down. When to lead, and when to follow. When to ideate, and when to execute. It is a skill that can only be learned through trial and error.

The world changes, organizational priorities shift, urgent matters pop up from users, customers, or other inputs. Day-to-day and week-to-week priorities are always in flux. But over the span of months and years, higher order goals remain constant while the underlying details shift and adapt.

Going back to the beginning, the four sections that follow are where I'd focus my efforts across multiple Mondays.

## 1. Network Protocols - How AI talks to the world

We use natural language to communicate with AI. AI uses digital binary representations to encode and train itself. Networking protocols and their abstractions, APIs, RPCs, and the rest of the stack, are how AIs communicate with humans, between themselves, and with the external world.

As I said earlier, an air-gapped AI on a separate server is arguably safer than one connected to the internet. But it's also less useful. It's like a car that doesn't move, safe but pointless. The moment you connect it, every API endpoint becomes an attack surface, and every protocol decision becomes a trust decision.

Across Google, Twitter, Magic Leap, Waymo, and Pocket Network, the pattern was the same: APIs aren't just plumbing, they're the trust layer. When you operate a live protocol with individuals running infrastructure trying to game your system, you learn about the importance of incentives, and technical barriers that need to exist to prevent abuse.

As agentic infrastructure matures, this only intensifies. Natural language lets anyone talk to AI, but underneath, it's still APIs all the way down. There is no limit to the scope of this work, and it needs to be studied safely, because protocols are where safety and utility collide.

## 2. Sensor Data - How AI perceives the physical world

We see it with self-driving cars, drones, robots, and we already have cameras alongside every road on earth, in orbit, and in many other places. It's only a matter of time before a connected AI cluster will have access to all of it.

Processing and making decisions off of input is one thing. Having "limbs", physical or metaphorical, to act on it in the real world is another. The gap between perception and action is where some of the hardest safety problems live.

Whether it's reconstructing physical space from spatial sensors or turning noisy lidar and camera data into ground truth for autonomous vehicles, the pattern is the same: rigorous evaluation design is everything. A misclassified object isn't a bad recommendation, it can be a fatality.

As AI systems become more capable at processing sensor data, it becomes harder for humans to evaluate whether their decisions are correct. Anthropic's [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) captures this well:

> "To use an analogy, it is easy for a chess grandmaster to detect bad moves in a novice but very hard for a novice to detect bad moves in a grandmaster."

This is precisely the problem with increasingly capable AI perceiving and acting on the physical world. The better it gets, the harder it is for us to catch its mistakes, and the stakes are measured in human lives, not user metrics.

## 3. Construction - Where it all converges in a lagging industry

[This a16z post](https://www.a16z.news/p/charts-of-the-week-ventures-300b) shows how behind the construction industry is:

> "Whatever the mix of causes, construction is a $2 trillion industry that's been waiting 60 years for its technology upgrade. That's a major contributor to the housing affordability crisis – and one of the largest opportunities for robotics, prefabrication, and AI-driven construction tech to make a dent."

**AI WILL** be adopted in this industry very soon. Whether it's digital or in-person, AI will be heavily involved here in both the design and build phases, where it has to be useful, safe, and reliable. When AI analyzes drone data to identify potential landslides, it's not a chatbot making a suggestion, it's a system informing decisions about physical infrastructure where human lives are at stake.

More traditional industries, unlike software, tend to react to new technology in extremely binary ways. It's either _"not useful at all"_ or _"extremely dangerous."_ Experts dismiss it, novices fear it, and there's very little spectrum in between. Software teams adopt incrementally but quickly. They tinker, experiment, roll things out and iterate in public. Construction teams don't have that luxury. A bridge either stands or it doesn't.

Building [GetSoils](https://getsoils.com) (essentially an AirBnB for construction soil) was my first exposure to how resistant established industries are to new technology - and that was simple, harmless tech. Through [calgeo.org](https://calgeo.org) and [breakingground.tech](https://breakingground.tech), I've seen both the policy conversations and the product gaps firsthand. AI that isn't aligned to the domain won't just produce a bad user experience, it'll create havoc.

The industry is still stuck in the "summarize an email" era of AI adoption, often limited to the Microsoft suite. But the gap between where they are and where they're about to be is enormous. And this gap is exactly where Anthropic's empirical approach matters most:

> "Many of our most serious safety concerns might only arise with near-human-level systems, and it's difficult or intractable to make progress on these problems without access to such AIs."

**You can't theorize about safety in construction from a lab. You have to build and deploy to understand the risks, and do so with an organization that treats empirical study of AI behavior as a first principle.**

## 4. Cryptoeconomics - What happens when you give an agent money

Give it access to sensor data, and see what it does. Connect it with humans who make infrastructural decisions, and see how they interact. Give AI funds, and see how it behaves.

The moment an AI agent has access to financial resources, you've entered a new domain of risk. AI blackmailing humans. [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack), an AI creating thousands of fake identities to game a system. The [Byzantine General Problem](https://en.wikipedia.org/wiki/Byzantine_fault), how do you achieve consensus when some participants may be intentionally malicious, and some of those participants are AI?

The crypto ecosystem has been navigating these tradeoffs for over a decade. Fees, staking, and slashing as primitives for honest behavior; [Relay Mining](https://arxiv.org/abs/2305.10672) as a framework for ensuring quality in adversarial networks; micropayment infrastructure where the line between a legitimate transaction and an adversarial one is indistinguishable in real time. AI agents are the next participants, and the stakes are orders of magnitude higher.

Economic incentives are a powerful behavioral shaping force. When AI has access to financial resources, the incentive landscape becomes vastly more complex and dangerous. What reward functions emerge when AIs compete for resources? What exploits does an agent find when it has a wallet? What happens when multiple AI agents cooperate or defect in economic games?

These aren't hypothetical questions, they're research questions that need empirical answers.

In a [recent interview at the World Economics Forum](https://transcriptmate.com/interviews/dario-amodei/dario-amodei-on-ai-s-impact-opportunity-risk-and-societal-adaptation?utm_source=chatgpt.com), Dario said:

> "I think the most useful thing we can do is describe to the world what we're seeing and, and provide data to the world. And then, and then, you know, it's, it's left to the public in, in a democracy to, to, you know, to take that data and, and to use it and to use it to drive policy. We can't drive policy on our own."

Providing data to the world is exactly what protocols enable. The question is how to do it in a way that's transparent, reliable, and doesn't create new attack vectors.

## Putting it all together

These four areas aren't disparate, they're related problems at different layers of the stack.

An AI agent analyzing drone imagery of a construction site to assess landslide risk is using sensor data, communicating over APIs, informing decisions in an industry that reacts in binary, and soon enough transacting with economic incentives to get the job done. Every layer is a new trust boundary. Every trust boundary is a new safety question.

The progression is a widening of stakes: digital connections lead to physical perception, which leads to real industry impact, which leads to economic agency. Each layer adds complexity, each layer adds risk, and none of them can be studied in isolation from the others.

This is inherently multidisciplinary work. It requires many people, working empirically, research driven, aligned on a shared mission, at an organization that treats both usefulness and safety as non-negotiable.

## Closing thoughts

We're building the most powerful tools in human history. The question isn't whether they'll be used, it's whether the people who don't yet know they need them will be able to use them safely.

AI will help every human achieve their full potential, but only if this is done safely.

How we get there is what's likely going to be on my desk Monday morning.
