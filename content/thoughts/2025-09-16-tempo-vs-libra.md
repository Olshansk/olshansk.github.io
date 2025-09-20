---
title: "Tempo vs Libra"
date: 2025-09-16T18:19:06-07:00
draft: false
categories: ["Thoughts", "Technology", "Blockchain"]
---

**Stripe** is building a new blockchain: **Tempo**.

**Meta** tried the same ~5 years ago with **Libra/Diem**.

An overlooked point when comparing the two is what they’re focusing on...

First, a primer on 2 core blockchain concepts:

1. **Consensus**: how you agree on a set of transactions
2. **Execution**: how you process those transactions

---

**Meta → Consensus:**

- Designed & built DiemBFT (HotStuff-based)
- Optimized for scalable, permissionless consensus
- Execution layer → MoveVM
- Spurred Aptos Labs, Sui Network, 0L Network (use DiemBFT and MoveM)

**Stripe → Execution:**

- Using Reth by Paradigm (Rust-based execution layer for the EVM)
- Targeting 100K TPS
- Consensus → TBD (arc?)

Same problem space. Completely different tradeoffs.

---

Theoretical TPS in labs ≠ observed TPS in the wild.

Solana is a case study in what it takes to sustain 50K+ TPS. Those nodes are very hard and expensive to maintain.

At BuildWithGrove, while load testing POKTnetwork, we’ve also seen scaling limits pop up where you least expect them in permissionless networks.

Not in code, but in the jungle of reverse proxies spun up along the way, as one example.

Let's see how things evolve!
