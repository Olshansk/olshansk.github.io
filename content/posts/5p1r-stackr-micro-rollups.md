+++
author = "Daniel Olshansky"
title = "5P;1R Stackr: Micro-Rollups"
date = "2024-04-04T19:53:25.578Z"
description = "Modular Micro-Services for Web3 (build app-specific rollups on Ethereum in web2 programming languages)"
tags = [
    "crypto", "ai", "startup", "tech", "research", "productivity"
]
substack_url = "https://olshansky.substack.com/p/5p1r-stackr-micro-rollups"
+++

_This is a post in a series of articles I’m writing called “5 points & 1 resource” (think tl;dr but 5p;1r), where I summarize a list of 5 concepts that would have helped me start learning or re-learning a certain topic. It is intentionally far from a complete source of data._

_Edit: Thank you to [Kautuk](https://twitter.com/Kautukkundan) (founder of Stackr ) for reviewing this post._

---

- Micro-rollups (MRUs) are the answer to **_“a blockchain is too slow and expensive”_** for my use case, but **_“I still want some eventual Web3 security guarantees”_** in progressively porting a Web2 app to Web3.

- Micro-rollups can be seen through different lenses for different stakeholders:

**As a smart contract developer**, it is akin to writing a smart contract unconstrained to a specific blockchain, execution or development environment.

- **As a DevOps engineer**, it is similar to deploying a serverless functions whose inputs are user Actions and outputs are state transitions on L1 or L2 blockchains.

- **As a member of society**, is it like an external procedure (e.g. a tax audit) involving various parties that eventually settles on a shared system (e.g. a bank).

- **Stackr is a framework that enables modularity across the entire stack**. This ranges from the selection of a Data Availability network, proof & verification mechanisms, execution environments, sequencing architecture, settlement requirements, app-specific frameworks and more.

- **Security is a spectrum of tradeoffs that can be customized based on the app's needs**. User Actions are Acknowledged (C0), Batched (C1), Verified (C2), Finalized (C3) and ultimately Settled (C4), which range from milliseconds, seconds, minutes, hours and days, respectively.

- **The verification layer, Vulcan, creates a permissionless marketplace that is proof-type agnostic; **fraud/validity or optimistic/pessimistic/ZK. Centralized and permissioned applications enable a smooth onboarding transition for the Web2 ecosystem. They are enabled by a decentralized and permissionless set of auditors with a financial incentive to compete in increasing the security of an app’s state transition.

The best reference is (obviously) the [Stackr whitepaper itself](http://litepaper.stf.xyz).
