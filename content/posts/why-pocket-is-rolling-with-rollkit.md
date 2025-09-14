+++
author = "Daniel Olshansky"
title = "Why Pocket is Rolling with Rollkit"
date = "2023-09-29T23:39:57.222Z"
description = "A historical and technical deep dive leading to the next steps in the Pocket Network Protocol"
tags = [
    "crypto", "ai", "startup", "tech", "research", "productivity"
]
substack_url = "https://olshansky.substack.com/p/why-pocket-is-rolling-with-rollkit"
+++

This is a cross-post of the original article posted [here](https://www.pokt.network/why-pokt-network-is-rolling-with-rollkit-a-technical-deep-dive/) and announced [here](https://twitter.com/POKTnetwork/status/1704865768457060375) a couple of weeks ago. Some of the tables and diagrams that are presented as screenshots can be viewed in more detail in the markdown GitHub gist [here](https://gist.github.com/Olshansk/8c214ea3cb4685798079faadd6258664).

---

_tl;dr The Pocket Network core protocol team has decided to implement the first version of the next iteration of the protocol (Shannon Upgrade) as a “[micro-rollup](https://kautuk.substack.com/p/micro-rollup-a-wave-or-just-a-shameless)” using [Rollkit](https://rollkit.dev/) with [Celestia](https://celestia.org/) as a Data Availability (DA) layer._

_You can read the announcement by [@MatthewRossi](https://twitter.com/MatthewRossi), our Head of Product (Protocol), on behalf of the Pocket Network Foundation, [here](https://www.pokt.network/a-sovereign-rollup-and-a-modular-future/) to skip the technical history and jump straight to the point._

# **🛑 Taking a Pause to Forge Ahead 🛑**

In early August, the Pocket Network core protocol team made a crucial decision: we temporarily halted all development on the upcoming version of the Pocket Network Protocol: the Shannon upgrade (formerly referred to as v1). We embarked on a 3-week intensive research to evaluate rapid advancements of other projects in the industry and ensure an optimal path forward.

- Our research period was a mix of open exploration, daily research syncs lasting 1-2 hours, in-person discussions at a three-day offsite retreat, extensive deep dives into at least nine projects that caught our attention, calls with core team members from these projects, input from industry experts, and the development of several Proof-of-Concepts (POCs) along the way.

To get to the punch line, we’re going to implement the Shannon upgrade as a micro-rollup using [Rollkit](https://rollkit.dev/)’s modular framework that features [Celestia](https://celestia.org/) as the Data Availability (DA) layer.

This post will delve into some of Pocket Network’s history, explain how we got here, re-state the core problems the protocol solves, and detail the requirements and considerations that eventually led us to this final decision.

We'll also touch on some trending topics, including Data Availability and various Proof methodologies. Though these topics guided our direction, it's essential to note that our decisions were primarily steered by our medium-term product requirements so we can hone in our utility in creating the most powerful decentralized RPC protocol out there.

[Pocket Protocol Perplections](https://docs.google.com/presentation/d/1ik7EaM-b2LB78Pn3AVpa_rDQcTc7XxjvYIJZBONHPns/edit#slide=id.p) (August 9th, 2023)

# What is Pocket ❓

Pocket Network is an open protocol that offers developers **R**eliable, **P**erformant, and **C**ost-effective **RPC** access to the open internet. It’s the decentralized counterpart of your favourite neighborhood centralized node provider, designed to address the **RPC Trilemma**.

Most centralized _“Nodes-as-a-Service”_ providers excel in offering **Performant** and **Cost-effective** solutions, but what they lack is **Reliable** multi-tenant decentralization that can only be achieved via token-based incentivization.

Pocket's native cryptocurrency, POKT, facilitates access to a wide network of providers supporting more than 42 [blockchain RPC endpoints](https://docs.pokt.network/supported-blockchains/). POKT incentivizes full nodes (non-validators) to exist, pessimistically validate state transitions, replicate data, and make it accessible to developers. It's analogous to a universal API token, granting access to diverse RPC services from multiple providers.

The subsequent diagram (Fig 1) captures the interaction and relation among the various entities within Pocket and its functionality. Stick around as we later delve into how Pocket has operated as a pseudo-rollup since its inception! 🥕

Fig 1. Protocol actor integration post Shannon upgradeCommon questions we usually get are related to POKT tokenomics or our strategies for ensuring high QoS. However, here's a quick breakdown of our core utility in 4 bullet points:

**Applications** remunerate in POKT for RPC service access

- **Servicers** receive POKT in return for providing RPC services

- **Servicers** submit claims reflecting their service volume

- **Validators** verify proofs corresponding to the claimed service volume

# Morse (v0️⃣) - Navigating Mainnet for more than 3 years

The genesis of Pocket began in 2017 with the founding team: Michael (currently CEO of [Grove](https://grove.city)), Luis, and Andrew. Back when new Initial Coin Offerings (ICOs) would break the previous day’s record, or when plasma and state channels were all the rage, they sought ways of designing Pocket as a smart-contract-based protocol. Concepts like rollups, modularity, data availability, and even Ethereum as a Proof of Stake chain were mere visions on some distant horizon.

- [https://medium.com/ethereum-optimism/introducing-evm-equivalence-5c2021deb306](https://medium.com/ethereum-optimism/introducing-evm-equivalence-5c2021deb306)However, upon realizing the high costs of smart contracts and recognizing the constraints and nascent state of scaling solutions, the team shipped Pocket Protocol as its own sovereign L1 _“app-chain”_ utilizing a **[Tendermint](https://tendermint.com/)** fork.

In three years, Pocket has grown to all-time highs of more than 2B daily relays across dozens of blockchains. One of the coolest achievements is also the fact that none of the nodes currently on the network are run by the corporation that paid for developing the original protocol - which speaks to the substantial growth and strength of the Pocket community, ecosystem, and 60+ person DAO.

[poktscan.com](https://www.notion.so/ba333db3bca440f0addbc32abb985d5e?pvs=21)

# From Morse to Shannon : **Navigating Constraints, Legacy & Insights**

There is a lot of historical context leading to the decision to fork Tendermint in early 2020 (after beginning to design Pocket in 2017), leading to various downstream decisions.

Pocket Network’s first release, Morse (formerly known as v0), encountered a handful of chain halts, has had various scalability limitations, and due to our extensive modifications of Tendermint Core - has not kept up to date with Main.

Some of the problems we encountered included:

**Operational resource constraints**: The team was heavily constrained on time & capital, but managed to design & ship the first decentralized RPC protocol.

- **Tendermint Security Enhancements:** We added randomness into the proposer leader selection algorithm, shielding against potential [DDoS attacks](https://github.com/pokt-network/tendermint/commit/1d191c29a079c404c96c0c9bece5a44d18d2f1d2). This was not part of Tendermint Core at the time.

- **Tendermint Scaling**: Our network pushed Tendermint’s validator set to its limit. We had more than 20,000 individual validators at one point, double [Tendermint’s 10,000 validator limit](https://github.com/tendermint/spec/blob/master/spec/core/state.md), which ultimately led to a chain halt. As a result, we set a hard cap of 1,000 validators based on POKT stake weight.

- **Scaling and Performance:** We hit a few performance snags as Pocket Network grew. Amino serialization, IAVL operations, and the aforementioned validator limitation. We switched to protobufs (aligning with mainline Tendermint) and found workarounds for the IAVL issues.

- **Pocket Proofs & Sizes**: One of the biggest bottlenecks to making Pocket completely scalable and permissionless is the size of the relay proofs and the time to compute/verify them.

In late 2021, almost eighteen months after the genesis launch in 2020, with a growing network, a committed node runner community, and an influx of new capital, it felt right to start mapping out the [Shannon upgrade specifications](https://github.com/pokt-network/pocket-network-protocol/). As most of what has come into existence in the last 12 months (DA layers, rollup frameworks, etc…) did not exist at the time, the initial roadmap embraced [Hotstuff](https://arxiv.org/abs/1803.05069) consensus, a scalable P2P layer, and new ideas we couldn’t implement in the existing implementation of the network as we eyed crafting a top-tier L1 from the ground up.

Our development [was open source](https://github.com/pokt-network/pocket) since day 1 as we embarked on this ambitious task. As the core team grew and changed, the community became really active, finding solutions to scale the existing protocol on [our forums](https://forum.pokt.network/). External contributors came to help us BUIDL, and we all know what happened to the markets…

- As we kept building everything from the ground up, a lot of things started changing in the industry. Vitalik’s [Rollup-Centric Ethereum Roadmap](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698) in the EVM ecosystem started coming to fruition, Tendermint was rebranded to [CometBFT](https://cometbft.com/), and development picked up again. What started as a note on Ethereum’s [Research Github](https://github.com/ethereum/research/wiki/A-note-on-data-availability-and-erasure-coding), became an industry revolving around Data Availability, and started a movement around Modularity.

Having tooling, DA layers, settlement layers and interoperability protocols today enables us to delegate the responsibilities of some parts of a blockchain and focus on our utility instead.

# Shannon (v1️⃣) - The Pivot 📐

More than two years after designing the **[new specifications](https://github.com/pokt-network/pocket-network-protocol/)** for a custom L1 blockchain, and dedicating 1.5 years to R&D in our **[OSS repository](https://github.com/pokt-network/pocket)**, we've seen our highs and lows. The biggest realization? The need to focus on our utility, embrace modularity, and iterate on new features; a lesson every engineering org re-learns sooner or later.

Our decisions were always guided by first principles and steadfastly committed to the **[KISS](https://en.wikipedia.org/wiki/KISS_principle)** and **[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)** methodologies. We're proud of our documentation and the breadth of external contributors who joined along the way. Yet, over time, our development focus shifted towards the blockchain-back-end components of consensus, p2p, and persistence and away from our primary utility of decentralized RPC. Our ambitious move to design a complex system from the outset conflicted with Gall’s law, one of the pivotal **[Hacker Laws](https://github.com/dwmkerr/hacker-laws#galls-law)**:

> A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.

As we edged closer to launching the Shannon TestNet, we recognized that things were getting way more complex than we originally intended - a major driver in the decision to pivot to Rollkit was to get back to basics. Despite our vibrant community and committed node runners, we felt isolated as a protocol, navigating through the Ether in a separate Cosmos from leading ecosystems.

# Why now ⁉️

Our team regularly reassesses our trajectory after every major conference, event or significant industry innovation. For example, here are a few slides after Devcon6:

We also kept an eye out on other projects to understand what’s actually being done instead of what’s being advertised and marketed.

While we were making lots of progress toward the Shannon TestNet, we also realized there’s never a right time to Pivot and explore other options - the classic _“sunk-cost fallacy”_ at work, so we made the hard call to stop and challenge our base assumptions and approach. In the worst case, we’d lose three weeks of development time, learn a lot along the way, and pick up where we left off afterwards.

# Pocket Requirements & Evaluation Criteria ⚖️

Identifying exact requirements and clearly understanding our needs forms the foundation of any good research spike. However, articulating and defining these is more challenging than it sounds. We began with initial guidelines, and as we progressed, these evolved, raised new questions, became clearer, and re-raised further questions. One of our protocol engineers, Bryan, put it very well when he phrased it as needing to understand the **_“degrees of freedom”_** we can operate around. I think it’s fair to say that everyone on the team self-reflected on both Pocket Network's direction and the broader implications for blockchains sooner or later.

Ultimately, our functional requirements could be summarized as follows:

🚪**Permissionless Actors**: Any actor, whether an Application, Servicer, Portal, or Watcher, must be able to freely join or exit by staking or un-staking POKT.

- 💁‍♂️ **Servicer Selection:** Servicers should be chosen pseudorandomly, ensuring a fair distribution of work. This selection should factor in POKT stake weight, the quality of service, and the RPC services provided.

- 📞 **Relay Request**: Applications must be equipped to utilize the network, enabling Servicers to relay both read and write requests to any stateless service or any accessible data source through a unique RPC endpoint.

- **🧾 ⛏️Mine Relays:** Applications must be rate-limited by Servicers based on POKT stakes. Later, POKT must be minted and burned based on the quality and volume of relays completed.

- **📈 Scalable Relay Volume**: It is crucial for the network to be scalable, accommodating the anticipated growth in actors, sessions, chains, and relays in the foreseeable future.

- **🎛 Customizable Rewards & Cost Systems:** Both the cost and reward structures should be adjustable based on the service/chain and reflect real-world compute usage.

- **🫥 Transparent Data Management**: All records, service quality metrics, and other aggregated metadata should be openly available, verifiable, and stored on a decentralized ledger.

- **🌐 Interoperable**: Compatibility at protocol, community, and tooling levels is essential, especially with major ecosystems like IBC and EVM.

Mapping a requirement to a _“blockchain layer”_ can be considered a pseudoscience, but I think even an attempt can help build context. In the following table, the _Incentive Layer_ can be treated as the design of the actual application, and the _Execution Layer_ is what manages the state transition functions.

- Some additional non-functional requirements, applicable to any team (engineering or not), are to move fast, iterate, focus on building what provides value to our users and to quote Albert Einstein:

> Everything should be made as simple as possible, but not simpler.

# Hearing & Comparing 👂

With our requirements at hand, we started evaluating what’s out there.

We looked into the Cosmos Ecosystem (CometBFT, Cosmos SDK, Celestia), the EVM Ecosystem (Arbitrum, Optimism, Polygon, Aztec), compared ourselves against similar Smart Contract projects (LivePeer, TheGraph, Streamr), evaluated some Rollup-as-a-Service options ([Caldera](https://caldera.xyz/) and [Conduit](https://conduit.xyz/)) and also reviewed a few other projects that didn’t fit any of these buckets like Polygon Edge (Side-Chain) and Storj (Decentralized Data Storage).

Some of our internal and external discussions often had the following phrases come up over and over:

However, seeing how supportive everyone we spoke to is of other projects was very refreshing. At the end of the day, we’re all working towards the same vision:

> “Their team has brilliant & hard working individuals.”
> ”Their team is providing us with all the support we need asap.”
> ”They have great ideas and making a ton of progress.”
> ”That framework is very easy to use.”
> ”Their docs are very educational & informative.”

We realized that there wouldn’t be a clear and definitive answer here, and given the need to examine the ecosystem benefits of choosing one opportunity over another, too, it quickly became apparent that the set of tradeoffs resembled art more so than science.

# Defining Ambiguity in the Search for Data Availability

Partway through our research spike, we had the idea of doing a literature review-like document evaluating all the solutions that either exist or are under active development: smart contracts, L1, L2, L3, various DA layers, various rollup frameworks, etc.… However, it is hard to draw a straightforward comparison. Not only would this be a huge undertaking, but it is very nuanced. We need to compare what exists today vs. what will be available tomorrow. What are our timelines? What level of security risk are we willing to take? How much of a tradeoff will we take in exchange for the true long-term web3 ethos of complete sovereignty, permissionlessness and decentralization? What does settlement really mean? What ecosystem benefits do we expect? And what is the opportunity cost for choosing one option over another?

Settlement is very similar to 🎂. It can be delicious and bring joy, but comes with costs and tradeoffs since it’s not the healthiest food group. It could be a piece of cake if you leverage an existing framework, but could be very burdensome if you bake it from scratch. Some even question whether Settlement is real at all, or if it's just a promise from GLaDOS. Choose your 🍰

The team drew inspiration from the posts by [@jon_charb](https://twitter.com/jon_charb) discussing how [Rollups Aren’t real](https://joncharbonneau.substack.com/p/rollups-arent-real), and how Rollup’s [Actually Work](https://dba.mirror.xyz/LYUb_Y2huJhNUw_z8ltqui2d6KY8Fc3t_cnSE9rDL_o) to understand the caveats and ideologies around these topics. Understanding that nuance, reading through [Optimism](https://www.optimism.io/)’s amazing documentation on EVM rollups, and comparing that to documentation from [Sovereign Labs](https://www.sovereign.xyz/) and [Celestia](https://celestia.org/) on sovereign rollups can build a really good conceptual model that I won’t try to re-explain here.

Source: Kelvin Fichter, How Rollups actually workThere are endless discussions around building truly decentralized and permissionless systems to tackle the [Blockchain Scalability Trilemma](https://vitalik.ca/general/2021/04/07/sharding.html). If blockchain is really a science, then we are very early in the process of discovering what’s true based on [Alin Tomescu](https://alinush.github.io/2023/06/02/Science-process-not-truth.html)’s definition:

> Science is a **process** that we engage in to discover truths. And it often leads us astray **[3](https://alinush.github.io/2023/06/02/Science-process-not-truth.html#fn:galileo)**,**[4](https://alinush.github.io/2023/06/02/Science-process-not-truth.html#fn:aether)**, which is why the idea of “science being true” is at best misleading and at worst dangerous.

Threads like [this](https://twitter.com/bkiepuszewski/status/1696417258552033558) on X do an excellent job at capturing the idea. L1s and L2s provide applications with consensus, data availability and have various tradeoffs when it comes to latency, cost and security, but those details are outside the scope of this post.

[X thread](https://twitter.com/jon_charb/status/1698195724960203029?s=20)A few common themes kept coming up when we spoke to different teams and individuals:

Everyone is starting with Fraud (optimistic) proofs and is aiming to have Validity (zk) proofs in the future

- Everyone is starting with a single centralized sequencer (i.e. a fancy term for a web2 server) and aiming to decentralize it over time

- Lots of teams are working on making validity proofs cheaper & more efficient to generate and verify in the future

- Every sovereign rollup framework aims to have a configurable DA layer at some point in the future

- There are lots of ways (e.g. bridging, etc.) to achieve settlement (whatever that means) and interoperability with other chains

- It’s too early to have an analytical comparison of data availability costs across DA layers, sequencer speeds and decentralization, or proof cost and sizes. These will have an impact across various factors, including the censorship resistance of the underlying DA, its ability to enable trustless bridging, etc.

-

# Why not the EVM?

When the team started its research spike, we were heavily focused on the OP Stack due to the signal in the industry and our bullish view on the EVM ecosystem, its developer community, security and interoperability. We managed to rule out EVM-based solutions after a little bit of work and a lot of great ideas from [@h5law](https://twitter.com/h5law), one of our lead protocol engineers.

We quickly realized that we might need to be an [OP Stack Hack](https://stack.optimism.io/docs/build/hacks/), but it would result in our new chain not being part of the official OP stack and, therefore, losing many of the ecosystem benefits we sought to obtain by joining the Superchain. We also discovered that we don’t need to fork the OP Stack because Pocket is an application-specific chain, and we do not need to be a standalone smart contract EVM rollup. This got us excited by the idea that Pocket could become a Smart Contract that acts as a registry for our on-chain actors deployed on one of the major EVM rollups similar to [The Graph](https://thegraph.com/) and [LivePeer](https://livepeer.org/).

The team quickly put together a smart contract that captures the bare-bones functionality (i.e. parity with the live network) of what we need.

// SPDX-License-Identifier: MIT
pragma solidity 0.8.15;

contract PocketNetwork {
enum ComputeUnitType { PER_REQUEST }
enum ActorType { APPLICATION, SERVICER }

struct ComputeUnit { ... }
struct Fraction { ... }
struct Service { ... }
struct Actor { ... }
struct Application { ... }
struct Servicer { ... }
struct RelayProof { ... }
struct RelayClaim { ... }
struct Session { ... }

mapping(address => Application) public applications;
mapping(address => Servicer) public servicers;
mapping(bytes32 => mapping(address => RelayClaim)) public relayClaims;
mapping(bytes32 => Session) public sessions;

function getApplication(address applicationAddress) public view returns (Application memory) { ... }
function getServicer(address servicerAddress) public view returns (Servicer memory) { ... }
function getSessionNumber(uint256 blockHeight) public view returns (uint256) { ... }
function getHeightSession(uint256 blockHeight) public view returns (uint256) { ... }
function getSessionHeight(uint256 session) public view returns (uint256) { ... }
function getSessionData(address applicationAddress, uint256 blockHeight, uint256 serviceId) public view returns (Session memory) { ... }
function getSessionSecret(uint256 blockHeight) external view returns (bytes32) { ... }
function stake(ComputeUnit memory offerRate, uint256 serviceId, ActorType actorType) external payable { ... }
function unstake(uint256 amount, ActorType actorType) external { ... }
function submitRelayClaim(RelayClaim memory relayClaim) external { ... }
function validateRelayProof(RelayProof memory relayProof, bytes32 leaf) external view returns (bool) { ... }
function verifySumProof(bytes[] memory \_sideNodes, bytes memory \_root, bytes32 \_path, bytes32 \_valueHash, uint64 \_sum) external pure returns (bool) { ... }
function getPathBit(bytes32 \_path, uint256 \_index) internal pure returns (uint8) { ... }
function getParent(bytes memory \_left, bytes memory \_right) internal pure returns (bytes memory) { ... }
}
And then found ourselves having discussions around how to optimize for gas.

We realized that we’ll be at the mercy of various gas optimization discussions for our relay verification mechanism, while also being constrained by L2 to Ethereum block compression optimizations, and potential gas spikes in turbulent markets. That’s when Vitalik’s [Ethereum’s rollup-centric roadmap](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698) from a few years back became much evident, and when this line from the Optimism docs really started ringing (pun intended) true:

We need EVM compatibility not for the protocol’s core utility but to improve the experience related to wallets, our DAO UX, and access to best-in-class DeFi infra and token liquidity. This was a critical component of why we sought to explore rollups, particularly the OP stack, in the first place. But if we can’t deploy directly where the wallet, DAO or DeFi infra we want to integrate with currently exists (e.g. on ETH L1, OP stack, Arbitrum, Polygon, etc.), we still need a bridge somewhere along the way. Building outside of the EVM ecosystem can get us to a pretty similar spot without needing to be “EVM Native” if sufficiently robust and well-supported bridges like [Axelar](https://axelar.network/) and [Hyperlane](https://www.hyperlane.xyz/) support our network.

# Pocket has always been a Rollup 🧻

One of our key findings during this exercise, first mentioned by Dylan, is the realization that \*“**Pocket is, and always has been, a pseudo-rollup.”\***

Needing to handle more than a billion requests a day, with the goal of having the network handle a magnitude more within the next few years, it’s unfathomable (and unnecessary) to have every request be its own independent on-chain transaction. Having an on-chain transaction called `Relay` can be ruled out immediately.

Off-chain, Applications make thousands or millions of RPC requests to a Servicer during a session. Once the session ends, the Servicer uses a basic commit-and-reveal scheme that requires it to reveal one random branch in the tree. In other words, servicers roll-up all the RPC requests over some time (e.g. 1 session = 1 hour) and post a claim for it on-chain. Later, they are requested to provide a pseudorandom proof that cannot be predicted ahead of time. It can be thought of as a hybrid between an optimistic and a validity proof with different probabilistic error guarantees, but those details are outside the scope of this specific post. The [Relay Mining Paper](https://arxiv.org/abs/2305.10672) and [Shannon specifications](https://github.com/pokt-network/pocket-network-protocol) go into it in greater depth for those interested in learning more.

A few of the key things in realizing the above is understanding where Pocket stands:

**Scalability** - Most of Pocket’s business logic happens off-chain, so our scalability is less-so limited by the number of transactions that we need to have on-chain.

- **Latency** - Accounting for POKT rewards distributions, slashes, POKT transfers and staking updates do not necessarily require sub-minute commitment, so longer block times are okay.

In Pocket’s utility, the blockchain is used as a distributed registry (i.e. ledger) to transparently track actor properties, optimistically rate limit applications, verify the work done and keep permissionless actors honest through (dis)incentives. We have the leisure of not needing to optimize for milliseconds.

# Committing to a Decision 🧑‍⚖️

**We’ve already started prototyping an [alpha version of the Shannon upgrade](https://github.com/pokt-network/poktroll-alpha) as a rollup using Rollkit and Celestia as a DA layer, and are committed to bringing this to mainnet early next year.**

We had a few _“runners-ups”_ and wanted to share the reasons that led to our final decision. After going through the research above, identifying our requirements, and ruling out the need to be “EVM Native,” our top 3 choices were

- [Rollkit](https://rollkit.dev/): leveraging the Cosmos SDK and Celestia DA (configurable)

- [Cosmos](https://docs.cosmos.network/main/building-modules/structure): leveraging the Cosmos SDK and [CometBFT](https://docs.cometbft.com/v0.37/)

- [Sovereign](https://www.sovereign.xyz/): Leveraging the Sovereign SDK and Celestia DA (configurable)

These three solutions would cover all of our functional requirements, but in terms of non-functional requirements, we also took the following into account:

- **Framework Maturity** - Though Cosmos has a lot of [encapsulated complexity](https://vitalik.ca/general/2022/02/28/complexity.html), it is also a very mature framework that provides tons of tooling out of the box.

- **Support** - All three of these options have very supportive teams that have been invaluable in answering all our questions.

- **Risk Mitigation** - If we realize that, for some reason, we need to quickly go back to being an L1, Rollkit makes that much easier as it is compliant with the ABCI interface and lets us fall back to Cosmos.

- **Interoperability** - We filtered for options that are compatible with IBC out of the box, which also enables us to leverage projects like Axelar to bridge into the EVM ecosystem.

- **Simplicity** - While we’re not too focused on the programming language, we did take into consideration that the team has experience in Go, and Rust has a slightly higher learning curve, which adds some complexity.

- **Time to Market** - We biased towards more mature networks and frameworks to shorten the timeline for us to reach Mainnet.

- **External Contributions** - Using a well-known framework (i.e. Cosmos) would welcome more external contributors to build submodules specific to Pocket’s utility.

I anticipate that over the next 3-9 months, as these frameworks and DA layers mature, there will be a lot more visibility into the costs, scalability, security and decentralization of each solution. For now, we’re making the best decision we can, given the data we have.

# So What’s Happening to the Validators?

Pocket was always committed to being the most decentralized, trustless and censorship-resistant protocol out there. By moving to a rollup, we’re delegating the security and decentralization to the underlying Data Availability layer, which could raise risk with respect to censorship resistance. However, modularity means that Pocket could move from one DA layer to another, use multiple DA layers in parallel for redundancy, and eventually leverage its network of nodes for its own DA layer. It also moves the cost of the validators (on and off-chain) to the underlying Data Availability layer.

Some of the leading projects in the space, with very talented and hardworking teams, are working on solving the problems related to censorship resistance, DDoS attacks, trustless bridging, decentralizing sequencers, and many others while also making sure that these solutions scale. Being able to delegate that responsibility to a project for whom it is their top priority, allows us to focus on our core value add - Portals, Applications & Servicers and Relay Mining, rather than Validators & Sequencers.

Instead of scaling validators, we can scale the number of relays that the network can handle. Instead of researching proof mechanisms for state transitions, we can focus on proving different types of relays (gRPC, websockets, etc…) and their quality of service, on-chain. Instead of designing permissionless sequencers, we can design trust and tokenomic mechanisms around permissionless portals (i.e. gateways). We have plenty of other ideas and are hoping to collaborate tightly with the teams behind the projects that we’ll be working with.

This shift in work lets us focus solely on Pocket’s utility. We can nail down the core mechanics specific to the Pocket Network, such as the claim & proof lifecycle to validate relays completed, and spend more time listening to the community on how to expand other features over time. For example, we have heard, ideated and experimented with dozens of different ideas related to Quality of Service, but bringing them on-chain takes time and requires finding concrete solutions to various nuances. Offloading core blockchain building blocks to other frameworks in a modular fashion lets us be more productive and collaborate more closely with our community on our specialization. Similar to how Portal (by Valve Corp.) was a great game because it nailed one key game mechanic, we can do the same with Pocket’s utility. In fact, tokenizing gateways (now known as portals) was an [idea first brought](https://github.com/pokt-network/pocket-network-protocol/issues/14) up by one of our community members, [@shane8burger](https://twitter.com/shane8burger).

# Special Thanks 🙏

Shoutout to Matteo for the meticulous edits as well as the protocol team for related discussion and review: Bryan, Dylan, Harry, Dima, Rampey and Red0ne.

Special thanks to Valeriy at [1kx](https://1kx.network/), Adi at [Informal Systems](https://informal.systems/), Cem at [Sovereign Labs](https://www.sovereign.xyz/) and Kautuk at [Stackr](https://www.stackrlabs.xyz/) who jumped on calls, provided a ton of support along the way, and helped review this post.

If you liked this content and want to read more from me, you’ll find my substack [here](https://olshansky.substack.com/).

# Bonus

I assume some people might ask: “_What should our team choose?”._ This isn’t an easy question, but below is an opinionated decision tree that does not take lots of things (tooling, maturity, interoperability, security, etc…) into account, but can hopefully help as a rough starting point.
