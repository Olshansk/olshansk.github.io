---
title: "7 Pocket Network Analogies"
date: 2024-10-22T14:40:47-07:00
draft: false
tags: ["blockchain", "pocket-network", "web3", "analogies", "networking"]
categories: ["Blockchain", "Pocket Network", "Products"]
summary: "tl;dr Explaining what Pocket Network is through a series of 7 internet networking analogies. Subscribe if you want to be notified of when…"
medium_url: "https://medium.com/@olshansky/7-pocket-network-analogies-14aecd8086ed"
ShowToc: true
---

### 7 Pocket Network Analogies

_tl;dr Explaining what [Pocket Network](https://pokt.network/) is through a series of 7 internet networking analogies. Subscribe if you want to be notified of when we post about a series of 7 use-cases!_

### Table of Contents

- [7 Pocket Network Analogies](#7-pocket-network-analogies)
- [Table of Contents](#table-of-contents)
- [The Power of Analogies](#the-power-of-analogies)
- [Relay Mining — An Incentive for Network Requests](#relay-mining--an-incentive-for-network-requests)
- [Open Systems Interconnection (OSI) Analogies](#open-systems-interconnection-osi-analogies)
- [7. Application Layer: Uber for Network Requests](#7-application-layer-uber-for-network-requests)
- [6. Presentation Layer: Decentralized Routing](#6-presentation-layer-decentralized-routing)
- [5. Session Layer: Permissionless Digital Highway Toll System](#5-session-layer-permissionless-digital-highway-toll-system)
- [4. Transportation Layer: Incentivized TCP/IP](#4-transportation-layer-incentivized-tcpip)
- [3. Network Layer: Multi-Tenant Rate Limiting](#3-network-layer-multi-tenant-rate-limiting)
- [2. Data Link Layer: Verifiable On-Chain Counter](#2-data-link-layer-verifiable-on-chain-counter)
- [1. Physical Layer: Backbone of Permissionless ISPs](#1-physical-layer-backbone-of-permissionless-isps)

### The Power of Analogies

Everyone knows the ability to _ELI5 (Explain Like I'm Five)_ is critical, but it's one of those things that's much easier said than done.

I bet that if Einstein were around today, he'd have a very popular YouTube video titled: _"ELI5 — General Relativity"_.

![Einstein would have had a popular YouTube channel](/images/posts/7-pocket-network-analogies-image-01.jpeg)

For the sake of discussion, let's assume you succeed and a 5-year-old (or a friend's 5-year-old in my case) understands what you're working on.

In reality, to make something happen, you'll most likely need to work with someone older than 5, putting aside any potential time-dilation situations.

This is when analogies become really useful in addition to explaining things simply. It enables you to tap into pre-existing neural connections the other individual has rather than helping them build new ones. The latter requires a lot of deliberate cognitive effort.

Something I've learnt over the past couple of years is that one good analogy may not always be enough. You should aim to have multiple analogies in your back pocket. Different people have different experiences, so depending on whom you speak to, and when, you may need to pull out a different analogy.

It's like going into a Pokemon battle. You have a bunch of Pokemon of different types. If you're up against a 🔥 type, you need to take out your 💧type. If you're up against a 🌿 type, you need to bring out your 🔥 type. _#CharizardForLife_

![Pokemon battle analogy - different types for different situations](/images/posts/7-pocket-network-analogies-image-02.jpeg)

### Relay Mining — An Incentive for Network Requests

A couple of months ago, I presented [Relay Mining](https://arxiv.org/abs/2305.10672) at EthCC. If you missed it, you can find a recording at [ethcc.io](https://ethcc.io/archives/relay-mining-cryptographically-incentivizing-non-validating-nodes), on [YouTube](https://youtu.be/UoUslw_v__c?si=Ko9xFrH3jutym-F5&t=967), or my annotated presentation [here](https://olshansky.substack.com/p/annotated-presentation-relay-mining).

Over the past few weeks, I've found myself referencing one of the slides on multiple occasions. It comes up in various calls when I need to explain what [pokt.network](https://pokt.network/) is.

I thought it'd be fun to decompose it into multiple parts and create an online artifact I could reference.

**If any of these resonate, or you see value in integrating it into your product or service, my DMs are open or leave a comment below!**

![7 OSI Layer Analogies Overview Slide](/images/posts/7-pocket-network-analogies-image-03.png)

### Open Systems Interconnection (OSI) Analogies

Since we're dealing with networking protocols, I decided to use the [OSI Model](https://en.wikipedia.org/wiki/OSI_model) and draw a different analogy to every layer.

In case you're unfamiliar with the OSI model, it was made by the [International Organization for Standardization](https://www.iso.org/home.html) to conceptualize the different layers of how computers communicate over the internet.

![OSI Model 7 Layers Diagram](/images/posts/7-pocket-network-analogies-image-04.png)
_[https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)_

### 7. Application Layer: Uber for Network Requests

> Human-computer interaction layer, where applications can access the network services.

The Application Layer is where services interact with Pocket Network to provide data to end-users, bots, or other applications.

Just as Uber connects drivers with riders through a platform, Pocket aggregates decentralized open-source data & service providers and connects them to users through a permissionless protocol.

Put simply, Uber aggregates a lot of different **Drivers,** connects them with **Riders,** and facilitates all the interactions in the middle.

![Uber Model - Drivers, Riders, Platform](/images/posts/7-pocket-network-analogies-image-05.png)
_Aggregated Drivers (left) providing rides for Riders (right) via Uber (middle)_

Similarly, Pocket Network aggregates a lot of different **Open Source Data/Service Providers**, connects with **Users/Applications** and facilitates all the interactions in the middle.

![Pocket Network Model - Service Providers, Users, Protocol](/images/posts/7-pocket-network-analogies-image-06.png)
_Aggregated Open Source Data/Service providers (left) responding to network requests for Users/Applications (right) via Pocket Network (middle)_

### 6. Presentation Layer: Decentralized Routing

> Ensures that data is in a usable format and is where data encryption occur

This is where routing takes place and where quality is checked to ensure the service provided is usable.

With the help of Gateways such as [Grove.city](https://grove.city/), Pocket helps **Route** the **Relay** request across a decentralized set of service providers.

There are tons of details we're omitting related to how we maintain a high quality of service, how we determine the set of participating providers, etc. The key point is that the request is routed correctly across a permissionless & decentralized set of providers.

![Grove and Pocket Network Routing Diagram](/images/posts/7-pocket-network-analogies-image-07.png)
_Grove & Pocket Network routing the iPhone Application's network request to one of the available providers while ensuring a response of high quality. The providers maintain servers that participate in Pocket Network but are not owned by Grove._

### 5. Session Layer: Permissionless Digital Highway Toll System

> Maintains connections and is responsible for controlling ports and sessions

In 1995, Bill Gates wrote about the _Information Superhighway_ in [_The Road Ahead_](https://en.wikipedia.org/wiki/The_Road_Ahead_%28Gates_book%29).

If you're reading this, you've likely driven on both **physical and digital highways** — some with tolls, some without.

On physical highways, **entry, exit, maintenance, and payments** are controlled by a central authority using proprietary infrastructure.

**But on digital highways, what if these toll systems were public and permissionless?** That opens the door to alternative roads, each offering services of varying qualities at different prices points on what you're willing to pay.

### 4. Transportation Layer: Incentivized TCP/IP

> Transmits data using transmission protocols including UDP & TCP

Transmission Control Protocol (TCP) is one of the foundational protocols atop of which all internet protocols run. After a handshake between the Client and the Server is complete, we have a channel to reliably transfer **Data**.

However, in the same way that the adoption _internet-native money_ is slowly growing, there will likely exist a mechanism to pay for _internet-native data transfer_.

What if there were a way for Clients to pay Servers based on the amount of Data transfered regardless of what the application on top of it is?

![TCP Handshake with Payment Flow](/images/posts/7-pocket-network-analogies-image-08.jpeg)
_TCP handshake + Data Transfer + Payment using the $POKT token. Original image (before modification) can be found [here](https://www.netburner.com/learn/tcp-vs-udp-battle-of-the-protocols/)._

### 3. Network Layer: Multi-Tenant Rate Limiting

> Decides which physical path the data will take

Rate limiting is a strategy that cloud providers use to cap the number of requests an application can send to a server to avoid abusing it. You may have heard of [Denial-of-Service (DoS) attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack), which is a related concept.

This is technically "a solved problem", but is still a complex engineering endeavor for the hyperscalers. The key is that each of them has its own dedicated data centers (servers), so they can leverage solutions involving centralized (self-owned) databases.

For permissionless & decentralized networks, the same tactics don't apply directly. The servers on the backend are shared but the entrypoints (gateways) that the applications communicate with are independent. To coordinate amongst these different entrypoints, there needs to be a shared protocol to count and pay for the number of requests.

To visualize this, you can see entrypoints (gateways) that work operate along side the protocol to share cloud resources versus major cloud providers that have their own. Neither is necessarily better, but both involve hard tradeoffs; that topic is outside the scope of this blog post though.

![Decentralized vs Centralized Infrastructure Comparison](/images/posts/7-pocket-network-analogies-image-09.png)
_[liquify.io](https://www.liquify.io/) and [grove.city](https://grove.city/) (top half) using [pokt.network](https://pokt.network/) versus AWS & GCP (bottom half) maintaining their own dedicated server fleets._

### 2. Data Link Layer: Verifiable On-Chain Counter

> Defines the format of data on the network

In the same way that some (including Satoshi) refer to "_Bitcoin as just a timestamp server_", Pocket Network can be seen as a _"Verifiable Permissionless On-Chain Counter."_

![Bitcoin Whitepaper Quote about Timestamp Server](/images/posts/7-pocket-network-analogies-image-10.png)
_[https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)_

A lot of magic goes behind the scenes to enable this, but if you're one of the 🤓 reading this, I'll throw out all the buzzwords that make this happen: _It's a dynamically scalable, closed, self-modulating system using non-interactive probabilistic fraud-proofs for verification, leveraging on-chain commit-and-reveal schemes with crypto-economic incentive alignment._

**Details aside, doesn't everyone need a counter?** If it's a network request, we can count it. What if you could get the number of clicks your advertisement got from a public database rather than Google's dashboard?

The following table shows a public database (i.e. a Distributed Ledger) where anyone can read the number of requests served (e.g. server 2 served 42 requests) with the assurance that the number cannot be forged.

![Public Verifiable Counter Database](/images/posts/7-pocket-network-analogies-image-11.png)
_A verifiable public counter that anyone can read from_

### 1. Physical Layer: Backbone of Permissionless ISPs

> Transmits raw bit stream over the physical medium

A few decades ago, becoming a content creator was nearly impossible. You'd either need a lot of upfront capital to build a media empire or have the right connections so you can schmooze your way through. Today, it's basically free with almost no barrier to entry.

In the same way, all network requests currently flow through Internet Service Providers (ISPs). Becoming an ISP is nearly impossible. You'd either need a lot of upfront capital or have the right connections so you can schmooze your way through. In the distant future, there could be a world where it could be free with almost no barrier to entry.

This idea is inspired by one of [Naval's famous sayings](https://www.navalmanack.com/almanack-of-naval-ravikant/find-a-position-of-leverage):

> The final form of leverage is brand new — the most democratic form. It is: "**products with no marginal cost of replication.**"
>
> This includes books, media, movies, and code. Code is probably the most powerful form of permissionless leverage. All you need is a computer — you don't need anyone's permission. [1]

Creating the **Information Rails for Web3** is an ambitious long-term goal that may take decades, requiring dozens of leaps of faiths along the way. But, the technical value proposition of protocols like Pocket Network and many others play a necessary role to make it happen.

I'll leave this thread off with one of my own quotes:

> Decentralization is not the goal, it's a biproduct of incentive alignment and permissionless protocols.

![Final slide - Information Rails for Web3](/images/posts/7-pocket-network-analogies-image-12.png)
