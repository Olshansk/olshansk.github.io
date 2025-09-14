---
title: "How a Web2 Company Uses Crypto to Power Open Data APIs"
date: 2025-08-22T16:18:09-07:00
draft: false
description: "There is a big opportunity to build the “Google home page” for finding and accessing APIs for any open data sources and services."
tags: ["web2", "company"]
categories: ["cryptocurrency", "technology", "machine-learning", "business"]
substack_url: "https://olshansky.substack.com/p/how-a-web2-company-uses-crypto-to"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

### How a Web2 Company Uses Crypto to Power Open Data APIs

_Thank you to_[ _Art_](https://x.com/ArtSabintsev) _,_[_Fred_](https://x.com/fredt_io) _ & _[_Jake_](https://www.linkedin.com/in/jake-bodanis/) _for reviewing and providing feedback on this post!_

**Question** : Does your software use [API](https://en.wikipedia.org/wiki/API)s? Where do you find the endpoints? How do you get the specifications? How do you ensure quality? 🤔

### **_tl;dr_**

1. There is a big opportunity to build the “Google home page” for finding and accessing open data sources and services.
2. An open marketplace of APIs does not exist today.
3. API Discovery and RPC Quality are the two core primitives necessary to enable this.
4. An API marketplace fills a gap alongside the new [HTTP x402](https://www.coinbase.com/developer-platform/discover/launches/x402) standard, championed by Coinbase, for _internet-native network request payments._

My goal with this blog is to give you a sense of how the following graphic fits into today’s internet-native data access landscape. We’re slowly shifting to account for more _human-out-of-the-loop_ workflows, while continuing to accommodate both enterprises and independent developers.

![](/images/posts/2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis-image-01.png)To enable enterprises, developers and agents to find and access any data or services online, we need to make these two things seamless: API Discovery and RPC Quality.

I recently did a [2-minute pitch](https://www.youtube.com/watch?v=rdIlS36IFaQ&list=PLeHvNSh0enXSflgNf-YC6jW6K3Fh4cS5E&index=22) of Pocket Network, PATH and Grove at the [Science of Blockchain Conference](https://cbr.stanford.edu/).

![](/images/posts/2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis-image-02.png)[Timestamped link](https://www.youtube.com/live/c1_OP8DHjIs?si=R4gob9AI-NIucqwe&t=13705) / [Separate 2-minute upload](https://www.youtube.com/watch?v=rdIlS36IFaQ&list=PLeHvNSh0enXSflgNf-YC6jW6K3Fh4cS5E&index=22)

I received feedback from people at the event, my team watching remotely, my friends, and most importantly, my mom.

I wanted to gather all that feedback in a blog post that really captures how big of a problem (opportunity) everyone is overlooking.

To get started, here are some analogies I found myself using in various conversations at the conference:

- **Unstoppable Data:** kind of makes sense, but feels a bit cringey.
- **API Directory:** Clear but limiting, and makes me sound like a boomer, which there’s nothing wrong with 😏.
- **Permissionless APIs:** Sounds cool, but why does anyone need this?
- **Decentralized RPC:** This might make sense to someone deep in Web3, but raises more questions than it answers.

My goal with this blog is to provide more answers than questions. It’s written in a way that you don’t have to read it until the very end to get value. This allows non-technical individuals to get the gist, while crypto-native engineers can get the details.

### Table of Contents

- What’s the problem in non-technical terms?
- What’s the problem in technical terms?
- How big is this problem?
- What is the solution?
- Who is our customer?
- What is the moat and differentiator?
- Why now?

### What’s the problem in non-technical terms?

**_tl;dr_** _Humans need browsers and search engines to find websites. Programs need directories of data providers, along with technical specifications that explain how to access that data._

When humans use the internet, they need a browser and a way to find the right website or link. At first this looked like the Yahoo Directory, then it evolved into search engines like Google, and today it’s increasingly shifting toward chat interfaces like ChatGPT.

When computer programs interact with the internet, they also need a way to find, communicate with, and retrieve the data they need. This usually comes in the form of an endpoint to a data or service provider, accompanied by a technical specification explaining how that data can be accessed. Instead of a computer screen, a mouse, and a keyboard, all that’s required is a server and a reliable internet connection.

Take the weather app as an example: how does it know where to get the data, what format that data comes in, and how to parse it?

This is where internet primitives like APIs and RPCs come in. They’re the forks and knives of accessing and parsing data online.

If you’ve never heard these terms before, that’s fine — just think of this as the core problem we’re solving. If you _are_ familiar, the next section will dive deeper into the API economy.

### What’s the problem in technical terms?

**_tl;dr_** _The internet runs on APIs over RPC. While API specifications and RPC performance are well-studied, API discovery and RPC quality remain under-discussed, and are critical for the coming agent economy._

**What is an RPC?** A **R** emote **P** rocedure **C** all is the medium programs use to communicate over the internet (the transport layer). Think of it as the wire carrying the signals.

**What is an API?** An **A** pplication **P** rogramming **I** nterface is the language spoken on top of that wire. It’s like the difference between communicating in Morse code vs. English.

**API Discovery:** If you’re Gen Z, imagine a YouTube “discover” page, but for APIs. If you’re a Boomer, think Yellow Pages, but for APIs.

In reality, developers usually just ask around, search Google, or prompt ChatGPT. I asked over two dozen engineers how they find APIs, and even in 2025, it’s still an ad hoc process with no consistent standard.

**RPC Quality:** How can you be sure a provider’s data is **r** eliable, **p** erformant, and **c** orrect? [Service level agreements](https://en.wikipedia.org/wiki/Service-level_agreement) try to cover this, but in practice customers simply assume it works. When you open Netflix, you expect a stream to play, and your expectation of success is essentially 100%.

We have mature ways of measuring performance (e.g. latency), but no standards for quality (e.g. correctness). Unless you trust _WebsiteYouGotDataFrom.com_ , you can’t be certain the data is right.

**The key takeaways** :

- We have standards for defining API specifications, but no mechanisms for API discovery.
- We can measure RPC performance from a trusted provider, but we have no way to guarantee RPC quality from an unknown one.

The next section will dive into the types of data you might want to access and how our solution addresses these gaps. If you already get the gist, feel free to scroll and just enjoy the pictures.

### How big is this problem?

**_tl;dr_** _API discovery and RPC quality are open problems for any software systems. The first iteration of our solution transfers broadly from any open canonical dataset to any open-source stateless service._

To scope the markets we’re tackling, I split them into two categories:

- **Open Canonical Data Sets** :\*\*\*\* Publicly available data sources that are not user-specific (i.e. tenant-based).
- **Open Source Stateless Services:** Open source services accessible via publicly specified APIs.

![](/images/posts/2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis-image-03.png)Example list of Open Canonical Data Sets (left) and Open Source Stateless Services (right)

I’ve been asked if this is a data marketplace. If you squint and skip a few steps, it theoretically could be. In practice, we need to focus on being 10x better than anyone else at these two things. Once we get there, a data marketplace is definitely on the horizon.

The more I think about it, the more I realize starting with blockchain data was a bootstrapping coincidence. We could have begun with weather data, but the market wasn’t big enough. Blockchain simply gave us the largest initial opportunity.

Next, we’ll dive into how core crypto primitives like incentives and permissionlessness play a role in solving this problem. These primitives are critical to differentiating a world where you need to go and get someone’s approval to sell something, or just open up a kiosk on the street without any permits. If you provide a high-quality product, you’ll earn what you deserve, and no one cares if you have _“an official signoff”_.

### What is the solution?

**_tl;dr_** _A public incentivized ledger (Pocket Network) enables API discovery. An open-source SDK (PATH) guarantees enterprise-grade quality. A for-profit product (Grove’s Portal) abstracts it all into a trusted developer experience._

The full solution comes together through three components: Pocket Network, PATH and Grove’s Portal.

**Pocket Network** is a blockchain with built-in incentives. Anyone can advertise or discover APIs for data sources or services they need. Service owners and service hosts get rewarded based on the verifiable API meter.

> 💡 Beyond discovery, Pocket Network designed a novel permissionless cryptographic mechanism to meter API usage and settle payments per request. This is where [Coinbase’s new HTTP x402](https://www.coinbase.com/developer-platform/discover/launches/x402) standard for internet-native payments becomes relevant. There are lots of details to dive into which I’ll save for another post.

**PATH** is an open-source SDK that any internet gateway can use to enforce enterprise-grade quality on top of Pocket Network’s permissionless providers. If providers are inconsistent, low-quality, or adversarial, PATH ensures requests are only routed to high-quality and performant nodes.

> 💡 It also unlocks a novel use case: existing infrastructure providers can use the network as fallback “insurance” when their own services go down.

**Grove** operates a consumer-facing portal where developers can instantly get RPC endpoints for any API on Pocket Network. It provides a trusted brand, customer support, and a UI that abstracts away the underlying complexity.

In practice:

- Anyone can access Pocket Network directly, but PATH makes it easier.
- Anyone can use PATH, but Grove makes it easier.

One of the coolest things? Grove delivers infrastructure quality and performance on par with centralized providers, even though we don’t run the backend service infrastructure ourselves!

![](/images/posts/2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis-image-04.png)

### Who is our customer?

**_tl;dr_** _Our customers are enterprises today, independent developers tomorrow, and AI agents in the future._

1.  **Enterprises:** Major enterprises already trust Grove to provide reliable infrastructure. For example, we are [XRPL EVM’s primary RPC provider](https://www.xrplevm.org/blog/xrpl-evm-is-live-this-is-how-to-get-started) and are listed on [Google’s Web3 Marketplace](https://cloud.google.com/application/web3/discover).
2.  **Independent Developers:** These are pay-as-you-go users who sign up through [portal.grove.city](https://portal.grove.city), add a credit card, and start building. They represent the long tail of developers who want fast, reliable access without heavy setup
3.  **AI Agents:** Though still early, this isn’t hype. AI agents will need access to data. They’ll need to know where to find it, how to access it, and they’ll need guarantees that requests succeed with high quality. And importantly, they’ll pay for it using internet-native money.

_That last point deserves its own post…_

### What is the moat and differentiator?

**_tl;dr_** _Pocket Network and PATH make it possible for Grove to build a business through the open-core model._

To understand how Grove can become a large, profitable business, it helps to look at the [open-core model](https://en.wikipedia.org/wiki/Open-core_model) in practice. Let’s use [Supabase](https://supabase.com/) as an example.

Supabase is a development platform built on PostgreSQL. Postgres has been around since the late 80s and open source since the late 90s. Hundreds of companies have tried to build businesses on top of it, with varying levels of success. By the 2010s, hyperscalers like AWS, GCP, and Azure were all offering hosted Postgres solutions.

So how did Supabase, founded in 2020, offering “little differentiation”, end up onboarding [3M+ developers](https://www.linkedin.com/posts/paulcopplestone_the-journey-to-3-million-developers-supabase-activity-7352971832536326146--ESs/) and reaching a [$2B valuation](https://techcrunch.com/2025/04/22/vibe-coding-helps-supabase-nab-200m-at-2b-valuation-just-seven-months-after-its-last-raise/) in under five years? There’s no single answer. For one, it obfuscates the details of how a database works, enabling anyone (non-technical individual or AI agents) to seamlessly spin up a database. Even as a developer, I default to their product because of the superior and simple user experience.

Similarly, just as there was once no obvious answer to _“Where can I easily get a hosted instance of Postgres?”_ , today there’s no obvious answer to \_“Where can I find a reliable API provider for _\_\_?”_

A sustainable API ecosystem can’t be maintained by a single entity, which is why you need **Pocket Network**. It can’t rely on a single entity for quality either, which is why you need **PATH**. And most enterprises and developers don’t want to manage gateways themselves, which is how **Grove** fills the gap.

With over a dozen providers and 100+ developers, we’re already handling around [50 million requests per day](https://poktscan.com/).

What we’ve built so far has been enough to prove there’s a clear gap in API discovery and RPC quality. We’ve completed the heavy technical foundation and are serving live customers. The next step is to iterate and expand the product.

It’s about supporting more services, adding more providers, onboarding more developers and increasing visibility into what’s happening on the network. In addition, we’ll soon be able to start building out integrations with other networks, protocols and institutions, which is the real unlock.

This is just the beginning! The vision is an open, permissionless fabric of data and services powering the next generation of applications and agents.

![](/images/posts/2025-08-22-how-a-web2-company-uses-crypto-to-power-open-data-apis-image-05.png)<https://poktscan.com/> (08/17/2025)

### Why now?

**API Discovery —** Enterprises sign deals with close partners. Developers scour the web for a solution matching the tradeoffs they’re willing to make. Agents will iterate in endless circles until they find an API endpoint that matches the specifications they have found for accessing and parsing the data.

**RPC Quality —** Enterprises rely on service level agreements from close partners. Developers often have half a dozen backups in case one fails. Agents will keep retrying and wasting resources until a request succeeds.

In short, everyone needs a good solution to API Discovery and RPC Quality, yet somehow it’s still missing.

When I asked [@kiwicopple](https://x.com/kiwicopple/) (CEO of Supabase) what led to their success, he kept it simple:

> **T** here isn’t something uniquely open source about the answer — mostly we a) built something people wanted and b) focused on where the market was moving rather than where it was.

The agentic market presents a large opportunity but is still in its toddler years. In the meantime, we are actively building, iterating and polishing the product for enterprises and developers. Once the world of agents is ready, Grove will be too.

_If anything here piqued your interest and you want to reach out, for any reason,_[_Discord is the best way to contact us_](https://discord.gg/build-with-grove) _._

_You can try out the product at_[ _portal.grove.city_](https://portal.grove.city/) _, or learn more by visiting_[ _grove.city_](https://grove.city/) _and_[ _pocket.network_](https://pocket.network/) _._
