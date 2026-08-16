---
title: "The Bridge Between DeFi & TradFi"
date: 2026-03-13T10:12:46-0700
draft: false
description: "A 53-second demo of round-tripping between traditional banking and onchain, and why building it was way harder than it looks."
tags: ["DeFi", "TradFi", "Crypto", "Coinbase", "Base", "Grove"]
categories: ["Posts"]
ShowToc: false
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

_TL;DR: Round-tripping between TradFi and DeFi in under 2.5 minutes looks simple. Building it was one of the hardest things I've shipped._

## The Demo

Here's a 53-second video showing the future of finance.

It's the backbone technology [Grove](https://buildwithgrove.com) uses to ensure that high quality earns what it deserves.

Anywhere. Anytime. Anyone. Instantly. Keeping more of what you earn.

In less than 2.5 minutes, this showcases moving from traditional banking to [Base](https://base.org), moving money onchain, and then back to traditional banking.

It leverages many parts of the [Coinbase Developer Platform](https://www.coinbase.com/developer-platform), including auth, server wallets, embedded wallets, gas sponsorship, and much more.

<video controls width="100%">
  <source src="/videos/posts/the-bridge-between-defi-tradfi/grove_ramp.mov" type="video/mp4">
</video>

## Why This Was So Hard

If you watch the demo, it looks trivial.
Move money in, move money out.
A couple of button taps and some loading spinners.

It was anything but.

Every step in that flow touches a different system with different latency guarantees, different failure modes, and different consistency models.

- Bank ACH transfers settle in hours or days
- Onchain transactions settle in seconds
- Your product's database updates instantly
- The user expects the UX to feel instantaneous

You're stitching together systems that were never designed to talk to each other.
And the user doesn't care.
They just want to see the number go up.

## We Need a New Framework

If you've been doing software engineering for a while, you've probably come across the [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem), as well as the ACID and BASE frameworks.

These describe tradeoffs in distributed systems and databases.

We're going to need something similar to describe the bridge between TradFi and DeFi.

You need to account for consistency and latency across:

- Traditional banks and chains
- Onchain transactions
- Your product's data store
- A responsive (and optimistic) UX

Users don't want to wait 1 minute to see a balance update, even if that's what settlement actually takes.

SO MUCH is hidden in how money moves. On or offchain.

---

_Simple demos hide complex systems. The 53 seconds you see took months to build._
