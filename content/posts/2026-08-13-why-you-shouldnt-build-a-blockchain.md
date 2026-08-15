---
title: "Why You Shouldn’t Build a Blockchain"
date: 2026-08-13T20:01:10-0700
draft: false
description: "What I learned after spending four years building one"
tags: ["Crypto", "Blockchain", "Distributed Systems", "Decentralization", "Reflection", "Agentic Commerce"]
categories: ["Posts"]
substack_url: "https://olshansky.substack.com/p/why-you-shouldnt-build-a-blockchain"
cover:
    image: "/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-header.png"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

*Special thanks to [0xRahul](https://x.com/omw_to_the_moon) for feedback and review.*

**Preamble**: In early 2016, Ethereum was my gateway into the crypto industry. From late 2021 through early 2026, I worked in the industry full-time. I saw the good, the bad, and the ugly. More recently, I’ve had a handful of conversations where people asked me: *“So after all these years, what do you think?”* This post aims to capture my journey, the opinions I formed along the way, the tradeoffs of having a blockchain, and where I believe value will accrue in the industry moving forward.

*tl;dr*

1.  **Blockchains are insurance you rarely use.** You pay a premium in cost and complexity, hoping you’ll never need it.

2.  **Distributed systems are not decentralized networks**. These two are often conflated but solve completely different problems.

3.  **You don’t need a token**. With the rise, adoption, and regulation of stablecoins, there should *almost* never be a reason for a project to have its own token.

4.  **Agentic commerce.** Reliable, scalable, and cost-effective digital payments require new infrastructure, and a few large players are leading the charge.

## 2014 - 2016: Early Days and Nerd Sniping

In 2014, I did my undergrad thesis at UofT in speeding up fMRI analysis. A graduate student was responsible for migrating PCA analysis over from a CPU to a GPU, and I helped by distributing it over a cluster using Hadoop MapReduce.

In hindsight, I should have seen the pattern and capitalized on the fact that Cloud (distributed computing) and GPUs (parallel computing) were the future, but 🤷

I was aware of Bitcoin at the time, but didn’t think much of it. When Ethereum came out, my interest spiked because it led with “smart distributed systems” rather than Bitcoin’s “economic anarchism”. Ethereum was the ideal [nerd snipe](https://en.wiktionary.org/wiki/nerd-snipe) by living at the elegant intersection of distributed systems, cryptography, game theory, decentralized networks and programmable trust, and digital money.

## 2016 - 2018: Losing and Regaining Interest

Before the 2017 [ICO craze](https://en.wikipedia.org/wiki/Initial_coin_offering) kicked off, I got interested in prediction markets (e.g. [Augur](https://www.augur.net/), [Gnosis](https://www.gnosis.io/blog/ten-years-of-gnosis-from-prediction-markets-to-a-user-owned-open-finance-revolution)) and Decentralized Autonomous Organizations (e.g. [Aragon](https://www.aragon.org/)). DAOs were a cool idea that never materialized - there’s a reason they say that democracy is the worst form of government, except for all the others. Years later, prediction markets caught on through a new generation of companies (i.e. Polymarket and Kalshi), though I’m still hoping those companies shift focus from everyday gambling to leveraging the [wisdom of the crowds](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd).

In late 2018, I went to a couple of conferences and got disenchanted by suits building out [IBM’s Hyperledger](https://www.ibm.com/think/topics/hyperledger). Around the same time, I kept one foot in the industry by becoming an advisor for a project called [Pocket Network](https://pokt.network) building a decentralized [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) network. I like to describe it as a marketplace of API providers for canonical data sets, akin to what [OpenRouter](https://openrouter.com/) has done for LLM inference providers.

I didn’t pay much attention to the NFT boom, and looked past DeFi summer. I was never a fan of the speculative side of crypto and was more interested in the value that [Decentralized Physical Infrastructure Networks](https://en.wikipedia.org/wiki/Decentralized_physical_infrastructure_network) (DePINs) could bring through smart request routing and incentive alignment of unused hardware.

## 2021 - 2025: Pocket Network, Grove, APIs and QoS

In late 2021, I got invited as a guest to Pocket Network’s offsite, and ended up joining as a consensus protocol engineer [after running into Robert Downey Jr. in Mexico City](https://olshansky.substack.com/p/a-life-changing-trip-to-mexico-on).

Pocket Network’s mission was permissionless infrastructure. The core problem it was trying to solve was access to reliable blockchain data. Why? Because most users and institutions don’t want to run their own infrastructure¹.

There were two entities responsible for making this happen:

1.  **Pocket Network Foundation**: A nonprofit entity that stewarded the Pocket Network blockchain, community, and token ecosystem. It acted as a liaison between the mission and the development team.

2.  **Grove**: A for-profit corporation that led the technical R&D for the Pocket Network blockchain, launched the primary gateway to the network, and focused on customer acquisition and building products on top of the network.

We designed the blockchain to coordinate a permissionless network of infrastructure providers. It included primitives for privacy-preserving requests and a verifiable rate limiter. We also built a multi-provider API gateway.

<img src="/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-pocket-network.png" alt="Pocket Network architecture diagram" width="70%">

Along the way, we learned that customers only cared about **R**eliable, **P**erformant, and **C**ost-effective API endpoints, with a dashboard where they could track usage, spend, permissions, etc.²

Retail participants mostly cared about what Pocket Network’s blockchain could do, in the hope that the narrative would make the token price go up. Enterprise customers, which captured the bulk of the real revenue, couldn’t care less about the underlying blockchain as long as they were getting a reliable service with customer support.

The blockchain was built around the ethos that originally drove the crypto industry: permissionless and censorship-resistant systems. We designed and implemented a protocol called [Relay Mining](https://arxiv.org/abs/2305.10672) to enable verifiable rate limiting. In other words, a provider didn’t have to trust a central party to accurately report how many API requests it had served.

> While intellectually stimulating, [hard and valuable](https://alearningaday.blog/2026/08/10/hard-and-valuable-arent-the-same-thing/) don’t have a direct correlation.³

When customers came to Grove, they didn’t care about the blockchain. All they cared about was the reliability of our service.

The [Quality-of-Service module](https://github.com/pokt-network/path/tree/main/qos) underpinning the gateway was the core component that made the network useful. Think of it as a smart load balancer with layers of composable rules, knobs, triggers, and circuit breakers that route an API request to the best provider.

Without a blockchain, the gateway would begin to resemble [OpenRouter](https://openrouter.ai/): a service that routes requests across multiple providers based on factors like cost, latency, and reliability. Like fraud detection, routing doesn’t have a silver-bullet solution. Lots of composable rules and checks accumulate to push the system over a minimum reliability threshold. From there, you continuously iterate as the underlying adversarial network changes.

<img src="/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-qos.png" alt="Quality-of-Service routing diagram" width="70%">

## Distributed Systems Are Not Decentralized Networks

When you’re in the heat of things, it’s easy to keep up with the inertia, and hard to challenge the underlying premise of what you’re doing and why.

Retail investors were making noise hoping the token price would go up. Institutional investors were asking questions about the investment in blockchain development and the gateway’s model for sustainable revenue. Customers were reaching out about our ability to meet our SLAs. On the leadership team, we’d have daily conversations about runway, product-market fit, resource allocation, or a potential pivot.⁴

The core constraint we accepted and never challenged was the presence of a token. A token is the mechanism that differentiates a distributed system from a decentralized network by enabling incentive alignment. At face value, it’s really easy to conflate the properties and characteristics of the two. But it’s as much of a misnomer as comparing AI research with DevOps. They need to tango, but one must lead and has large implications on the other.

**Blockchains leverage decentralized [state machine replication](https://en.wikipedia.org/wiki/State_machine_replication) to build a [distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger). Cloud services leverage centralized orchestration of distributed infrastructure to build scalable applications. The key difference is that blockchains prioritize [safety and liveness](https://en.wikipedia.org/wiki/Safety_and_liveness_properties) under adversarial conditions, while cloud services prioritize availability, latency, scalability, and operational control.**

Both adhere to the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem), but with a different set of tradeoffs, tolerance bands and failure modes. For example, a [proof-of-stake](https://en.wikipedia.org/wiki/Proof_of_stake)-based decentralized network will halt if less than two-thirds of the validators are offline. A traditional distributed system may keep operating as long as one node keeps responding to client requests.

A decentralized network is always a distributed system, but a distributed system is not necessarily a decentralized network. A phrase I often used was:

> Decentralization is a byproduct of a permissionless and incentive-driven system.

The degree of decentralization that’s necessary for any system or network is an open question. Everyone is using cloud services from Google, Amazon, Microsoft and numerous other companies. None of these are decentralized. A single customer goes to a single provider and uses its reliably distributed system. Decentralization solves a problem no one is complaining about⁵.

<img src="/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-decentralization.png" alt="Distributed systems and decentralized networks" width="70%">

## Decentralization Comes at a Premium

The properties at the core of a blockchain revolve around [crypto-economics](https://en.wikipedia.org/wiki/Cryptoeconomics). The value this brings is reliability when trust is minimized. This value comes at a cost.

[Bitcoin](https://bitcoin.org/bitcoin.pdf) is a very expensive canonical time-stamping service. Ethereum is a very expensive shared virtual machine. Pocket Network is a very complex and expensive counter used for rate limiting without a central party.

**Do you know how much complexity this adds? A LOT.** Any degree of observability, rollbacks, upgrades, or migrations, which are already a pain, becomes 10x harder.

**When would we ever need this?** If there’s a black swan event where the economy collapses, a foreign entity invades our networks, or adversarial AI agents take over the internet, then there *might* be a need for all of this to come into play. Otherwise, the customer doesn’t care, so let’s just keep things simple.

Blockchains make software slower, more complex, and more expensive in exchange for being resilient to the black swan event.

> It’s like insurance. You pay a premium hoping you’ll never need to use it.

The payment can come in the form of time, complexity, cost, or a combination of all three.

## Do you need a token though?

**The answer is easy: No, you do not need a token. ⁶**

The goal of a token is incentive alignment. Incentive alignment is critical to any system, digital or not. Financial incentives are a strong motivator. But, the process of staking can be simplified to two primitives: earning interest on invested funds, and putting money in escrow that can be taken away. A digital version of a fiat currency suffices here; $USDC can be used in the same way.

> An application-specific currency creates an unnecessary conflation between product utility and financial speculation.

In the public markets, some companies choose to go public. There are lots of reasons to do this including accountability, liquidity, or retail opportunity to share in the upside. On the other hand, some companies choose to stay private to avoid the overhead or distraction it could bring to a business.

In both cases, being a public or private company does not materially impact the underlying design of the business. In crypto, a token conflates utility and speculation, leading to even more unnecessary complexity.

## 2026+: Agentic Payments and the Future of Crypto

I see three key pillars setting the foundation for sustainable long-term value:

1.  **Digital ledger**. Scalable payment rails shared by major financial institutions.

2.  **Stablecoins**. Digital representation of fiat currency.

3.  **Agentic commerce.** Internet-native protocols to enable headless money transmission.

None of these need the characteristics of decentralized networks, but require all of the properties of distributed systems.

Under certain black swan circumstances, someone will yell, “I told you so” if we end up needing the permissionless and censorship-resistant properties of blockchains. Until that day arrives, programmable money will play a much more critical role in growing the economy.

As agents proliferate, headless gateways to the internet will become more important. Humans will have a super-app similar to OpenAI’s Codex, and the agents behind the scenes will leverage a super-api via a super-cli. Wallets and funds will be a basic primitive that runs on shared payment rails. We shouldn’t be relying on CSVs being transferred between banks every night, but we also don’t need it to be permissionless, nor do we need a new currency.

> In the same way that we [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) data to a database via an API, we should be able to check and transfer balances via an API.

<img src="/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-bell-curve.jpeg" alt="Bell curve of decentralization" width="70%">

At the moment, I see three major players pushing this forward:

1.  **Stripe** is doing all the right things in building the future of global digital payments. They’re incrementally adding the right partners, making tradeoffs around privacy and safety from a practical user lens without preconceived ideals, and taking a very long-term view. With the progress [Tempo](https://tempo.xyz) is making, alongside the foundation [Machine Payments Protocol](https://mpp.dev/) set in place, I believe Stripe has the potential to be one of the world’s largest companies in a couple of decades, managing a substantial part of the global GDP.

2.  **Cloudflare** made a couple of acquisitions over the past year including [Will Papper](https://x.com/WillPapper/status/2072339786531274861) of [Syndicateio](https://x.com/Syndicateio) and [Human Native AI](https://www.cloudflare.com/press/press-releases/2026/cloudflare-strengthens-content-offering-to-ai-companies-with-acquisition-of-human-native/). This quickly resulted in the release of products like the [Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/), [Cloudflare Wallets](https://blog.cloudflare.com/wallets/), and getting websites ready for [Agentic Commerce](https://blog.cloudflare.com/aeo/). While Stripe is setting the foundation for payments, Cloudflare is building all of the infrastructure agents will need to access the payment rails via a safe and scalable gateway.

3.  **Coinbase** is the most crypto-native of the three. On the surface, they’re lagging on adoption and distribution, but are often the ones leading with ideas and initiatives. For example, Coinbase was key in coming up with [x402.org](https://x402.org), which recently joined the [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications). This protocol kicked off the work Cloudflare and Stripe have done. Coinbase also played a key role in creating and launching $USDC, even though Circle has been the primary driver of stablecoin growth and adoption in the US.

## Concluding Thoughts and Painful Lessons

There are lots of lessons here, but none are new. Listening to users’ pain points, following what the customer is paying for, and iterating quickly are the oldest rules in the playbook. But, there’s a difference between knowing them, embodying them, and having them be second nature.

The other lesson I learnt the hard way is that “truth-seeking” or “thinking from first principles” is easier said than done when things aren’t up and to the right. The truth is likely tough to hear, and if that’s the case, acting on it goes against the grain. The friction is worth it, but it’ll burn.

**Questioning and challenging every constraint is easy to say, but hard to do.**

> So do we need censorship-resistant, permissionless, verifiable networks? Maybe one day, but we shouldn’t lead with them.

------------------------------------------------------------------------

## Appendix

1. Running your own infrastructure is a full-time job. Outside of a small privacy-sensitive population and tinkerers, both developers and enterprises look for ways to delegate it elsewhere. **I’m seeing very similar narratives and market behaviors play out in Sovereign AI as we did in crypto infrastructure**. Enterprises are price agnostic when outsourcing the architecture and maintenance of their data, training and inference as long as they have guarantees around the use, privacy, and security of their data along with the reliability and control of how it’s used. I believe this is what companies like Palantir are capitalizing on. Developers are less sensitive to the compliance requirements, but want to focus on building applications and spend less time on infrastructure, which is why Neoclouds are having such a good run.

2. To my knowledge, we were the first to coin the [RPC Trilemma](https://www.youtube.com/watch?v=7rQ4Awfx79g&t=3s). Remote procedure calls need to be reliable, performant and cost-effective. Be it a request for data or inference, there are a lot of analogues.

3. There are lots of really cool, interesting, and potentially useful primitives that could be used elsewhere but [Relay Mining](https://arxiv.org/abs/2305.10672) was not where the value accrued.

<img src="/images/posts/2026-08-13-why-you-shouldnt-build-a-blockchain-appendix.png" alt="Appendix diagram" width="70%">

4. We pivoted to agentic payments in October 2025. In hindsight, we did the right thing at the right time, leveraging our experience, relationships, knowledge, and intuition. We leveraged AI to the max and executed as well as I believe we could have.

5. An interesting thought experiment is if financial incentive alignment, along with decentralized consensus protocols, could play a role in organizing rogue or adversarial agents. There might be something there, but in the foreseeable future, I believe it’s more applicable to a short sci-fi story rather than a product that needs to be built.

6. There’s room for a longer discussion for a handful of the original players in the crypto space like Bitcoin, Ethereum, Zcash, and potentially a few others. These have achieved escape velocity and were built in a different time.