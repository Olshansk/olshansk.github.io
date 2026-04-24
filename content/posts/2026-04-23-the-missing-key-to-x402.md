---
title: "The Missing Key to x402"
date: 2026-04-23T12:38:32-0700
draft: false
description: "x402 is the right base layer. The missing piece is a practical key and session story that makes it shippable."
tags: ["x402", "MPP", "Payments", "Protocols"]
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

The missing base layer to internet-native payments was x402. It's here, and [as of 04/02](https://x.com/coinbase/status/2039689438922522728), it's part of the [Linux Foundation](https://www.linuxfoundation.org/x402foundation).

But, it's missing one key piece to unlock the whole puzzle: **A key management systemon top of the base layer**.

## What is x402?

[x402 is an open protocol](https://www.x402.org/) that builds on top of a more than twenty year old IETF standard: [HTTP's 402 Payment Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402) status code.

x402 is good because it is boring in the right way. It is simple, neutral, and very easy to explain.

The [whitepaper’s pitch](https://x402.org/whitepaper) is straightforward:

> Enable machine-native processes (e.g. AI agents, Web Services, etc.) to autonomously pay for API access, data, and digital services by leveraging the HTTP 402 ”Payment Required” and internet-native payment rails (e.g. stablecoins, blockchains, etc.).

Having spent years deep in the crypto industry, one of the most important lessons I learnt is that **simple protocols get adopted, while overdesigned protocols get discussed**. That is the tradeoff. In my opinion, it's why Bitcoin took off. It remains one of the most [approacble whitepapers](https://bitcoin.org/bitcoin.pdf) I've ever read. Just re-read it a handful of times and you'll undersand it.

_In fact, I see a world where PayPal could have come up with either or both of x402 and Bitcoin, but for now, let's get back on track..._

## How does x402 work?

The full x402 story is very easy to explain:

1. A client asks for a resource; _such as a PDF_.
2. The server replies `402 Payment Required`; _including a price and a destination address for payment_.
3. The client pays; _along with the crypto digital equivalent of a signed check_.
4. The server returns the resource; _after validating and setting the check_.

That is the perfect base layer. It can't be any simpler.

However, in the same way that the [OSI Model](https://en.wikipedia.org/wiki/OSI_model) needed a mature and ever-evolving **Application Layer** on top of the **Transport Layer**, x402 will need a mature and ever-evolving **Key Management Layer** on top of the **Payment Layer**.

The [last page](https://www.x402.org/x402-whitepaper.pdf) of the x402 whitepaper touts the following benefits:

- Instant, low-cost transactions.
- No API keys, no subscriptions, no middlemen.
- AI-first, developer-friendly, and blockchain-agnostic.

## So what is x402 Missing?

Something I've learnt in the world of software development is that rewrites almost never work. You have to meet the world where it is, integrate with existing systems, and incrementally build towards the future you want to see. That is the only way to get from _"this works on paper"_ to _"this works in production."_

It's been decades, and we still haven't [reached 50% IPv6 adoption](https://www.google.com/intl/en/ipv6/statistics.html) as of writing this post.

If you want this to work in real systems, you need to account for how existing systems work, including things like:

- Scoped access keys
- Sessions keys
- Rotation and revocation of keys
- Admin key management

Then, the moment you enter the world of crypto, you learn that "custody hot keys" is a setup for a nightmare. You start to learn about multi-sig, hardware wallets, ring signatures, and we haven't even gotten started with smart contracts.

## What does it look like?

The missing key to the puzzle is not a change to the protocol, but building infrastructure on top of it that makes it usable where the world is today, not where it's going to be.

In fact, I really that the protocol stay small and simple. It enables the ecosystem to introduce small, composable, layered primitives. I anticipate the OSI model will need to get updated soon.

<img src="/images/posts/2026-04-23-the-missing-key-to-x402-handshake.jpeg" alt="x402 API key handshake showing payment required, signed transaction verification, and then authenticated API access" style="max-width: 100%; border-radius: 12px;" />

**What's the takeaway?** In addition to enabling permissionless purchase of resources on the internet, enabling permissionless purchase of API keys is the next logical step. It is the missing piece that turns a one-off payment into an ongoing relationship with existing service.

It doesn't feel as "pure", but it works. Keys are not a cop-out. They are the mechanism that turns a payment event into an ongoing service relationship.

This enables lots of different paradigms:

- **Authentication**: Authenticate without processing payments with every call
- **Authorize**: Scope access instead of giving away the whole kitchen
- **Rotate/Revoke**: Rotate or revoke access without redesigning the protocol
- **Integrate**: Enable payments and top ups in the same way that you manage balances in existing services

Buying keys with x402 doesn't have to be limited to API Keys. This could extend to session keys, license keys, support JWTs, or even just a more traditional pay-per-use model. The point is that the key management layer is what turns the protocol from a one-off payment into an ongoing relationship with a service.

Those are the boring parts that make a system shippable. And boring is good here.

## How are others solving it?

First, what is the core problem of using off-the-shelf x402 for real systems? **Hyperscale**.

When you're servicing millions of requests per second, you can't go through a signature ceremony with every request. There's a long list of problems to solve including, but not limited, to, rate limiting requests, verifying payments, preventing abuse, protecting against denial-of-service, etc.

Two of the biggest efforts in the spaces targeting to solve this are:

- [Circle's Nonpayments Gateway](https://www.circle.com/nanopayments)
- [Stripe's Machine Payments Protocol (MPP)](https://docs.stripe.com/payments/machine/x402)

Circle has a very simple solution built on top of x402: batch thousands on nano transactions into one x402 transaction. It's not a new protocol, it's a [Gateway](<https://en.wikipedia.org/wiki/Gateway_(telecommunications)>) based approach to solving this problem.

Stripe has a more complex solution, also build on top of x402: [MPP](https://docs.stripe.com/payments/machine). It entangles the open layers of x402, along with a new protocol, full of features, with first-class support for it's [own blockchain](https://tempo.xyz/) and card network:

![Stripe supports machine payments across these networks.](/images/posts/2026-04-23-stripe-machine-payments.png)

This works, but the line between open protocol and a product offering gets blurry.

> x402 feels pure and neutral, like Bitcoin, Ethereum, or Zcash. MPP works, but feels bloated and blurs the line between an open protocol and a product offering.

One of the great things about MPP are [sessions](https://developers.cloudflare.com/agents/agentic-payments/mpp/#payment-intents): _"A streaming payment over a payment channel. Use for pay-as-you-go or per-token billing with sub-cent costs and sub-millisecond latency."_

I'd argue that in the same way that Cloudflare introduced [Pay Per Crawl](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/) as a product, and not a protocol, a lot of MPP could be an SDK on top of x402 as opposed to a protocol.

If you've been in the crypto indutry long enough, you've seen this many times.

## Where do we go from here?

We find a delicate balance between building, waiting, and seeing what is a real problem that needs solving.

It's clear that stablecoins are here to stay. It's clear that agents will become more prevalent on the internet. The key is to distinguish between signal and noise of where the market is today. The big players can keep funding these efforts in the same way that Meta continues to fund the _Metaverse_, but smaller companies need to follow the customer that comes back.

The key infrastructure layer I outlined above is how [Grove](www.grove.city) is built today. When we started, out thesis was that agents will pay humans. In reality, if you dive deep into [x402scan.com](https://www.x402scan.com/) or [agentic.market](https://agentic.market/), you'll find a lot of tinkering, but not a market. If we had visibility into the numbers behind [projects.dev](https://projects.dev/), I'm sure we'd find the same thing.

To summarize, I'm extremeley bullish on everything above. x402 will profolirate. MPP will be a great product. Agents will be consuming resources on the internet. I simply want to call out that in order to move the needle, we need to introduce layers that integrate the old system with the new, because it'll be a while. That is the missing key to x402.
