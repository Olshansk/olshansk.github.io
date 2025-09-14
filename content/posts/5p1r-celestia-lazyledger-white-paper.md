+++
author = "Daniel Olshansky"
title = "5P;1R - Celestia (LazyLedger) White Paper"
date = "2022-08-13T20:31:57.446Z"
description = ""
tags = [
    "crypto", "ai", "tech", "research", "productivity", "book"
]
substack_url = "https://olshansky.substack.com/p/5p1r-celestia-lazyledger-white-paper"
+++

*This is a post in a series of articles I’m writing called “5 points & 1 resource” (think tl;dr but 5p;1r), where I summarize a list of 5 concepts that would have helped me start learning or re-learning a certain topic. It is intentionally far from a complete source of data.*

---

- Celestia decouples transaction **consensus** and **execution** by splitting the responsibilities between Celestia (i.e. the core network) and other blockchains (i.e. clients/applications) built on top of it like so:
• **Celestia:** transaction **ordering **&** availability**
• **Client:** transaction **validation** & **execution**

- The **Data Availability Problem** (a guarantee to clients that block data is available) leverages **erasure encoding **and** probabilistic random sampling** to balance the tradeoff between network bandwidth costs and data availability guarantees. Specifically, if a message is extended to *n shares*, and more than *ᵏ⁄ₙ shares* are witheld by an adversarial block producer, a client sampling a **single missed share** can assume, with high confidence, that the block is unavailable.

- Client nodes (i.e. blockchains/applications) can be implemented using **any language** on top of **any execution environment** and are responsible for managing their own **state transition business logic** by querying storage, while Celestia is responsible for preventing DoS attacks by collecting fees from each included transaction.

- Using **2D Reed-Solomon** erasure encoding and assuming a **block of size N**, the bandwidth complexity of verifying block availability is either:
• ***O(N)*** — the whole block plus a single Merkle root are downloaded for a 100% data availability guarantee.
**• *****O( √ N+log(√ N))***** **— a single row or a single column plus ***2√(N)*** Merkle roots need to be downloaded for a sub-maximal guarantee. **For example**, with a code rate of *¼* and *4096 shares*, only *0.4%* of the block (*15 shares*) need to be downloaded to achieve *99% confidence* that the block is available. This means that increasing the block size and network throughput can be securely achieved by increasing the number of nodes that make sampling requests for block shares.

- The Celestia network uses a namespaced and ordered Merkle Tree with a 1:1 relationship between applications and namespace IDs, enabling applications to query for transactions associated only with their namespace ID. The hash of each non-leaf node is ***left||right*** where left is ***leftMinNs||leftMaxNs||hash(x)*** and right is ***rightMinNs||rightMaxNs||hash(x)***, meaning that the node value can be used to determine the range of namespaces the subtree holds messages for.

---
There’s no better reference than the original white paper: [LazyLedger: A Distributed Data Availability Ledger With Client-Side Smart Contracts](https://arxiv.org/pdf/1905.09274.pdf), but personally, I’d use my annotated version of the available at ipfs://bafybeibbxdsdzf5v7jdm7ak5opdtw3vf35nb37wldkyokwbhmvdzflwsry or [s3.olshansky.info/CelestiaWhitePaperReviewSmall.pdf](http://s3.olshansky.info/CelestiaWhitePaperReviewSmall.pdf).

---
*Source: [https://arxiv.org/pdf/1905.09274.pdf](https://arxiv.org/pdf/1905.09274.pdf)*Thanks for reading Olshansky's Newsletter! Subscribe for free to receive new posts and support my work.