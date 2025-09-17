---
title: "Pocket Network Shannon Migration Announcement"
date: 2025-05-06T19:08:16-07:00
draft: false
tags: ["pocket-network", "grove", "ai", "shannon"]
categories: ["Technology", "AI", "Blockchain"]
summary: "Pocket Network will undergo a major, consensus-breaking, non-backwards-compatible migration from Morse to Shannon before the end of Q2."
medium_url: "https://medium.com/@olshansky/pocket-network-shannon-migration-announcement-139c25e4166c"
ShowToc: true
---

![Pocket Network Shannon Migration Banner](/images/posts/pocket-network-shannon-migration-announcement-image-01.png)

### Pocket Network Shannon Migration Announcement

[Pocket Network](https://pokt.network/) will undergo a major, consensus-breaking, non-backwards-compatible migration from Morse to Shannon **before the end of Q2.**

The exact date will be finalized based on community feedback — **_your input matters_**. You can read more about our [shadow MainNet launch](https://medium.com/decentralized-infrastructure/pocket-networks-shannon-upgrade-has-been-successfully-soft-launched-f91f1af8039c) or the [history of the migration](https://medium.com/decentralized-infrastructure/an-update-from-grove-on-shannon-beta-testnet-path-the-past-the-future-5bf7ec2a9acf).

Once a concrete date is set, ecosystem participants will have exactly 14 days to prepare. **This could happen as early as next week**. It is deliberately lower than the 21-day on-chain unstaking time to prevent the gamification of the network.

### Table Of Contents

- [Pocket Network Shannon Migration Announcement](#pocket-network-shannon-migration-announcement)
- [Table Of Contents](#table-of-contents)
- [What's happening to my POKT?](#whats-happening-to-my-pokt)
- [🏦 Exchanges \& Investors](#-exchanges--investors)
- [⚙️ Suppliers (formerly Servicers / Node-Runners)](#️-suppliers-formerly-servicers--node-runners)
- [🌐 Applications \& Gateways](#-applications--gateways)
- [🔐 Validators](#-validators)
- [Staying up to date \& getting help](#staying-up-to-date--getting-help)
- [Thank you](#thank-you)

The docs behind the links in this post are being updated daily. You can also find a mirror of this post [on Notion](https://buildwithgrove.notion.site/Pocket-Network-Shannon-Migration-1e5a36edfff6805b87e0e512340b2c79) in table format.

![Migration Overview Visual](/images/posts/pocket-network-shannon-migration-announcement-image-02.png)
_A single visual of the links and details to get a quick high-level picture of what's happening._

### What's happening to my POKT?

- All staked and liquid balances **migrate 1 : 1.**
- Shannon is switching to [Cosmos cryptographic keys](https://docs.cosmos.network/main/learn/beginner/accounts) — every account requires a new address. [**Manual action**](https://dev.poktroll.com/explore/morse_migration/claiming_account) **is required to claim tokens.**
- [Migration docs](https://dev.poktroll.com/category/morse---shannon-migration) are updated continuously — check them before acting.

### 🏦 Exchanges & Investors

**What's happening & changing?** Balances migrate 1:1, but new cryptographic schemes are used for addresses and keys.

**What do you need to do?**

1. Create Shannon accounts
2. Claim Morse accounts
3. _(Optional)_ Run a full node

**Key Links:**

- [Creating a new wallet](https://dev.poktroll.com/explore/account_management/create_new_account_cli)
- [Claim your account](https://dev.poktroll.com/explore/morse_migration/claiming_account)
- [Operating a Full Node](https://dev.poktroll.com/operate/cheat_sheets/full_node_cheatsheet)

### ⚙️ Suppliers (formerly Servicers / Node-Runners)

**What's happening & changing?** Supplier stakes & balances migrate onchain, but operators must update their tooling, infra, and configs to provide services and earn rewards on Shannon.

**What do you need to do?**

1. Stake a Shannon Supplier
2. Stand up a Relay Miner
3. Claim your Morse Servicer
4. Reconfigure your endpoints

**Key Links:**

- [Operating a Supplier](https://dev.poktroll.com/operate/cheat_sheets/supplier_cheatsheet)
- [Claiming a Supplier](https://dev.poktroll.com/explore/morse_migration/claiming_supplier)

### 🌐 Applications & Gateways

**What's happening & changing?** App stakes & balances migrate onchain, but Gateway operators must migrate to running PATH to settle traffic on Shannon.

**What do you need to do?**

1. Stake a Shannon Application
2. Stake a Shannon Gateway
3. Stand up a PATH Gateway
4. Claim your Morse Application

**Key Links:**

- [Operating a Gateway](https://dev.poktroll.com/operate/cheat_sheets/gateway_cheatsheet)
- [Claiming an Application](https://dev.poktroll.com/explore/morse_migration/claiming_application)
- [PATH Documentation](https://path.grove.city/)

### 🔐 Validators

**What's happening & changing?** Validators are now decoupled from Suppliers and follow standard Cosmos patterns.

**What do you need to do?**

- Review validator walkthrough
- Reach out if you'd like to join the initial set

**Key Links:**

- [Validator Walkthrough](https://dev.poktroll.com/operate/cheat_sheets/validator_cheatsheet)
- [Cosmos Validator Overview](https://hub.cosmos.network/main/validators/overview)

### Staying up to date & getting help

We're shipping updates to our docs and tooling daily. Stay current via [Discord](https://discord.gg/build-with-grove), [Twitter](https://x.com/BuildWithGrove), [Docs](https://dev.poktroll.com), or [Telegram](https://t.me/@UnofficialPokt). If you need support, reach us via [email us](mailto:portal@grove.city), or book time on [Calendly](https://calendly.com/d/cmdf-tbq-dc3/grove-engineering).

### Thank you

This migration is the first step toward our shared vision of a **crypto-native API Layer**. _What does that mean?_ It co-exists with Web2 services, supports traditional enterprises, and is gearing up to enable an internet of agentic API requests.

On behalf of **Grove Inc.** and the **Pocket Network Foundation**, thank you for your continued support.

![Grove and Pocket Network Footer](/images/posts/pocket-network-shannon-migration-announcement-image-03.png)
