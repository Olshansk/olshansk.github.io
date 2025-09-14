---
title: "5P;1R — Ethereum’s Modified Merkle Patricia Trie"
date: 2022-04-23T15:31:50-07:00
draft: false
description: "This is the second of a series of articles I’m trying out called “5 points & 1 resource” (think tl;dr but 5p;1r) where I summarize a list…"
tags: ["ethereum", "modified", "merkle"]
categories: ["cryptocurrency", "technology", "machine-learning"]
medium_url: "https://medium.com/@olshansky/5p-1r-ethereums-modified-merkle-patricia-trie-6956f5888398"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

### 5P;1R — Ethereum’s Modified Merkle Patricia Trie

This is the second of a series of articles I’m trying out called “ _5 points & 1 resource_” (think tl;dr but 5p;1r) where I summarize a list of bullet points that would have helped me start learning a new topic. It is intentionally far from a complete source of data. You can find the first one here: [5P;1R — Bitcoin’s Elliptic Curve Cryptography](https://olshansky.medium.com/5p-1r-bitcoins-elliptic-curve-cryptography-196fc74a1bf1).

1.  A **Patricia Trie** is a prefix tree where edge values are concatenated as you navigate down the tree to form a key associated with the node’s value. All leaf nodes must have a value while it remains optional for parent nodes.
2.  A **Merkle Tree** is a hash tree where the value of every non-leaf node is the hash of the sum of hashes of all of its children.
3.  A **Merkle Patricia Tree (MPT)** is used to store **keys** (hashes of values) and **values** (serialized data structures) using **Leaf Nodes** (containing a _key-end_ _&_ _value_) and **Branch Nodes** (containing _pointers to other nodes & optional value_).
4.  Assuming the **key is of size N bits** (e.g. `N = 256 bits`) and the **encoding chosen is M bits** (e.g. `M = 2^4 => hex / base 16)`, a branch node can have at most **M + 1 elements** (e.g. `1 optional value + 16 hex digits / nibbles`)and the Tree can have a **maximum depth of N / M** (e.g. `256 / 4 = 64`).
5.  Ethereum’s **Modified MPT** also contains **Extension Nodes** which is an optimization of Branch Nodes that only have one child by compressing them into a _Leaf-Node-like structure_ while replacing the **key-end with shared-nibbles** and **node value with the child path/hash** , and using a special **hex prefix** value to differentiate Extension Nodes from Leaf Nodes:

![](/images/posts/2022-04-23-5p1r-ethereums-modified-merkle-patricia-trie-image-01.png)

If I only had to recommend one resource out of all the references I looked through, it would be: <https://medium.com/@chiqing/merkle-patricia-trie-explained-ae3ac6a7e123>

![](/images/posts/2022-04-23-5p1r-ethereums-modified-merkle-patricia-trie-image-02.png)<https://ethereum.stackexchange.com/questions/6415/eli5-how-does-a-merkle-patricia-trie-tree-work>

> Join Coinmonks[ Telegram Channel](https://t.me/coincodecap) and[ Youtube Channel](https://www.youtube.com/c/coinmonks/videos) learn about crypto trading and investing

### Also, Read

- [SmithBot Review](https://coincodecap.com/smithbot-review) |[ 4 Best Free Open Source Trading Bots](https://coincodecap.com/free-open-source-trading-bots)
- [Leveraged Token](https://medium.com/coinmonks/leveraged-token-3f5257808b22) |[ Best Crypto Exchange](https://medium.com/coinmonks/crypto-exchange-dd2f9d6f3769) |[ Paxful Review](https://medium.com/coinmonks/paxful-review-4daf2354ab70)
- [Crypto arbitrage](https://medium.com/coinmonks/crypto-arbitrage-guide-how-to-make-money-as-a-beginner-62bfe5c868f6) Guide |[ How to Short Bitcoin](https://medium.com/coinmonks/how-to-short-bitcoin-568a2d0b4ae5)
- [Binance Futures Trading](https://coincodecap.com/binance-futures-trading) |[ 3Commas vs Mudrex vs eToro](https://coincodecap.com/mudrex-3commas-etoro)
- [How to buy Monero](https://coincodecap.com/buy-monero) |[ IDEX Review](https://coincodecap.com/idex-review) |[ BitKan Trading Bot](https://coincodecap.com/bitkan-trading-bot)
