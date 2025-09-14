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

### *tl;dr Explaining what [*Pocket Network*](https://pokt.network/) is through a series of 7 internet networking analogies. Subscribe if you want to be notified of when we post about a series of 7 use-cases!*

### Table of Contents

- [The Power of Analogies](#d6e0)
- [Relay Mining — An Incentive for Network Requests](#aabb)
- [Open Systems Interconnection (OSI) Analogies](#bef4)- 7. [Application Layer:](#978c) **Uber for Network Requests**- 6. [Presentation Layer:](#f83d) **Decentralized Routing**- 5. [Session Layer:](#68ee) **Permissionless Digital Highway Toll System**- 4. [Transportation Layer:](#b58e) **Incentivized TCP/IP**- 3. [Network Layer:](#c0ed) **Multi-Tenant Rate Limiting**- 2. [Data Link Layer:](#d6a7) **Verifiable On-Chain Counter**- 1. [Physical Layer:](#6a81) **Backbone of Permissionless ISPs**

### The Power of Analogies

Everyone knows the ability to ELI5 (Explain Like I’m Five)* is critical, but it’s one of those things that’s much easier said than done.

I bet that if Einstein were around today, he’d have a very popular YouTube video titled: *“ELI5 — General Relativity”.

For the sake of discussion, let’s assume you succeed and a 5-year-old (or a friend’s 5-year-old in my case) understands what you’re working on.

In reality, to make something happen, you’ll most likely need to work with someone older than 5, putting aside any potential time-dilation situations.

This is when analogies become really useful in addition to explaining things simply. It enables you to tap into pre-existing neural connections the other individual has rather than helping them build new ones. The latter requires a lot of deliberate cognitive effort.

Something I’ve learnt over the past couple of years is that one good analogy may not always be enough. You should aim to have multiple analogies in your back pocket. Different people have different experiences, so depending on whom you speak to, and when, you may need to pull out a different analogy.

It’s like going into a Pokemon battle. You have a bunch of Pokemon of different types. If you’re up against a 🔥 type, you need to take out your 💧type. If you’re up against a 🌿 type, you need to bring out your 🔥 type. *#CharizardForLife*

### Relay Mining — An Incentive for Network Requests

A couple of months ago, I presented [Relay Mining](https://arxiv.org/abs/2305.10672) at EthCC. If you missed it, you can find a recording at [ethcc.io](https://ethcc.io/archives/relay-mining-cryptographically-incentivizing-non-validating-nodes), on [YouTube](https://youtu.be/UoUslw_v__c?si=Ko9xFrH3jutym-F5&t=967), or my annotated presentation [here](https://olshansky.substack.com/p/annotated-presentation-relay-mining).

Over the past few weeks, I’ve found myself referencing one of the slides on multiple occasions. It comes up in various calls when I need to explain what [pokt.network](https://pokt.network/) is.

I thought it’d be fun to decompose it into multiple parts and create an online artifact I could reference.

**If any of these resonate, or you see value in integrating it into your product or service, my DMs are open or leave a comment below!**

### Open Systems Interconnection (OSI) Analogies

Since we’re dealing with networking protocols, I decided to use the [OSI Model](https://en.wikipedia.org/wiki/OSI_model) and draw a different analogy to every layer.

### In case you’re unfamiliar with the OSI model, it was made by the [International Organization for Standardization](https://www.iso.org/home.html) to conceptualize the different layers of how computers communicate over the internet.[https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)

### 7. Application Layer: Uber for Network Requests

Human-computer interaction layer, where applications can access the network services.

The Application Layer is where services interact with Pocket Network to provide data to end-users, bots, or other applications.

Just as Uber connects drivers with riders through a platform, Pocket aggregates decentralized open-source data & service providers and connects them to users through a permissionless protocol.

Put simply, Uber aggregates a lot of different **Drivers, **connects them with **Riders, **and facilitates all the interactions in the middle.

Aggregated Drivers (left) providing rides for Riders (right) via Uber (middle)

Similarly, Pocket Network aggregates a lot of different **Open Source Data/Service Providers**, connects with **Users/Applications** and facilitates all the interactions in the middle.

### Aggregated Open Source Data/Service providers (left) responding to network requests for Users/Applications (right) via Pocket Network (middle)

### 6. Presentation Layer: Decentralized Routing

Ensures that data is in a usable format and is where data encryption occur

This is where routing takes place and where quality is checked to ensure the service provided is usable.

With the help of Gateways such as [Grove.city](https://grove.city/), Pocket helps **Route** the **Relay** request across a decentralized set of service providers.

There are tons of details we’re omitting related to how we maintain a high quality of service, how we determine the set of participating providers, etc. The key point is that the request is routed correctly across a permissionless & decentralized set of providers.

### Grove & Pocket Network routing the iPhone Application’s network request to one of the available providers while ensuring a response of high quality. The providers maintain servers that participate in Pocket Network but are not owned by Grove.

### 5. Session Layer: Permissionless Digital Highway Toll System

Maintains connections and is responsible for controlling ports and sessions

In 1995, Bill Gates wrote about the Information Superhighway* in [*The Road Ahead](https://en.wikipedia.org/wiki/The_Road_Ahead_%28Gates_book%29)*.*

If you’re reading this, you’ve likely driven on both **physical and digital highways** — some with tolls, some without.

On physical highways, **entry, exit, maintenance, and payments** are controlled by a central authority using proprietary infrastructure.

**But on digital highways, what if these toll systems were public and permissionless?** That opens the door to alternative roads, each offering services of varying qualities at different prices points on what you’re willing to pay.

### 4. Transportation Layer: Incentivized TCP/IP

Transmits data using transmission protocols including UDP & TCP

Transmission Control Protocol (TCP) is one of the foundational protocols atop of which all internet protocols run. After a handshake between the Client and the Server is complete, we have a channel to reliably transfer **Data**.

However, in the same way that the adoption internet-native money* is slowly growing, there will likely exist a mechanism to pay for *internet-native data transfer.

What if there were a way for Clients to pay Servers based on the amount of Data transfered regardless of what the application on top of it is?

### TCP handshake + Data Transfer + Payment using the $POKT token. Original image (before modification) can be found [here](https://www.netburner.com/learn/tcp-vs-udp-battle-of-the-protocols/).

### 3. Network Layer: Multi-Tenant Rate Limiting

Decides which physical path the data will take

Rate limiting is a strategy that cloud providers use to cap the number of requests an application can send to a server to avoid abusing it. You may have heard of [Denial-of-Service (DoS) attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack), which is a related concept.

This is technically “a solved problem”, but is still a complex engineering endeavor for the hyperscalers. The key is that each of them has its own dedicated data centers (servers), so they can leverage solutions involving centralized (self-owned) databases.

For permissionless & decentralized networks, the same tactics don’t apply directly. The servers on the backend are shared but the entrypoints (gateways) that the applications communicate with are independent. To coordinate amongst these different entrypoints, there needs to be a shared protocol to count and pay for the number of requests.

To visualize this, you can see entrypoints (gateways) that work operate along side the protocol to share cloud resources versus major cloud providers that have their own. Neither is necessarily better, but both involve hard tradeoffs; that topic is outside the scope of this blog post though.

### [liquify.io](https://www.liquify.io/) and [grove.city](https://grove.city/) (top half) using [pokt.network](https://pokt.network/) versus AWS & GCP (bottom half) maintaining their own dedicated server fleets.

### 2. Data Link Layer: Verifiable On-Chain Counter

Defines the format of data on the network

In the same way that some (including Satoshi) refer to “*Bitcoin as just a timestamp server*”, Pocket Network can be seen as a “Verifiable Permissionless On-Chain Counter.”*

[https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)

A lot of magic goes behind the scenes to enable this, but if you’re one of the 🤓 reading this, I’ll throw out all the buzzwords that make this happen: *It’s a dynamically scalable, closed, self-modulating system using non-interactive probabilistic fraud-proofs for verification, leveraging on-chain commit-and-reveal schemes with crypto-economic incentive alignment.

**Details aside, doesn’t everyone need a counter?** If it’s a network request, we can count it. What if you could get the number of clicks your advertisement got from a public database rather than Google’s dashboard?

The following table shows a public database (i.e. a Distributed Ledger) where anyone can read the number of requests served (e.g. server 2 served 42 requests) with the assurance that the number cannot be forged.

### A verifiable public counter that anyone can read from

### 1. Physical Layer: Backbone of Permissionless ISPs

Transmits raw bit stream over the physical medium

A few decades ago, becoming a content creator was nearly impossible. You’d either need a lot of upfront capital to build a media empire or have the right connections so you can schmooze your way through. Today, it’s basically free with almost no barrier to entry.

In the same way, all network requests currently flow through Internet Service Providers (ISPs). Becoming an ISP is nearly impossible. You’d either need a lot of upfront capital or have the right connections so you can schmooze your way through. In the distant future, there could be a world where it could be free with almost no barrier to entry.

This idea is inspired by one of [Naval’s famous sayings](https://www.navalmanack.com/almanack-of-naval-ravikant/find-a-position-of-leverage):The final form of leverage is brand new — the most democratic form. It is: “**products with no marginal cost of replication.”**This includes books, media, movies, and code. Code is probably the most powerful form of permissionless leverage. All you need is a computer — you don’t need anyone’s permission. [1]

Creating the **Information Rails for Web3** is an ambitious long-term goal that may take decades, requiring dozens of leaps of faiths along the way. But, the technical value proposition of protocols like Pocket Network and many others play a necessary role to make it happen.

I’ll leave this thread off with one of my own quotes:

Decentralization is not the goal, it’s a biproduct of incentive alignment and permissionless protocols.
