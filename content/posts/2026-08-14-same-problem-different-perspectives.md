---
title: "Same problem, different perspectives"
date: 2026-08-14T14:53:23-0700
draft: false
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

## Kicking off the conversation

A friend of mine read my recent post on [Why You Shouldn't Build a Blockchain](https://olshansky.info/posts/2026-08-13-why-you-shouldnt-build-a-blockchain) and reached out with some thoughts that I'd summarize as: _"I still don't get it..."_

We've had countless conversations about whether digital payments need blockchains, crypto, stablecoins, or other improvements that have nothing to do with crypto. My personal perspective has shifted from crypto toward shared digital ledgers between institutions. He still wasn't convinced.

To ground the conversation in something practical, we decided to focus on two cases:

1. How would he send me $2?
2. How would he send me $15,000?

For the first case, we would use Venmo, Cash App, or PayPal. For the second case, he'd use a wire transfer.

## The state of digital payments

Even though there are dozens of billion-dollar companies in payments, the landscape is still confusing.

- Why do we need Plaid to connect to financial institutions when the underlying systems are already digital?
- Why do we have debit, credit, ACH, wire transfers, real-time payments, and everything in between?
- Why can I pay someone instantly in one app, but struggle to move that money back to my own bank account?
- Why do so many payment operations still end in files, batch jobs, and manual reconciliation?
- Why isn't sending $1 as easy as sending $15,000?
- Why does a company like Stripe need workflows for authorizing, holding, settling, retrying, and reconciling funds? Which parts are inherent to money movement, and which parts are artifacts of the rails?
- Why is there no global API where I can send money to `@olshansky` and know that it is final, available, and addressed to the right person?
- Why is sending $1 or $15,000 across borders still difficult?

## The gap in our conversation

There were multiple gaps in our conversation, so this was one of those moments when we had to decompose the discussion.

**User perspective**: A normal individual has a tool of choice for sending $2. That same person is willing to go out of their way to send $15,000. At that size, the friction is partly a feature: it creates a moment for verification, review, and trust.

**Developer perspective**: Developers can use APIs and SDKs from [Stripe](https://docs.stripe.com/api), [Plaid](https://plaid.com/docs/api/), [Dwolla](https://developers.dwolla.com/), [Modern Treasury](https://docs.moderntreasury.com/), [Adyen](https://docs.adyen.com/), [PayPal](https://developer.paypal.com/api/rest/), and others. These products hide a lot of legacy complexity, but they do not eliminate it. They package it into APIs, webhooks, retries, idempotency keys, compliance checks, and reconciliation workflows.

**Tinkerer perspective**: As a tinkerer who has looked into how these systems work, I know there is technology that could make some parts much simpler. That is part of the promise of blockchains. But when the thing being moved is money, simplicity runs into compliance, fraud, reversibility, identity, and liability.

**Founder perspective**: My friend is a founder. He thinks about the specific problem a new product or technology would solve, who would pay for it, and whether the solution can become a business.

**Employee perspective**: As someone who has gone from building companies to looking to join one, I've been thinking about how I can use my experience and expertise to compound on the foundation a company has built.

**The last two are where we found the gap.**

I had a 10-year time horizon for what a company like Stripe should do to avoid falling into the innovator's dilemma. In my view, Stripe should challenge Mastercard, Visa, and the other payment rails by building the global payment relay of the internet. That could be how it goes from a $200 billion company to a $2 trillion company.

However, my friend had a one-to-three-year time horizon for what a new entrant would need to do to disrupt the market. It wasn't about going from $200 billion to $2 trillion, but from $0 to $1 billion. Under those constraints, creating new payment rails is the wrong problem to solve. The better opportunity might be to make the existing rails dramatically easier to use, or to solve one painful step—identity, fraud, reconciliation, settlement, or cross-border movement—better than anyone else.

**Both of us were right, but we were answering different questions.**

I was asking: _What should the dominant company build over the next decade?_ My friend was asking: _What can a new company build and sell in the next few years?_ Those questions can produce completely different answers without either person misunderstanding the technology or the market.

**The lesson?** Before debating whether an idea is good, ask: good for whom, at which layer, and on what time horizon?

> Same problem. Different perspectives. Different answers—and sometimes, all of them are right.
