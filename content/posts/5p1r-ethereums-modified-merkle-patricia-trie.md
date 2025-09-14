+++
author = "Daniel Olshansky"
title = "5P;1R - Ethereum's Modified Merkle Patricia Trie"
date = "2022-04-23T06:16:39.068Z"
description = ""
tags = [
    "crypto", "ai", "tech", "5p1r"
]
substack_url = "https://olshansky.substack.com/p/5p1r-ethereums-modified-merkle-patricia"
+++

This is the second of a series of articles I’m trying out called “_5 points & 1 resource_” (think tl;dr but 5p;1r) where I summarize a list of bullet points that would have helped me start learning a new topic. It is intentionally far from a complete source of data. You can find the first one here: [5P;1R - Bitcoin's Elliptic Curve Cryptography](https://olshansky.substack.com/p/5p1r-bitcoins-elliptic-curve-cryptography)

---

- A **Patricia Trie** is a prefix tree where edge values are concatenated as you navigate down the tree to form a key associated with the node’s value. All leaf nodes must have a value while it remains optional for parent nodes.

- A **Merkle Tree** is a hash tree where the value of every non-leaf node is the hash of the sum of hashes of all of its children.

- A **Merkle Patricia Tree (MPT)** is used to store **keys** (hashes of values) and **values** (serialized data structures) using **Leaf Nodes** (containing a _key-end_ _&_ _value_) and **Branch Nodes** (containing _pointers to other nodes & optional value_).

- Assuming the **key is of size N bits** (e.g. N = 256 bits) and the **encoding chosen is M bits** (e.g. M = 2^4 ⇒ hex / base 16), a branch node can have at most **M + 1 elements** (e.g. 1 optional value + 16 hex digits / nibbles) and the Tree can have a **maximum depth of N / M** (e.g. 256 / 4 = 64).

- Ethereum’s **Modified MPT** also contains **Extension Nodes** which is an optimization of Branch Nodes that only have one child by compressing them into a _Leaf-Node-like structure_ while replacing the **key-end with shared-nibbles** and **node value with the child path/hash**, and using a special **hex prefix** value to differentiate Extension Nodes from Leaf Nodes:

---

If I only had to recommend one resource out of all the references I looked through, it would be: [https://medium.com/@chiqing/merkle-patricia-trie-explained-ae3ac6a7e123](https://medium.com/@chiqing/merkle-patricia-trie-explained-ae3ac6a7e123)

https://ethereum.stackexchange.com/questions/6415/eli5-how-does-a-merkle-patricia-trie-tree-work
