---
title: "The Missing Key to x402"
date: 2026-04-13T12:38:32-0700
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

What's the point I want to make?

- A lot of companies are saying they're building protocols, but they're usually just APIs, SDKs or opinionated workflows disguised as "open protocols"
- x402 is awesome. It is a real neutral API.
- Linux foundation

How will we make this point?

- MCP, A2A, etc didn't get adopted
- x402 is simple

What's missing?

- It's too "pure" and there are A LOT of companies that work around API keys and

API Marketplace:

- https://x.com/stripe/status/2037197998074335292
- We tried to build it at Pocket network using a permissionless rate limiting layer (you can read the paper if you want to)

---

> isnt the idea of these protocols that you dont need API keys?

- Link to x402 whitepaper
- Link to cloudflare comments on x402
- Link to stripe's MCP
- Talk about sessions and state channels

- TCP won because it was simple
- API keys are easy
- JWTs enable sessions

- When you've been deep in "real crypto", you learn that the pure solution doesn't work

Giving keys to agents is necessary, but a lot of the problems we've seen up until now will come back:

- Hot keys?
- Cold keys?
- Multisig
- Social recovery
- Etc...

There are existing primitives to solve this:

- Embedded wallets
- Server wallets
- Smart wallets

https://x.com/olshansky/status/2037253629711966525?s=20
https://developers.cloudflare.com/agents/agentic-payments/mpp/
https://www.x402.org/
https://www.linuxfoundation.org/x402foundation
https://docs.stripe.com/payments/machine/x402
