+++
author = "Daniel Olshansky"
title = "5P;1R Decentralized AI: Permissionless LLM Inference on POKT Network"
date = "2024-06-22T04:17:26.863Z"
description = "You don’t always need NVIDIA GPUs for inference"
tags = [
    "crypto", "ai", "nuclear", "research", "productivity", "book"
]
substack_url = "https://olshansky.substack.com/p/5p1r-decentralized-ai-permissionless"
+++

_This is part of a series called "5 points & 1 resource" (think tl;dr but 5p;1r). I summarize 5 key concepts that would have helped me learn, relearn, or refresh my knowledge of a topic or paper._

_Today, I’m reviewing a paper I contributed to myself so I added a personal forward :)_

---

- [The real value prop of a permissionless inference network](https://olshansky.substack.com/i/144980765/the-real-value-prop-of-a-permissionless-inference-network)

- [1 Reference](https://olshansky.substack.com/i/144980765/reference)

- [5 Points](https://olshansky.substack.com/i/144980765/points)

Point 1: POKT Network

- Point 2: Model Suppliers

- Point 3: POKT Network

- Point 4: Model Providers

- Point 5: Inference Verification

## **The real value prop of a permissionless inference network**

Having spent more than half a decade working alongside some of the world’s leading ML researchers at Waymo & Magic Leap, [I wrote about](https://olshansky.substack.com/p/24-hours-of-chatgpt) how my worldview changed of what’s possible on **December 1st, 2022**. I use [my personal GPT multiple times a day](https://olshansky.substack.com/p/from-pc-personal-computer-to-pgpt), I [built a RAG](https://x.com/olshansky/status/1682893635506012160) application before the term was coined, and I’ve written about what practical eval entails as a result of my [prior experience and intuition](https://olshansky.substack.com/p/vibe-checks-are-all-you-need); _multiple ML researchers have told me offline that this is the hard truth no one wants to admit._

I frequently test different versions of [Llama on Ollama](https://ollama.com/library?q=llama) but return to GPT-4 for high-quality responses. I experiment with various workflows with the goal of extending them to the whole team. The success-failure ratio is about 50-50 and I plan to detail these experiments here in the future.

If you’re a new reader, this feels like a good opportunity to prompt you (pun intended) to subscribe ‎😅

Most of the AI industry and capital is mostly focused on building large, energy-consuming training clusters, often powered by NVIDIA, _the Nitro of GPUs_. However, my personal experience, combined with many conversations at various AI events has revealed the following:

- **Asynchronous, agentic or assistant-based tasks are not always limited by GPU power**. Slower chatbot responses force me to think deeply about my prompt. It doesn't matter if an LLM that's assisting, teaching or reviewing something takes 60 seconds or 10 seconds.

- **Costs can accumulate quickly**. I use Llama3 locally for experiments but rely on GPT-4 APIs in "production." Iterations can cost $15 in 15 minutes or less. If OpenAI offered GPT-4 on cheaper hardware, at the cost of increased latency, I’d sign up.

- **Experimentation is hard.** Every time I want to try out a new model, I need to spend half an hour downloading a 50GB file only to learn that it’s “bad” after doing a few _vibe checks_.

- **Energy**. Some of my more complex local workflows make my M1 MacBook pro overheat to the point where I’m concerned about long-term damage, forgoing the battery life when I’m on the road.

Our team at [Grove](https://grove.city/) is piloting the expansion of [POKT Network](https://pokt.network/) to support LLM inference. This isn't just a "Crypto x AI" narrative. It addresses cost, quality, energy, and enables both experimentation and incentivization. It's a permissionless network of hardware operators, that has been live for almost 4 years, offering high-quality services for blockchain RPC queries; _see the metrics [here](https://poktscan.com/)_. Gateways abstract protocol complexities, providing value (cost & quality) with familiar SLAs. If an application doesn’t want to use a gateway, the onus of quality-of-service checks is on them.

The argument that scale is easier for centralized, vertically integrated companies is fair, but it comes with tradeoffs. There is a huge opportunity for idle mid-market GPUs to provide inference at a higher latency, but lower cost and satisfy many (not all) use cases. The [litepaper we wrote](https://arxiv.org/abs/2405.20450) came out of a real need for this service, so it was the obvious next step in the evolution of the network we were already designing, building and growing.

**If you’re involved in maintaining cluster of mid-market GPUs which are sitting idle, this is a CALL TO ACTION to leave a comment and we’ll make something happen.**

-

## **1 Reference**

The one reference you need is just the https://arxiv.org/abs/2405.20450

https://arxiv.org/abs/2405.20450

## **5 Points**

##### **1. POKT Network - **A mature protocol & ecosystem primed to expand from web3 queries to LLM inference.

Handles **500M daily requests** with decentralized load balancing.

- The **Remote Procedure Call (RPC) abstraction** is agnostic to the data being transported or compute being invoked.

- LLM nodes are **compute-heavy;** Blockchain nodes are **networking-heavy**.

- Unique value proposition: **verifiable on-chain counter** as a non-interactive optimistic rate limiter.

##### **2. **Model Sources **- AI researchers can monetize their open-source work by making it publicly available on the network.**

- No need for backend infrastructure maintenance.

- No need for front-end user-facing products.

- Earnings are proportional to verified usage volume.

##### **3. Model Suppliers**: Operators specialized in efficient hardware deployment & maintenance.

- Leverage both dedicated and idle hardware.

- Ideal for temporarily idle NVIDIA GPUs or unused AMD (or other) GPUs not good enough for training.

##### **4. Model Providers**: Gateways facilitate network access, abstracting out protocol

- Provide permissionless quality-of-service, SLA guarantees, dashboards, value-add features, etc…

- Can focus on things like routing requests to the best LLM, without expertise in hardware maintenance.

##### **5. Inference Verification**

- This is a hard problem that has no silver bullet. POKT Network has a sufficiently good solution to it by aligning incentives and having Gateways (see [Grove’s SLA](https://www.grove.city/sla)) provide enterprise grade customer support. That said, we have tons of ideas (see the screenshot below from the paper) that we’ll iterate on in the years to come.
