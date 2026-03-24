---
title: "An Open Letter to Content Publishers"
date: 2026-03-20T17:54:57-0700
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

Reach used to be king. Then revenue entered the conversation.

Companies like Substack and Patreon made earning a core feature. Medium followed.

Now, with AI training and inferring on content, **credit and compensation** are front and center.

**The opportunity is not about squeezing more out of the same revenue model. It's about unlocking new ones.**

## The future of content publishing needs configurable revenue models, not just policy toggles

Medium’s [latest update](https://medium.com/blog/writers-you-now-have-more-control-over-how-ai-companies-use-your-stories-662788e7a6ae) frames the problem well around 3Cs and their AI strategy: **C**onsent, **C**redit, and **C**ompensation.

The current implementation is a binary toggle. Maximize reach or minimize training. Writers choose between getting cited by AI products, having AI learn about their contributions, or opting out entirely.

That is a step in the right direction. But it is not the 3Cs. It is a tradeoff between two of them.

Digg’s [recent reset](https://digg.com/) looks like a different story, but it is not. **If bots, spam, and synthetic engagement dominate the system, trust disappears and the product breaks.** Same root issue.

The internet still runs on economics that assume human attention is scarce, content is static, and abuse is manageable.

None of that is true anymore.

- 🗑️ Slop leads to a low quality internet
- 📢 Noise diffuses our attention
- 🤖 Abuse extends beyond keyboard warriors
- 👻 Engagement is cheap to fake
- 🔗 Distribution is increasingly intermediated
- 🎯 Attention is increasingly fragmented

The infrastructure for agentic commerce is already here, just not evenly adopted.

## The X to Spam Problem

Near the beginning of February, [@nikitabier of X](https://x.com/nikitabier) called this out:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Prediction: In less than 90 days, all channels that we thought were safe from spam &amp; automation will be so flooded that they will no longer be usable in any functional sense: iMessage, phone calls, Gmail. <br><br>And we will have no way to stop it.</p>&mdash; Nikita Bier (@nikitabier) <a href="https://twitter.com/nikitabier/status/2021632774013432061?ref_src=twsrc%5Etfw">February 11, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

And the team at X did not wait to start acting on it. Nikita followed up a month later saying [the financial incentive to spam on X will soon be negative](https://x.com/nikitabier/status/2034143577425776805).

## Not Everyone Wants the Same Thing

We started working on [Grove.city](https://grove.city/) late last year to make sure that content creators can engage their audience and earn what they deserve for high-quality content. It doesn't matter if the creator or consumer is a human or agent: **high quality earns what it deserves**.

Speaking with various content creators, we learnt that not everyone wants the same thing:

- Some want to **engage their audience**
- Some want to **make a living** from it
- Some are **building a personal brand**
- Some just do it as a **hobby**

All of this results in tradeoffs that compete with each other: monetization, exclusivity, exposure, reach, distribution, quality, engagement, attention, and more.

But the current landscape forces everyone into the same set of tradeoffs:

- Want reach? You give up revenue.
- Want revenue? You gate content and lose reach.
- Want engagement? You optimize for algorithms that reward volume over quality.

**The one thing we know for sure is that everyone is open to a solution that simultaneously maximizes Reach and Revenue.**

## Business Models: The Reach vs. Revenue Landscape

Here is the current landscape of business models on the Reach vs Revenue tradeoff matrix, including new models enabled by agentic payment infrastructure:

{{< reach_revenue_graph_infra >}}

**It's not about giving up one revenue stream for another. It's about having more ways to earn. It grows the pie for everyone.**

## What Options Do We Have?

Below is a non-exhaustive list of options companies like Medium could implement to continue enabling reach, create revenue opportunities, and account for AI access.

### 1. Pay to unlock

**One article. One payment. No subscription.**

Most paywalls require a monthly subscription. But what if you could pay to unlock just a single article or video for a small fee?

This creates a middle ground the web mostly skipped over: not free, not subscription, just pay for what you want, when you want it.

### 2. Pay for preview

**Bots pay to peek. Humans decide if it's worth it.**

You've likely seen a handful of articles where you get a preview (a few paragraphs) for free, but then you have to pay to read the rest.

Paying to unlock solves for humans, but not for bots. What if you had to pay a couple of cents to see a preview?

Any bot or AI lab training their models would have to pay to see if they even want to train on your content.

### 3. Pay to comment

**Put your money where your mouth is.**

Up until now, comments have been a binary toggle: open to everyone or completely off. Most platforms turned off comments a decade ago. That was the only available answer.

What if there was a middle ground? Pay to comment.

Are you a keyboard warrior who is willing to give $0.05 to share your frustration? If you're willing to pay, go for it.

Are you a supporter who wants to express your gratitude and get the author's attention? A small economic attribution goes further than a cold email.

Are you a bot that's spamming the internet? Well, if you're willing to pay, maybe some people would be okay with it.

If posting is free, spam scales. If commenting requires a small payment or stake, low-effort abuse becomes more expensive. Quality goes up. Moderation gets easier. Community trust improves.

### 4. Leave a tip

**Let agents and humans say "thank you" with real value.**

We've all heard of Sentiment Analysis, but how about Sentiment Creation?

Imagine if frontier labs gave their agents a _tipping jar_ — leaving a small tip during training or inference whenever they deemed content useful. I'd probably tweet about it every time it happened.

This has been tried many times, but never really took off because there is no sustainable long-term business model for it. What we've seen is that this won't survive as a standalone product but can live side-by-side with the business models above by leveraging the same infrastructure.

## Is the infrastructure for this ready today?

Yes.

Protocols, standards, infrastructure, usage. It's all here. Simple, cheap, and available to everyone. Just hasn't been widely adopted yet.

- 💰 [Stablecoin volumes](https://app.rwa.xyz/stablecoins) are in the billions
- ☁️ Cloudflare launched [Pay-per-crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/)
- 🪙 Coinbase championed the HTTP [x402](https://www.x402.org/) standard
- 💳 Stripe launched [Machine Payments Protocol (MPP)](https://mpp.dev/)
- 🛒 Shopify has the [Universal Commerce Protocol (UCP)](https://shopify.engineering/ucp)
- 🔄 [Agent Transaction Protocol (ATXP)](https://atxp.ai/)
- 🤝 Google's [Agent to Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- 🧠 Anthropic's [MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- ...and probably a handful of others I've forgotten

The building blocks exist. What's missing is adoption.

**If you're interested in integrating a new revenue model into your platform, and not sure where to start, we're here to help. Send [us a message](mailto:hello@grove.city) and we'll help you out.**

---

_We've got a lot of exciting product updates coming soon. Follow us on [X](https://x.com/BuildWithGrove) or create an account at [Grove.city](https://grove.city/) to get early access._
