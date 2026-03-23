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

Reach and engagement used to be the primary focus for any online content publisher or mediator. For example, look at Google or Meta.

Revenue was always a focus for the platform, not the users. That changed as companies like Substack or Patreon emerged, and others like Medium made it a core part of their value proposition.

Now, with AI training and inferring on content, the conversation is doubling down on revenue generation, with more focus on credit and compensation.

**The opportunity, however, is not in simply the ability to earn-more, but the ability to have more-ways-to-earn.**

## The future of content publishing needs configurable revenue models, not just policy toggles

Medium’s [latest update](https://medium.com/blog/writers-you-now-have-more-control-over-how-ai-companies-use-your-stories-662788e7a6ae) frames the problem well around 3Cs and their AI strategy: **C**onsent, **C**redit, and **C**ompensation.

The current implementation is a binary toggle. Maximize reach or minimize training. Writers choose between getting cited by AI products, having AI learn about their contributions, or opting out entirely.

That is a step in the right direction. But it is not the 3Cs. It is a tradeoff between two of them.

Digg’s [recent reset](https://digg.com/) looks like a different story, but it is not. **If bots, spam, and synthetic engagement dominate the system, trust disappears and the product breaks.** Same root issue.

The internet still runs on economics that assume human attention is scarce, content is static, and abuse is manageable. None of that is true anymore. Slop leads to a low quality internet. Noise diffuses our attention. Abuse is rampant and extends beyond keyboard warriors.Engagement is cheap to fake. Distribution is increasingly intermediated. Focus is increasingly scrace. Attention is increasingly fragmented.

The saving grace is that agentic commerce is emerging, and will play a big role in solving this problem. More on this later in the post

## The X to Spam Problem

Near the beginning of February, [@nikitabier of X](https://x.com/nikitabier) called this out:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Prediction: In less than 90 days, all channels that we thought were safe from spam &amp; automation will be so flooded that they will no longer be usable in any functional sense: iMessage, phone calls, Gmail. <br><br>And we will have no way to stop it.</p>&mdash; Nikita Bier (@nikitabier) <a href="https://twitter.com/nikitabier/status/2021632774013432061?ref_src=twsrc%5Etfw">February 11, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

And the team at X did not wait to start acting on it:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The financial incentive to spam on X will decline enormously over the next 30 days and soon be negative.</p>&mdash; Nikita Bier (@nikitabier) <a href="https://twitter.com/nikitabier/status/2034143577425776805?ref_src=twsrc%5Etfw">March 18, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

X money might also play a role here but it's too early to tell.

## Not Everyone Wants the Same Thing

We started working on [Grove.city](https://grove.city/) late last year to make sure that content creators can engage their audience and earn what they deserve for high-quality content. It doesn't matter if the creator or consumer is a human or agent: **high quality earns what it deserves**.

Speaking with various content creators, we learnt that not everyone wants the same thing. Some are looking for a way to engage their audience. Some want to make a living or build a business around it. Some are building a personal brand. Others just do it as a hobby.

All of this results in tradeoffs that compete with each other: moentization, exclusivity, exposure, reach, distribution, quality, engagement, attention, and more.

But the current landscape forces everyone into the same set of tradeoffs. If you want reach, you give up revenue. If you want revenue, you gate content and lose reach. If you want engagement, you optimize for algorithms that reward volume over quality.

**The one thing we know for sure is that everyone is open to a solution that simulatenously maximizes Reach and Revenue.**

## Business Models: The Reach vs. Revenue Landscape

Here is the current landscape of existing business models on the Reach vs Revenue tradeoff matrix:

![Reach vs. revenue today](/images/posts/2026-03-20-reach-revenue-baseline.png)

With agnetic payment infrastructure, and a world of agent consumers and AI labs, there are new revenue business models:

![New agentic infrastructure](/images/posts/2026-03-20-reach-revenue-infra.png)

**The key is that it's not about giving up one revenue stream for another. It's about having more ways to earn. It grows the pie for everyone.**

## What Options Do We Have?

Below is a non-exhaustive list of options companies like medium could implement to continue enabling reach, create revenue opportunities, and account for AI access.

### 1. Pay to unlock

Most paywalls require a monthly subscription. But what if you could pay to unlock just a single article or video for a small fee?

This creates a middle ground the web mostly skipped over: not free, not subscription, just pay for what you want, when you want it.

### 2. Pay for preview

You've likely seen a handful of articles where you get a preview (a few paragraphs) for free, but then you have to pay to read the rest.

Paying to unlock solves for humans, but not for bots. What if you had to pay a couple of cents to see a preview?

Any bot or AI lab training their models would have to pay to see if they even want to train on your content.

### 3. Pay to comment

If posting is free, spam scales.

If commenting requires a small payment or stake, low-effort abuse becomes more expensive. Quality goes up. Moderation gets easier. Community trust improves.

### 4. Leave a tip

We've all heard of Sentiment Analaysis, but how about Sentiment Creation?

Imagine frontier labs had a _tipping-jar_ they would give to agents that can leave a tip during training or inference runs if they deemed your content useful? I'd probably tweet about it every time it happened.

This has been tried many times, but never really took off because there is no sustainable long-term business model for it. What we've seen is that this won't survive as a standalone product but can live side-by-side with the business models above by leveraging the same infrastructure.

## Is the infrastructure for this ready today?

Yes.

Protocols, standards, infrastructure, usage. It's all here. Simple, cheap, and available to everyone. Just hasn't been widely adopted yet.

[Stablecoin Volumes](https://app.rwa.xyz/stablecoins) are in the billions. Cloudflare launched [Pay-per-crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/). Coinbase championed the HTTP [x402](https://www.x402.org/) standard. Stripe launched [Machine Payments Protocol (MPP)](https://mpp.dev/). Shopify has the [Universal Commerce Protocol (UCP)](https://shopify.engineering/ucp). There's also the [Agent Transaction Protocol (ATXP)](https://atxp.ai/), Google's [Agent to Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), Anthropic's [MCP](https://modelcontextprotocol.io/docs/getting-started/intro), and probably a handful of others I've fogotten.

**If you're interest in integrating a new revenue model into your platform, and not sure where to start, we're here to help. Send [us a message](mailto:hello@grove.city) and we'll help you out.**

---

_We've got a lot of exciting product updates coming soon. Follow us on [X](https://x.com/BuildWithGrove) or create an account at [Grove.city](https://grove.city/) to get early access._
