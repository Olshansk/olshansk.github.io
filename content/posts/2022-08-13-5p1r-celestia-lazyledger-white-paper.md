---
title: "5P;1R — Celestia (LazyLedger) White Paper"
date: 2022-08-13T20:30:40-07:00
draft: false
description: "This is a post in a series of articles I’m writing called “5 points & 1 resource” (think tl;dr but 5p;1r), where I summarize a list of…"
tags: ['celestia', 'lazyledger', 'white']
categories: ['cryptocurrency', 'technology', 'machine-learning', 'business']
medium_url: "https://medium.com/@olshansky/5p-1r-celestia-lazyledger-white-paper-9915e83a079b"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

### 5P;1R — Celestia (LazyLedger) White Paper

 _This is a post in a series of articles I’m writing called “5 points & 1 resource” (think tl;dr but 5p;1r), where I summarize a list of bullet points that would have helped me start learning or re-learning a certain topic. It is intentionally far from a complete source of data._
1.
Celestia decouples transaction **consensus** and **execution** by splitting the responsibilities between Celestia (i.e. the core network) and other blockchains (i.e. clients/applications) built on top of it like so:
• **Celestia:** transaction **ordering** &**availability**
• **Client:** transaction **validation** & **execution**
2.
The **Data Availability Problem** (a guarantee to clients that block data is available) leverages **erasure encoding** and**probabilistic random sampling** to balance the tradeoff between network bandwidth costs and data availability guarantees. Specifically, if a message is extended to _n shares_ , and more than _ᵏ⁄ₙ shares_ are witheld by an adversarial block producer, a client sampling a **single missed share** can assume, with high confidence, that the block is unavailable.
3.
Client nodes (i.e. blockchains/applications) can be implemented using **any language** on top of **any execution environment** and are responsible for managing their own **state transition business logic** by querying storage, while Celestia is responsible for preventing DoS attacks by collecting fees from each included transaction.
4.
Using **2D Reed-Solomon** erasure encoding and assuming a **block of size N** , the bandwidth complexity of verifying block availability is either:
• **_O(N)_** — the whole block plus a single Merkle root are downloaded for a 100% data availability guarantee.
**• _O( √ N+log(√ N))_ **— a single row or a single column plus **_2√(N)_** Merkle roots need to be downloaded for a sub-maximal guarantee. **For example** , with a code rate of _¼_ and _4096 shares_ , only _0.4%_ of the block (_15 shares_) need to be downloaded to achieve _99% confidence_ that the block is available. This means that increasing the block size and network throughput can be securely achieved by increasing the number of nodes that make sampling requests for block shares.
5.
The Celestia network uses a namespaced and ordered Merkle Tree with a 1:1 relationship between applications and namespace IDs, enabling applications to query for transactions associated only with their namespace ID. The hash of each non-leaf node is **_left||right_** where left is **_leftMinNs||leftMaxNs||hash(x)_** and right is **_rightMinNs||rightMaxNs||hash(x)_** , meaning that the node value can be used to determine the range of namespaces the subtree holds messages for.

There’s no better reference than the original white paper: [LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts](https://arxiv.org/pdf/1905.09274.pdf), but personally, I’d use my annotated version of the available at ipfs://bafybeibbxdsdzf5v7jdm7ak5opdtw3vf35nb37wldkyokwbhmvdzflwsry or [s3.olshansky.info/CelestiaWhitePaperReviewSmall.pdf](http://s3.olshansky.info/CelestiaWhitePaperReviewSmall.pdf).

![](/images/posts/2022-08-13-5p1r-celestia-lazyledger-white-paper-image-01.png)![](/images/posts/2022-08-13-5p1r-celestia-lazyledger-white-paper-image-02.png)_Source:_[_https://arxiv.org/pdf/1905.09274.pdf_](https://arxiv.org/pdf/1905.09274.pdf)