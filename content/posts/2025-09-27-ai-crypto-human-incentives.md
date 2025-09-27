---
title: "Incentives & Outcomes in Humans, AI, and Crypto"
date: 2025-09-27T09:15:00-0700
draft: false
description: ""
tags:
  - "post"
  - "ai"
  - "crypto"
  - "behaviour"
  - "incentives"
  - "psychology"
  - "economics"
categories: []
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

- [On Charlie Munger](#on-charlie-munger)
- [Incentives in Humans](#incentives-in-humans)
- [Incentives in AI](#incentives-in-ai)
- [Incentives in Crypto](#incentives-in-crypto)
- [Putting it all together](#putting-it-all-together)
  - [Art, Science \& Tradeoffs](#art-science--tradeoffs)

## On Charlie Munger

Charlie Munger once said:

> “Show me the incentive, and I’ll show you the outcome.”

If he were in his prime today, he’d be the Czar of AI & Crypto.

[David Sacks](https://en.wikipedia.org/wiki/David_O._Sacks), the current Czar of AI & Crypto in 2025,
is doing a phenomenal job on the legislative front, but Charlie would have embodied it differently.

Incentives run the world. They're innate to human nature. What I find intriguing is
how this core understanding translates to other domains.

## Incentives in Humans

Imagine you're hiring a team of 10 people to get a job done in 30 days.

You've likely heard of [Parkinson's Law](https://en.wikipedia.org/wiki/Parkinson%27s_law),
which states that **work expands so as to fill the time available for its completion**.

With the exception of a few rare cases, such as [The Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project), I'm saddened to say this law is alive and well. Unfortunately, things often
get delayed as well.

But what if we leverage two tools: Bonuses & [Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion)?

**Bonus** — What if we give each of those 10 people an extra $1,000 per day for each day they complete the task before the deadline? That may actually be a way to circumvent Parkinson's Law and get things done.

**Loss Aversion** — What if we give each of those 10 people an extra $10,000 on day 1,
and take away $1,000 a day for each day the timeline extends after day 30? Since the money is
already in the bank, losses sting more than equivalent gains, making deadlines harder to slip.

Two completely different tactics targeting different parts of human behavior.

I've never put these to the test myself but am sure the day will come.

## Incentives in AI

Most of modern AI is built on the foundations of [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning).

One of the core principles of Reinforcement Learning is a **Reward Function**.

You can think of it like this:

- **Reward function**: what is the definition of success?
- **Reinforcement learning**: a repeating feedback loop that tries random things to increase its reward.

The hard part is defining the function correctly — everything else flows from it.
It's what thousands of the world's smartest people are working on.

The most recent example of incentives in AI that I found fascinating was OpenAI's
[breakthrough on reducing hallucinations](https://openai.com/index/why-language-models-hallucinate/) in GPT-5.

The solution was simple: **If you're unsure, abstain from answering instead of being confident in a wrong answer.**

The results:

- Abstention rate went from 1% (o4-mini) to 52% (gpt-5-thinking-mini)
- Error rate decreased from 75% (o4-mini) to 26% (gpt-5-thinking-mini)

This shifted the model’s incentive from “always answer” to “only answer when confident,”
which directly cut hallucinations.

## Incentives in Crypto

Having been part of the crypto industry for nearly a decade, I've seen this
evolve and take many different forms — from [Bitcoin Mining](https://en.wikipedia.org/wiki/Proof_of_work),
to [Yield Farming](https://hedera.com/learning/decentralized-finance/defi-yield-farming),
and the entire **Proof-of-X** [verifiability ecosystem](https://vitalik.eth.limo/general/2025/09/24/openness_and_verifiability.html) in between.

I believe most future value will come from applying [Proof-of-Stake](https://en.wikipedia.org/wiki/Proof_of_stake) mechanics from first principles:

1. **Fees**: Rewards and payments for providing utility or value-add services.
2. **Staking**: Putting money in escrow — locking up funds that can be rewarded or taken away.
3. **Slashing**: Penalties for adversarial or faulty behavior — taking away the money you have in escrow.

**Fees** are pretty self-explanatory. No different than the 2–3% that credit cards charge.

**Staking** is similar to a security deposit or an insurance premium. It's not
leveraged heavily in day-to-day life, and often relies on lengthy legal or banking processes,
so there is a big opportunity here.

**Slashing** is even less common. The closest real-world equivalent would be losing a rental deposit
for damaging an apartment, or court-ordered damages for breaking a contract.

## Putting it all together

Let's put it all together by using human incentives, AI agents, and crypto-native digital money.

Assume the following scenario:

1. You need to hire someone to get a job done in 10 days for $10,000.
2. You are willing to pay an extra $1,000 for every day the job gets done early.
3. You are going to provide access to sensitive information and need to make sure the counterparty doesn't act adversarially.

The real-world flow would be:

1. You put $10,000 in escrow for completion of the job. **Staking. Fees.**
2. You put an extra $10,000 in escrow as a potential bonus payout. For every day that passes, the worker earns $1,000 less of it. **Staking. Incentives. Reward Function.**
3. The worker puts $10,000 in escrow as proof they won’t misbehave. **Staking.**
4. Anytime the worker does something faulty or wrong, you take a part of their stake. **Reinforcement Learning. Slashing.**

### Art, Science & Tradeoffs

Anyone who has worked in Machine Learning would agree that the process of defining
a reward function is both an art and a science with tradeoffs.

Similarly, the process of defining and verifying slashing conditions in Crypto is
also both an art and a science with tradeoffs.

The beauty is that whether in humans, machines, or markets, progress comes from iterating incentives until they align with outcomes.
