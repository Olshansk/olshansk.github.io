---
title: "Pocket Network — Shannon State Shift Day"
date: 2025-05-19T16:49:51-07:00
draft: false
tags: ["pocket-network", "ai", "shannon"]
categories: ["Technology", "AI", "Blockchain"]
summary: "tl;dr — Pocket Network will hard-fork from Morse MainNet to Shannon MainNet on June 3, 2025 at 10 a.m. PT."
medium_url: "https://medium.com/@olshansky/pocket-network-shannon-state-shift-day-b8c06122cb76"
ShowToc: true
---

![Shannon State Shift Day Banner](https://cdn-images-1.medium.com/max/800/1*em-561cFxCmQH42gv-My0w.png)

### Pocket Network — Shannon State Shift Day

_tl;dr — Pocket Network will hard-fork from Morse MainNet to Shannon MainNet on **June 3, 2025 at 10 a.m. PT**._

### Table of Contents

- [Pocket Network — Shannon State Shift Day](#pocket-network--shannon-state-shift-day)
- [Table of Contents](#table-of-contents)
- [State Shift Day Announcement](#state-shift-day-announcement)
- [What happens on State Shift Day?](#what-happens-on-state-shift-day)
- [What happens after?](#what-happens-after)
- [Staying up to date \& getting help](#staying-up-to-date--getting-help)
- [Thank you](#thank-you)

### State Shift Day Announcement

Two weeks ago we released the first set of Shannon-migration resources. You can catch up [here](https://medium.com/decentralized-infrastructure/pocket-network-shannon-migration-announcement-139c25e4166c).

**The hard fork is locked in for June 3, 2025 at 10 a.m. PT.**

In honor of Claude Shannon's work on bit manipulation in the context of Information Theory and Signal Processing, we're calling the event **_State Shift Day_**.

This upgrade is a major step to unlocking native interoperability, maintainability, and most importantly, the technical capability to iterate quickly so we can achieve our [long-term roadmap](https://forum.pokt.network/t/shannon-post-launch-development-roadmap/5497).

### What happens on State Shift Day?

The Pocket Network Foundation 🌀, with support from Grove 🌿, will perform the following sequence:

1. **Morse Snapshot** — capture the Morse MainNet state.
2. **State Transform** — convert that snapshot into a Shannon _genesis-like_ state object, with one-off adjustments for special cases (e.g. highly-staked validators).
3. **Shannon Upload** — publish the state transform to Shannon, opening token-claim windows.
4. **Morse Rewards Off** — adjust `RelayToTokenMultiplier` on Morse to **0**; turning off the production of new tokens removing incentives for any actor (Validator or Supplier) to continue participating in the network.
5. **Traffic Shift** — Gateways (including Grove) begin rerouting traffic from Morse to Shannon.

### What happens after?

Migrating a live, permissionless network **_and_** changing its cryptographic key scheme has never been done — per all the conversations we've had with other Web3 organizations — so we're pushing the frontier.

Our priority is to minimize downtime for users while giving every participant a clear path forward.

Here is what we anticipate to happen and follow in the days and weeks following State Shift Day:

- **Token Claims** — Sovereign POKT holders can claim immediately. The Foundation will maintain the upgrade functionality for one year after the Shannon cutover date to make sure that everyone with a Morse wallet has had a chance to upgrade to Shannon.
- **Centralized Exchanges** — CEXs will (likely) briefly pause POKT deposits/withdrawals while claiming on behalf of customers. Most already support Cosmos-style chains, so we anticipate a smooth process. There is a risk of delisting as well.
- **Morse Actor Migration** — With incentives gone, we expect all Suppliers and Validators to quickly move from Morse to Shannon.
- **Morse Chain Halt** — As Validators stop signing Morse blocks and exchanges disable trading, Morse will naturally halt.
- **Shannon MVP Tooling** — Over the following weeks, we'll prioritize feedback from the community and focus on tooling to ensure a smooth continued transition, as we begin onboarding new ecosystem participants.

_If you rely on Grove's portal, we expect brief interruptions. We are aware that Grove and Pocket Network act as a backup RPC provider for major services, so please ensure that you have another backup during State Shift Week._

### Staying up to date & getting help

We're shipping updates to our [docs](https://docs.pokt.network/) and [tooling](https://dev.poktroll.com/) daily.

Stay current via [Discord](https://discord.gg/build-with-grove), [Twitter](https://x.com/BuildWithGrove), [Docs](https://dev.poktroll.com), or [Telegram](https://t.me/@UnofficialPokt). If you need support, reach us via [email](mailto:portal@grove.city), or book time on [Calendly](https://calendly.com/d/cmdf-tbq-dc3/grove-engineering).

Large ecosystem participants (exchanges, investors, validators, suppliers) can contact the Foundation for bespoke support.

We're actively publishing and updating a living [FAQ](https://dev.poktroll.com/category/faq--troubleshooting).

![FAQ Documentation Screenshot](https://cdn-images-1.medium.com/max/800/1*PApy984ama2eqDS54Whu9A.png)
_[https://dev.poktroll.com/category/faq--troubleshooting](https://dev.poktroll.com/category/faq--troubleshooting)_

### Thank you

State Shift Day is the first concrete step toward a [**crypto-native API layer**](https://dev.poktroll.com/). On behalf of Grove Inc. and the Pocket Network Foundation, thank you for building the next internet with us. 🌿🌀

![Grove and Pocket Network Footer](https://cdn-images-1.medium.com/max/800/1*0wtR-jL4Ars4Vbw3g-D-Xg.png)
