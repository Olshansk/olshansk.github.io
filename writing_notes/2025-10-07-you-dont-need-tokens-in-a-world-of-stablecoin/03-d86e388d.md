---
title: "Your Blockchain Doesn't Need A Token"
date: 2025-10-08T11:35:15-0700
draft: false
description: ""
tags: ["blockchain", "token", "crypto", "pocket"]
categories: []
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

Rough notes for the update:

- https://x.com/paramonoww/status/1975575772971573437?utm_source=tldrcrypto
- Add a note on USDC being enough
- Add a note on it giving us the security we need
- Part of security is governance, we don't need anything else there
- Add USDC market cap to the table below: https://threadreaderapp.com/thread/1974983137458639182.html?utm_source=tldrcrypto
- Buybacks are how you handle tokenomics
- Start with a stablecoin, figure out what works, and then add a token. Similar to what polymarket is doing.
- Hyperliquid is a great example of a team that seemed to figure it out quickly.

--

A couple of weeks ago I [posted some thoughts](https://olshansky.info/posts/2025-09-19-clarity-trilemma) after looking through the [CLARITY act](https://www.congress.gov/bill/119th-congress/house-bill/3633/text).

## Blockchain Use Cases

I was thinking about it again and am coming to the conclusion that while we do need the [Distributed Ledger Technology](https://en.wikipedia.org/wiki/Distributed_ledger) blockchains enable, the majority (not all) of crypto projects do not need their own token.

![token needs](../../static/img/token_needs.png)

The token for a particular blockchain (i.e. L1) or project (i.e. L2+) can be reduced to three primary use-cases:

1. **Security** - Prevent malicious changes to the distributed ledger.
2. **Utility** - Create net new utility to users of the blockchain.
3. **ROI** - Provide network stakeholders with a return on investment; investors, operators, etc.

The industry is still in its discovery phase, so I'll briefly outline my thinking as of today.

### Security

This is either about incentives or distinctiveness with `Bitcoin` and `Ethereum` as the gold standards.

| Feature                 | Bitcoin                                   | Ethereum                             |
| ----------------------- | ----------------------------------------- | ------------------------------------ |
| **Consensus Mechanism** | Proof-of-Work                             | Proof-of-Stake                       |
| **Capital Commitment**  | Invest money in infrastructure            | Put some money in escrow             |
| **Behavior Incentives** | You don’t earn anything for poor behavior | Your money is burnt if you misbehave |
| **Market Cap**          | $2T+                                      | $500B+                               |

1. Put some money in escrow

Bitcoin:

- Proof-of-Work
- Invest money in infrastructure & maintenance
- You don't earn anything for poor performancne
- Market cap: $2T+

Ethereum:

- Proof-of-Stake
- Put some money in escrow
- Your money is burn for adverserial behavior
- Market cap: $500B+

Stablecoin:

- Proof-of-Stake + Proof of Reserve
- Put money in escrow
- Your money is taken for adverserial behavior
- Market cap: Reserve currency of choice

We have two "special" chains that can solve this problem across the board: `Bitcoin` and `Ethereum`.

With market capitalization in the trillions, and hundreds of billions, respectively, the [Deterrence theory](https://en.wikipedia.org/wiki/Deterrence_theory) is in full effect. They are too big and expensive to attack.

If someone has the capital to attack a small chain (e.g. < $100M), it is likely not worth their time. Once it is worth their time, the capital requirements are too large.

We have projects like [EigenLayer](http://eigenlayer.xyz/) and [Babylon](https://babylonlabs.io/) that enable
leveraging `BTC` and `ETH` for other projects.

We can assume this problem is solved unless you're doing some very different.

Since most blockchains are Proof-of-Stake, we can either use `BTC, `ETH`, or `USDC` for security.

### Utility

This part is still being played out, but it seems like fast settlement for payments and trading is where things are settling.

The business model for these use-cases are fees in the range of 1-2% of the value transacted.

This is no different than how most neo-banks, credit card issuers and others payments processors (e.g. Stripe) work today.

More efficient way to skin the same cat.

Most blockchains tout their token can be used for paying for the utility provided by the network

But, why not stablecoins? Then, you don't have to worry about conversation or fluctuations in value.

The utility will be indpendent of marketing or factors

### ROI

Speculation and memes have their place in this industry, similar to how gambling has it's place.

But, I'd argue this is not long

## Stablecoins solving all of the above

Putting aside geopolitical risks, Stablecoins solve all of the above.
