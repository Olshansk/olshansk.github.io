---
title: "Incentives & Outcomes: Humans, AI & Crypto"
date: 2025-09-27T09:15:00-0700
draft: false
description: ""
tags: []
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

David Sachs is doing a phenomenal front, especially in making things happen on the
legislative front, but Charlie would have embodied it differently.

Incentives run the world. They're innate to human nature. What I find intriguing is
how this core understanding translates to other domains.

## Incentives in Humans

Imagine you're hiring a team of 10 people to get a job done in 30 days.

You've likely heard of [Parkinson's Law](https://en.wikipedia.org/wiki/Parkinson%27s_law),
which states that **work expands so as to fill the time available for its completion**.

With the exception of a few rare case, such as [The Human Genome Project](https://en.wikipedia.org/wiki/Human_Genome_Project), I'm saddened to say this law is alive and well. Unfortunately, things often
get delayed as well.

But, what if we leverage two tools: Bonuses & [Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion).

**Bonus** - What if we give each of those 10 people an extra $1,000 per day for each day they complete the task before the deadline? That may actually be a way to circumvent Parkinson's Law and get shit done.

**Loss Aversion** - What if we give each of those 10 people an extra $10,000 on day 1,
and take away $1,000 a day for each day the timeline extends after day 30? Since losses hurt
more than gains feel good, and the money is already in the bank, no one will want for the project to sall.

Two completely different tactics targeting different parts of human behaviour.

I've never put these to the test myself but am sure the ady will come.

## Incentives in AI

Most of modern AI is built on the foundations of [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning).

One of the core principals of Reinforcement Learning is a **Reward Function**.

You can think of it like this:

- **Reward function**: what is the definition of success?
- **Reinforcement learning**: a repeating feedback loop that tries random things to increase it's reward.

The hard part is actually defining this function and kicking off this loop.
It's what thousands of the world's smartest people are working on.

The most recent example of incentives in AI that I found fascinating was OpenAI's
[breakthrough on reducing hallucinations](https://openai.com/index/why-language-models-hallucinate/) in GPT5.

The solution was simple: **If you're unsure, abstain from answering instead of being confident in a wrong answer.**

The results:

- Abstention rate went from 1% (o4-mini) to 52% (gpt-5-thinking-mini)
- Error rate decreased from 75%(o4-mini) to 26% (gpt-5-thinking-mini)

## Incentives in Crypto

Having been part of the crypto industry for nearly a decade, I've seen this
evolve and take many different form [Bitcoin Mining](https://en.wikipedia.org/wiki/Proof_of_work),
to [Yield Farming](https://hedera.com/learning/decentralized-finance/defi-yield-farming)
and the entire **Proof of X** ecosystem [verifiability ecosystem](https://vitalik.eth.limo/general/2025/09/24/openness_and_verifiability.html) in between.

However, I believe most of the value will come from the extension and integration
of applying [Proof-of-Stake](https://en.wikipedia.org/wiki/Proof_of_stake) components (reconsider this word) from first principles:

1. **Fees**: Rewards and payments for providing utility or value-add services.
2. **Staking**: Putting money in escrow; _locking up some funds that can be rewarded or taken away_.
3. **Slashing**: Penalties for adversarial or faulty behavior; _taking away the money you have in escrow_.

**Fees** are pretty self-explanatory. No different that 2-3% of a transaction credit cards charge.

**Staking** is less common in the real world. It usually relies on the banking system and long-term contracts with tons of legal implications.

**Slashing** is less common in the real world. It usually relies on the banking system and long-term contracts.

## Putting it all together

Let's put it altogether by using human incentivies, AI agents and crypto-native digital money.

Assume the following scenario:

1. You need to hire someone to get a job done in 10 days for $10,000.
2. You are willing to pay an extra $1,000 for every day the job gets done early.
3. You are going to provide access to sensitive information and need to make sure the counterparty doesn't act adverserial.

The real world flow would be:

1. You put $10,000 in escrow for completion of the job. **Staking**. **Fees**.
2. You put an extra $10,000 in escrow as bonus payout. You get back $1,000 of it for every day that passes. **Staking**. **Incentives**. **Reward Function**.
3. An agent puts $10,000 in escrow as proof that they don't misbehave. **Staking**.
4. Anytime the agent doesn't something faulty or wrong, you take a part of their stake. **Reinforcement Learning**. **Slashing**.

### Art, Science & Tradeoffs

Anyone who has worked in Machine Learning would agree that the process of defining
a reward function is both an art and a science with different tradeoffs.

Similarly, the process of defining and verifying slashing conditions in Crypto is
also both an art and a science with tradeoffs.

The beauty is seeing it all come together through constant iteration.
