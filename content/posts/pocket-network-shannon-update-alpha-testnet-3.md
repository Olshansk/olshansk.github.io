---
title: "Pocket Network Shannon Update — Alpha TestNet #3"
date: 2024-08-16T17:51:07-07:00
draft: false
tags: ["docker", "google", "grove", "ai", "shannon"]
categories: ["DevOps", "Blockchain", "Pocket Network"]
summary: "Enable Gateways by streamlining access to a decentralized supply network 🌿"
medium_url: "https://medium.com/@olshansky/pocket-network-shannon-update-alpha-testnet-3-eca539a9e111"
---

### Pocket Network Shannon Update — Alpha TestNet #3

### Grove’s Mission

Now seems like a good opportunity to remind everyone of Grove’s mission: `Enable Gateways by streamlining access to a decentralized supply network`🌿

We achieve this with **2 goals**:

- Build a protocol, Pocket Network’s \***\*Shannon\*\*** upgrade, that attracts and incentivizes high-quality supply (service providers) of open data sources and services.
- \*Build a suite of tools, \***\*Path (Path API & Toolkit Harness)\*\***, that enables anyone to settle traffic on the protocol’s decentralized supply network.

### Shannon Roadmap

The following is a tentative rough roadmap of the development of Shannon, as well as the transition from Morse to Shannon.

### The red square shows where we are today. We’ll be updating this diagram and providing more details over time.

### Why Shannon?

Though Shannon’s work on the [noisy-channel encoding theorem](https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem) was focused on error-free digital communication, the details of why we’re building Shannon have been lost over the wire.

Years of designing and building has led to A LOT of ideas of things we could do on both the protocol and gateway sides in the future, but we are laser-focused on what matters today.

### A high-level comparison of the what and why between Morse and Shannon.

### What’s new?

### 🆕 What are the new major features?

- Protocol Upgrades Framework
- Supplier Non-Custodial Staking
- Supplier Unbonding Periods
- Supplier Revenue Share
- Service Owners Addresses
- Token Logic Modules Overhaul
- Lots and lots of bug fixes, infrastructure improvements and techdebt

### 🛠️ Tools & Resources

- 🪙 **Token Faucet**: [faucet.testnet.pokt.network](https://faucet.testnet.pokt.network/)
- 🗺️ **Explorer**: [shannon.testnet.pokt.network/poktroll/block](https://shannon.testnet.pokt.network/poktroll/block)
- 🏗️ **Deploy your own gateway & Supplier**: [pokt-network/poktroll-docker-compose-example](https://github.com/pokt-network/poktroll-docker-compose-example)
- 🍝 **Copy-pasta your way to deploying on a Debian server**: [pokt-network/poktroll-docker-compose-example/debian_cheatsheet.md](https://github.com/pokt-network/poktroll-docker-compose-example/blob/main/debian_cheatsheet.md)
- 🧑‍💻 **Developer Onboarding**: [dev.poktroll.com/develop/developer_guide/quickstart](https://dev.poktroll.com/develop/developer_guide/quickstart)
- 💽 **Full Node Indexer**: [pokt-network/pocketdex/](https://github.com/pokt-network/pocketdex/)
- 📖 **General Documentation**: [docs.pokt.network/pokt-protocol/the-shannon-upgrade](https://docs.pokt.network/pokt-protocol/the-shannon-upgrade)
- 📒 **Technical Documentation**: [dev.poktroll.com/](https://dev.poktroll.com/)
- 🧑‍💻 **Shannon SDK**: [pokt-network/shannon-sdk](https://github.com/pokt-network/shannon-sdk)
- 🖥️ **Shannon source code**: [pokt-network/poktroll](https://github.com/pokt-network/poktroll)

### What’s coming up next?

- **Hardening Relay Miners** - Make it cheap and easy for anyone to run a Relay Miner (i.e. Supplier) on Pocket Network. If you’re already running an open source service (e.g. a full node), there will be zero reason to not also provide that service on Pocket.
- **Gateway Integration** - Integrating with new (Path) and existing (GatewayServer) gateway frameworks so everyone can have access to Shannon’s supply.
- **Morse Parity** - Continue working on parity features with Morse; app stake transfers, application unbonding periods, governance, inflation, etc.
- **Quality of Life Improvements** - Tending to TECHDEBT, TODOs, known bugs and other lingering issues related to scalability & source code hardening
- **Beta Preparation** - Prepare to kick off Beta TestNet, which will used for Shannon airdrop incentives, hardening the network, migration efforts, bridging, and more!

### ❓ How can one provide feedback?

- **GitHub Issues**: [pokt-network/poktroll/issues](https://github.com/pokt-network/poktroll/issues)
- **Leave a comment on Discord in** [#shannon-general](https://discord.com/channels/553741558869131266/1234943674903953529).
- Make a feature request on [Google Forms](https://docs.google.com/forms/d/1fHdmm94AytryOuRoXx58yYIoDkk4PmSuOStMlA65yuM)

### What’s our Current Focus?

In the near-term, we’re doing whatever is necessary to make it easy for you to try out our latest tooling, whether it be running a Gateway using Path or a Supplier on Shannon.

In the mid-term, we’re focused on putting Telegraph systems (i.e. Morse) behind us and moving onto Information Theory (i.e. Shannon).

Stay tuned for further updates on Path, and DM us if you have ideas of how to make Shannon more accessible.
