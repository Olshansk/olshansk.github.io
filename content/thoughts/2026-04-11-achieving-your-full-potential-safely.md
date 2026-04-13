---
title: "Achieving your full potential, safely"
date: 2026-04-11T08:21:20-0700
draft: false
description: ""
tags: []
categories: ["Thoughts"]
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

I was recently asked: _"What's on Daniel Olshansky's desk Monday Morning?"_

It's not a simple question, especially for someone who lives to work, with appropriate breaks in between.

In essence, it's a different way of asking _"What do you want to do with your life?"_

A few years ago, before AI entered its current phase of exponential improvement, I formulated my mission in life as: _"To enable every human to achieve their full potential."_

This doesn't mean that _"anyone can do anything"_, nor does it mean that _"everyone will do everything"_. Rather, it means that each human, if they choose to, should have the opportunity and ability to achieve their full potential. They would need to bring the will, drive, and effort, but should not be limited by tools, circumstances, resources, support or factors that are outside of their control.

For now, I'm still working on achieving my own full potential. The path to doing so enables and involves others as well. As I progress through my career and life, I anticipate that the balance will continue shifting more and more towards enabling others.

This post isn't about my mission, but rather how the recent and future advances in Artificial Intelligence play into it.

My mission hasn't changed. In fact, AI is the most powerful accelerant for this. However, it introduced a new set of risks that need to be taken into account. A lot of individuals talk about ensuring this can be done in a safe manner. The more I learn about Anthropic, their culture, and their approach, the more I realize that they're the only organization that embodies this and is actively doing something about it.

Anthropic's [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) captures a principle I keep coming back to:

> "That means making products that are genuinely useful, speaking honestly about risks and benefits, and working with anyone serious about getting this right."

The rest of this post is my attempt to answer _"what's on my desk"_ concretely. It boils down to three convictions:

1. **AI communicates with the world through APIs and network protocols.** An air-gapped AI on a disconnected server is arguably safe, but it's also useless — like a car that doesn't move. The protocols that connect AI to humans, to other AIs, and to external systems are where safety and utility collide. This is where I've spent most of my career.

2. **AI perceives and acts on the physical world through sensor data.** When AI processes drone imagery to detect landslides, or navigates a car through traffic, the stakes become physical. Industries like construction, which have waited decades for a technology upgrade, are about to get one — the question is whether it'll be done safely.

3. **AI will have access to financial resources and economic incentives.** Give an agent money, and you enter the domain of cryptoeconomics: adversarial networks, Byzantine fault tolerance, and sybil resistance. The question isn't whether AI will participate in economies — it's whether the incentive structures will be aligned.

## Achieving your potential requires guardrails

As humans, we have laws, social norms, self-discipline, and consequences to keep society functioning. These aren't just restrictions — they're enablers. You can drive anywhere you want, but only if you follow traffic laws. You can say almost anything, but social norms help you keep your friends.

AI will need something analogous. Actions taken by AI have consequences, but on a scale that's incomparable to what any single individual can have. A human making a bad decision affects a few people. An AI making a bad decision at scale affects millions.

The balance is delicate: AI needs to be abundantly available, but with appropriate guardrails. Safe AI needs to be able to do anything, but not everything. Universally available, but aligned to the individual. The issue is that everything is a tradeoff, and tradeoffs mean optimizing for upside while understanding that there are consequences. How you do so safely is difficult to answer — but it has to be answered empirically, not theoretically.

## Getting practical about the mission

Grandiose mission statements are easy to come up with. They're critical for guiding action, but action still needs to be taken in small, granular, incremental steps.

What follows is a slightly more tactical approach to what I'd want on my desk. For better or for worse, it is quite broad in its discipline. It builds on top of my prior work, interests, experience, and expertise.

Charlie Munger captures the rationale behind the multidisciplinary "ADD" I, and some other founders, have:

> "If you skillfully follow the multidisciplinary path, you will never wish to come back. It would be like cutting off your hands."

Multidisciplinary thinking helps engage different parts of the brain, building neural connections, surfacing a wide range of perspectives, and triggering new ideas. It's not only helpful, but it's also a fun way to live life.

What's on my desk on Monday? I genuinely don't know, because every week is dynamic. The world changes, organizational priorities shift, urgent matters pop up from users, customers, or other inputs. However, over the span of months or years, higher order efforts remain constant while the underlying details shift and adapt. I can tell you what I'd like to achieve over the course of several years — and the four sections that follow are where I'd focus that effort.

## Network Protocols — How AI talks to the world

We use natural language to communicate with AI. AI uses digital binary representations to encode and train itself. But networking protocols and their abstractions — APIs, RPCs, and the rest of the stack — are how AIs communicate with humans, between themselves, and with the external world.

An air-gapped AI on a separate server is arguably safer than one connected to the internet. But it's also less useful. It's like a car that doesn't move — safe, but pointless. The moment you connect it, every API endpoint becomes an attack surface, and every protocol decision becomes a trust decision.

This is where I've spent most of my career. At Google, I worked with protobufs and gRPC. At Twitter, it was the API platform. At Magic Leap, we built the first version of a digital twin of the real world in the cloud — my title was literally "Augmented Reality Cloud API Engineer." At Waymo, APIs were the common language across organizations. At Pocket Network, our vision was a permissionless API marketplace, and we spent years ensuring and evaluating API quality in a distributed, adversarial environment driven by economic incentives.

As agentic infrastructure matures, I believe APIs will play a critical role in how the digital economy operates. LLMs have enabled anyone to interface with AI, but this is an abstraction layer atop APIs, in the same way that APIs are an abstraction layer of the networking stack. There is no limit to the scope of this work — and it needs to be done safely, because protocols are where safety and utility meet head on.

In a [recent interview at the World Economics Forum](https://transcriptmate.com/interviews/dario-amodei/dario-amodei-on-ai-s-impact-opportunity-risk-and-societal-adaptation?utm_source=chatgpt.com), Dario said:

> "I think the most useful thing we can do is describe to the world what we're seeing and, and provide data to the world. And then, and then, you know, it's, it's left to the public in, in a democracy to, to, you know, to take that data and, and to use it and to use it to drive policy. We can't drive policy on our own."

Providing data to the world is exactly what protocols enable. The question is how to do it in a way that's transparent, reliable, and doesn't create new attack vectors.

## Sensor Data — How AI perceives the physical world

We see it with self-driving cars, drones, robots, and we already have cameras alongside every road on earth, in orbit, and in many other places. It's only a matter of time before a connected AI cluster will have access to all of it.

Processing and making decisions off of input is one thing. Having "limbs" — physical or metaphorical — to act on it in the real world is another. The gap between perception and action is where some of the hardest safety problems live.

During my time at Magic Leap and Waymo, I spent years working on systems that ingest and process raw sensor data. Spatial sensors, lidar, camera, radar — building reliable pipelines to turn noisy signals into ground truth. At Waymo, rigorous evaluation design was everything. A misclassified object isn't a bad recommendation — it's a potential fatality.

As AI systems become more capable at processing sensor data, it becomes harder for humans to evaluate whether their decisions are correct. Anthropic's [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) captures this well:

> "To use an analogy, it is easy for a chess grandmaster to detect bad moves in a novice but very hard for a novice to detect bad moves in a grandmaster."

This is precisely the problem with increasingly capable AI perceiving and acting on the physical world. The better it gets, the harder it is for us to catch its mistakes — and the stakes are measured in human lives, not user metrics.

## Construction — Where it all converges in a lagging industry

[This a16z post](https://www.a16z.news/p/charts-of-the-week-ventures-300b) shows how behind the construction industry is:

> "Whatever the mix of causes, construction is a $2 trillion industry that's been waiting 60 years for its technology upgrade. That's a major contributor to the housing affordability crisis – and one of the largest opportunities for robotics, prefabrication, and AI-driven construction tech to make a dent."

AI WILL be adopted in this industry very soon. Whether it's digital or in-person, AI will be heavily involved here and it has to be safe and reliable. When AI analyzes drone data to identify potential landslides, it's not a chatbot making a suggestion — it's a system informing decisions about physical infrastructure where human lives are at stake.

I engage with this directly. At [calgeo.org](https://calgeo.org), I help set AI policy for the geotechnical engineering community in California. They're worried about safety and policy — rightfully so. At [breakingground.tech](https://breakingground.tech), I'm building products for the industry. I fine-tuned a geotechnical model that outperformed general-purpose models on domain-specific tasks out of the box. But more than the model itself, it unlocked conversations where I can see how big the problem and opportunity is.

The industry is still stuck in the "summarize an email" era of AI adoption, often limited to the Microsoft suite. But the gap between where they are and where they're about to be is enormous. And this gap is exactly where Anthropic's empirical approach matters most:

> "Many of our most serious safety concerns might only arise with near-human-level systems, and it's difficult or intractable to make progress on these problems without access to such AIs."

You can't theorize about safety in construction from a lab. You have to build and deploy to understand the risks — and do so with an organization that treats empirical study of AI behavior as a first principle.

## Cryptoeconomics — What happens when you give an agent money

Give AI funds, and see what it does. Give it access to sensor data, and see what it does. Connect it with humans who make infrastructural decisions, and see how they interact.

The moment an AI agent has access to financial resources, you've entered a new domain of risk. AI blackmailing humans. [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack) — an AI creating thousands of fake identities to game a system. The [Byzantine General Problem](https://en.wikipedia.org/wiki/Byzantine_fault) — how do you achieve consensus when some participants may be malicious, and some of those participants are AI?

I've spent years building in this exact environment. At Pocket Network, we designed protocols that leverage economic incentives in adversarial networks — fees, staking, and slashing as primitives for honest behavior. We published a paper on [Relay Mining](https://arxiv.org/abs/2305.09315) and spent a lot of time ensuring API quality in a permissionless, distributed, adversarial environment. At Grove, we're building micropayment infrastructure where agents and humans transact.

Economic incentives are the most powerful behavioral shaping force we know. When AI has access to financial resources, the incentive landscape becomes vastly more complex and dangerous. What reward functions emerge when AIs compete for resources? What exploits does an agent find when it has a wallet? What happens when multiple AI agents cooperate or defect in economic games?

These aren't hypothetical questions — they're research questions that need empirical answers. Studying how AI behaves in adversarial economic environments is a natural extension of alignment research, and it's where my experience maps most directly to what I believe Anthropic will need to study.

## Putting it all together

All of the above may seem like disparate, independent topics. In reality, they're components of a greater whole — the full picture of how AI will interact with the real world.

AI will communicate over the internet using APIs and protocols. It will perceive the world through cameras, lidar, and drones. It will make decisions about physical infrastructure in industries like construction. And it will have economic agency through access to financial systems.

The progression isn't arbitrary — it's a widening of stakes. Digital connections lead to physical perception, which leads to real industry impact, which leads to economic agency. Each layer adds complexity, and each layer adds risk.

Each of these needs to be built, tested, studied, understood, and decomposed in isolation. A problem always needs to be broken down into primitive components and then reassembled to solve it holistically. This isn't just a multidisciplinary approach — it requires many people, working empirically, at an organization that takes both usefulness and safety seriously.

## Closing thoughts

Anthropic is the modern-day Bell Labs.

What Bell Labs did for communication, Anthropic is doing for intelligence. Both need to be useful, and both can be used unsafely. Bell Labs didn't just invent the transistor and the laser — they studied, standardized, and made communication work reliably for everyone. They built products, they did research, and they shaped policy. That's the kind of organization where multidisciplinary work isn't a nice-to-have — it's the only way the mission gets done.

The question on my desk Monday morning is the same one that'll be there in a year, and in a decade: _How do I help every human achieve their full potential, safely?_

I don't have a Monday answer. I have a career-long one. And I believe Anthropic is where I can do my best work pursuing it.
