---
title: "GATE: Gateway Abstraction Technical Elements — Annotated Presentation"
date: 2025-03-08T23:27:05-07:00
draft: false
tags: ["crypto"]
categories: ["Technology", "Cryptocurrency"]
summary: "I recently gave a talk at dinfra.xyz, a side event hosted by 1kx.capital alongside Denver's annual ETHDenver conference."
medium_url: "https://medium.com/@olshansky/gate-gateway-abstraction-technical-elements-annotated-presentation-2c1ee2e27373"
---

### **GATE**: Gateway Abstraction Technical Elements — Annotated Presentation

I recently gave a talk at [dinfra.xyz](https://dinfra.xyz/), a side event hosted by [1kx.capital](https://1kx.capital/) alongside Denver's annual [ETHDenver](https://www.ethdenver.com/) conference.

In my honest opinion, this is the most serious and highest-quality side event of the week.. It bridges ideas related to decentralized systems, cryptography in and out of web3 (aka "crypto" space).

The [list of speakers](https://dinfra.xyz/) includes individuals like Kurt Rohloff (founder of [openfhe.org](https://openfhe.org/)), Sam Williams (founder of [Arweave](https://arweave.org/)), Ed Felten (Princeton University Professor and co-founder of [Arbitrum](https://arbitrum.io/)), among many others. The opportunity to share a stage with these individuals is an honor.

You can find the [presentation on YouTube](https://www.youtube.com/watch?v=8Axy3TF_Itk&t=5s) for the full 12 minute talk. This is a [Simon Willison](https://medium.com/u/d0634905149a) [inspired annotated presentation](https://simonwillison.net/2023/Aug/6/annotated-presentations/), in case you just want to read or scroll through the pictures.

![GATE Introduction Slide](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-01.png)

For context, anyone who works in a technical capacity in an internet-adjacent industry has likely heard or used the term "**Gateway.**" I wouldn't say it's overused, but it means different things to different people.

I start by introducing myself as Olshansky, with a quick reminder that my first name is Daniel.

After years of thinking about the problems Gateways solve, I decided to kickoff the **GATE Framework**: **Gateway Abstraction Technical Elements.** It's a starting point to create a shared language so we can categorize and classify the problems, solutions and elements involved.

I proceed to make a _very funny joke:_ a screenshot of me [presenting](https://www.youtube.com/watch?v=jVW-3lRzVT0) at [d/infra last year](https://dinfra.xyz/2024), which includes a screenshot of me [presenting](https://www.youtube.com/watch?v=7rQ4Awfx79g) at ETHDenver the year before, which itself has a screenshot of me [presenting](https://www.youtube.com/watch?v=cjuDDdiMbMQ) at ETHDenver the year prior to that.

![Presentation History - Recursive Screenshots](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-02.png)

Abstractions, Gateways, Trust Delegation, Ring Signatures and [GNAP](https://datatracker.ietf.org/doc/rfc9635/) ([oauth.xyz](https://oauth.xyz/)) are on the agenda.

The most likely reason why I even got into this side event is because I [nerd-sniped](https://www.urbandictionary.com/define.php?term=Nerd%20Sniping) our audience by the fact that we use [Ring Signatures](https://en.wikipedia.org/wiki/Ring_signature).

Technical audiences often get wary of new standards. I reiterate and assure everyone that my goal isn't to create a new standard, but to provide a framework, a language, for what already exists. Too many things are conflated into the term **Gateway**.

![Don't Worry - Jackie Chan Assurance](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-03.png)

To double down on the assurance, I brought in Jackie Chan. He can save us from anything while also providing some comic relief.

![Core Abstractions](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-04.png)

We kick things off by talking about the core abstractions used and discussed in the crypto industry.

I'll provide a very quick summary of the three below, but you can skip to the next slide as long as you remember this: **Gateway Abstraction is the off-chain bridge between Account Abstraction, which is on-chain, and Chan Abstraction, which is cross-chain.**

1. [**Account Abstraction**](https://ethereum.org/en/roadmap/account-abstraction/) **(_On-Chain_)**: Convert Externally Owned Accounts (EOAs) into Smart Contract Wallets (SCWs) to enable social recovery, gas sponsorship, etc… The implementation is pretty straightforward via a UserOperation pseudo-transactions in a separate mempool and most wallets have support for it. Lots of easy to learn details at [erc4337.io](https://www.erc4337.io/) if you want to learn more.

2. [**Chain Abstraction**](https://docs.near.org/chain-abstraction/what-is) **(_Cross-Chain_)**: This is a little more amorphous and ill-defined. The high-level goal of "intents" is to make it seamless to send and receive different currencies, across different blockchains, without having any visibility of what happens in the middle. I won't get into the details here, but the [CAKE Framework](https://frontier.tech/the-cake-framework) does a great job at capturing the complexity and necessity of this.

3. **Gateway Abstraction (_Off-Chain_)**: This is the piece that Web3 (Crypto) industry inherited from traditional Web2 (Internet) industry. This is the core technology that everyone takes for granted. But, without this product, nothing works. It spans quality-of-service, SLAs, load balancing, user authentication, rate limiting, etc…

![Web2.5 - Gateway Abstraction](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-05.png)

I refer to Gateway Abstraction as Web2.5 because it's responsible for enabling Web3 products by bridging Web2 technology.

I also call out that nothing I'm saying so far is new or innovative. Moxie, the founder of [Signal](https://signal.org/), wrote about this over three years ago in his instant classic [Web3 First Impressions](https://moxie.org/2022/01/07/web3-first-impressions.html).

He called out that the entire distributed and permissionless blockchain industry is accessed via two centralized and permissioned Gateways (i.e. service providers): [Infura](https://www.infura.io/) and [Alchemy](https://www.alchemy.com/).

Over the past three years, in some ways, everything has changed, and in other ways, nothing has changed. Most crypto applications still use centralized and permissioned gateways, but instead of two, we have hundreds. In fact, 1kx, the organizer of this event, has a [dashboard](http://atlas.1kx.capital/) that compares their performance.

![Conspiracy Keanu - Gateways](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-06.png)

Now that we're done talking about abstractions, it's time to move on to Gateways.

This meme is called "[Conspiracy Keanu](https://thefunnyist.fandom.com/wiki/Conspiracy_Keanu)". I thought it was appropriate because while Gateways are an abstract and overloaded term, they're definitely not a conspiracy.

![Why Do We Need Gateways?](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-07.png)

Before we zoom into concrete problems and solutions Gateways tackle, I wanted to zoom out into why we need them at all.

Gateways enable [Remote Procedure Calls (RPCs)](https://en.wikipedia.org/wiki/Remote_procedure_call). It enables a Client to **C**all a **P**rocedure **R**emotely on a Server. RPCs are the "medium of communication," and on top of that we have [Application Programming Interfaces (APIs)](https://en.wikipedia.org/wiki/API), which are the various languages that different services use.

Anyone who has ever gone to one of my talks has likely seen me bring up **The RPC Trilemma**. I first presented at [Stanford Blockchain 2022](https://x.com/olshansky/status/1566402344455217157) and I won't give up until it catches on.

Everything we need from a **R**emote **P**rocedure **C**all (RPC) is for it be **R**eliable, **P**erformant and **C**ost-Efficient (RPC Trilemma). All the other things (permissiones, incentives, etc) fall somewhere in between.

![RPC Trilemma](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-08.png)

I spent quite a bit of time looking for an online categorization of Gateways.

The single best resource I could find is [a post by ByteByteGo on API Gateways](https://blog.bytebytego.com/p/api-gateway). It's not very simple, and it's isolated to just one particular aspect of Gateways.

With that said, I did come across some cool findings during my research. [CloudFlare](https://www.cloudflare.com/), on average, [handles 46 million requests per second](https://blog.cloudflare.com/scalable-machine-learning-at-cloudflare/). This value is from mid 2023, so I wouldn't be surprised if its nearing 100M soon.

This is just one, of many, Gateways out there and it excludes the hyperscalers with multi billion dollar cloud services; Google, Amazon, Microsoft, etc. This really underlines the magnitude of the problem Gateways serve, and how large the opportunity is.

![GATE Framework Introduction](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-09.png)

Since a general-purpose framework to classify and categorize Gateways does not exist, I decided to create one myself.

With the help of my friends — Claude, Perplexity and ChatGPT — we came up with the GATE Framework. It is composed of 4 layer: **Entrypoints**, **Guards**, **Couriers** & **Translators**. It is important to call out that services most Gateways provide likely span across more than one layer, but the nuances can be discussed in a separate forum.

The beauty of this is that it applies to products, projects, services and frameworks in both Web3 and Web3.

I call out a few concrete examples the audience may be familiar with just to help build a mental model:

- **Web2 Entrypoints**: [Envoy](https://www.envoyproxy.io/) & [Kong](https://konghq.com/)
- **Web3 Entrypoints**: [Grove](https://grove.city/) & [Infura](https://www.infura.io/)
- **Web2 Couriers**: [Tor](https://www.torproject.org/) & [Signal](https://signal.org/)
- **Web3 Courier**: [Pocket](https://pokt.network/) & [Nostr](https://nostr.com/)

![Halfway Through - Still An Unsolved Problem](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-10.png)

_We're halfway through the presentation at this point._

I've been talking about Gateways, Abstractions, RPCs, but why does any of this matter?

**It's still an unsolved problem.**

Everyone agrees that the problem exists. Everyone discusses it. No one argues against it. But, a concrete framework to _"solve it"_ has not been defined.

![Examples of Gateway Problems Being Called Out](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-11.png)

I present three concrete examples where other projects and ecosystems call this out.

Calling this out is critical to show that the problem is not being ignored, but you can skip to to the next slide to get closer to the meat of the presentation.

Three concrete examples from the Web3 industry where gateways are called out include:

- [Consensys](https://consensys.io/): One of the companies leading R&D for the Ethereum ecosystem leading companies [explicitly calls out the following](https://consensys.io/blog/enabling-collaborative-collective-improve-security-web3):

> A paradigm shift is required to operate within this scheme […]. In the proposed model, a gateway serves as an optional module installed by the operator of a blockchain node, designed to facilitate secure interactions between clients and the blockchain relayer.

- [Ar.io](https://ar.io/): Arweave, [a permanent information storage network](http://permanent%20information%20storage/), has a whole ecosystem called ar.io dedicated to the [support and proliferation](https://docs.ar.io/) of Gateways built on top of Arweave.

- [Nostr](http://nostr.com/): Nostr is a simple, open protocol that enables global, decentralized, and censorship-resistant social media. When it comes to running a relayer (i.e. a courier in the GATE framework), this is what [they have to say](https://nostr.com/relays):

> Should I run my own relay?
>
> For most people, no, it's better to just pick a few public relays or relays from people you know and trust, or even relays that offer paid services.

![Audience Engagement Survey](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-12.png)

_This is the last slide before I put everything together and show our approach to solving one small piece of this very big puzzle._

I wanted to get some audience engagement by having everyone raise or lower their hands, but I only learnt the day prior that my time slot was reduce from 15 minutes to 10 minutes. Luckily, they ended up giving me 12.5 minutes on stage.

The idea here was to have me predict if a majority of audience (🟢), about half the audience (🟡) or a minority of the audience (🔴) take these factors into consideration when selecting a Gateway (i.e. a service provider) for the [Blockchain RPC nodes](https://help.coinbase.com/en/coinbase/getting-started/crypto-education/glossary/rpc-node).

This was also my opportunity to promote the services we're building at Grove. Check it out at [grove.city/pricing](http://grove.city/pricing) 😉

![Let Him Cook Meme](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-13.png)

This is the "[Let Him Cook](https://knowyourmeme.com/photos/2488659-let-him-cook-let-that-boy-cook)" meme because the buildup of all the context we've been cooking is heating up. 🧑‍🍳️🍳🌡🔥

![Cheque Analogy - Onchain, Offchain, Cross-chain](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-14.png)

We're going to use a cheque (aka a check) as an analogy to put everything together. Assume we have an individual who wants to send funds from one account to another.

On the bottom left of the image, _onchain_, what a individual/user does is:

1. Take a cheque — Prepare a transaction
2. Specify the balance transfer — Specify the tokens to send
3. Agree to pay the wire fees — Agree to pay the gas fees
4. Sign the check — Sign the transaction

On the bottom right of the image, _cross-chain_, what the banks/blockchains do is:

1. Validate the check — Validate the transaction
2. Settle the balance transfer— Settle the token transfer
3. Collect the wire fees — Collect the gas fees
4. Abstract away any details relate to crossing the boundaries of different banks, institutions, geographic, geopolitical, or blockchains.

In the top middle part of the image, _offchain_, the Gateways do everything else:

1. Put the check in an envelope — Provide a mechanism to submit the Transaction via an RPC
2. Drop in in the mailbox — Accept the RPC Request
3. Sign the envelope — Sign the RPC Request
4. Pay for the postage stamp — Pay for the API Request
5. Pass it to a mailman/courier — Proxy the request over the internet
6. Ensure delivery to the destination bank or blockchain
7. Receive acknowledgment of settlement — Recieve a signed RPC Response

![Gateway Trust and Payment Problems](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-15.png)

This whole end-to-end process makes a lot of assumptions and leaves a lot of details left to figure out. For example:

1. Who pays for the stamp? Who pays for the RPC request?
2. Who signs the envelope? Who signs the RPC Request?
3. Who operates the mailbox? Who operates the Gateway entrypoint?
4. Who operates the mailman? Who operates the Gateway courier?

The entire Crypto Web3 industry has been using traditional Web2 style solutions to tackle this. This includes things like [OAuth](https://oauth.net/2/), [JWT](https://jwt.io/)s, basic [API Keys](https://en.wikipedia.org/wiki/API_key). **In short, the trust and payment model for delivering these messages has not evolved at all.**

I proceed to make another _very funny joke_ that regardless of how decentralized or distributed blockchains are, we are never going to be able to fully obfuscate the need to remove a hard-coded hostname or IP address. Whether it's your [seed node](https://academy.bit2me.com/en/que-es-un-nodo-semilla/), or address book, the trusted endpoints are here to stay.

![Distributed Ledger Technology Solution](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-16.png)

Finally, I'm going to show a solution to a small part of this big puzzle!

To do so, I'm going to bring back a narrative that was really popular in 2017: [Distributed Ledger Technology (DLT)](https://www.investopedia.com/terms/d/distributed-ledger-technology-dlt.asp).

The beauty of a blockchain is that it can act as a permissionless, non-interactive, distributed directory (i.e. a bulletin board) of public keys belonging to various users and institutions. Think of it as a bulletin board of public keys.

_Note: I'm assuming the audience (and you — the reader) are familiar with [Public Key Cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) and [Public Key Infrastructure (PKI)](https://en.wikipedia.org/wiki/Public_key_infrastructure). Not going to dive into those details here._

In turn, at any point in time, a user can freely submit an onchain transaction that either delegates or undelegates trust from their personal public key to any public keys belonging to other actors. In our case, these other actors are institutions maintaining Gateways. This can be done any number of times at any point in time.

Unlike other trust delegation approaches I've seen, this doesn't require complex setups like [Shamir Secret Sharing (SSS)](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing), [Threshold Cryptography](https://en.wikipedia.org/wiki/Threshold_cryptosystem), or [Multi Party Computation (MPC)](https://en.wikipedia.org/wiki/Secure_multi-party_computation).

![Trust Delegation via Blockchain](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-17.png)

Next, we're finally going to use ring signatures to create an abstraction for the **Universal API Key**!

[Ring Signatures](https://en.wikipedia.org/wiki/Ring_signature) were invented in 2001 and were heavily popularized by the [Monero blockchain](https://www.getmonero.org/resources/moneropedia/ringsignatures.html).

Here's how it works:

1. Take the public key of the user
2. Take the public key of everyone the user delegated trust to
3. Form a ring
4. Any one (doesn't matter which one) actor in that ring can now sign the message
5. That's it

It doesn't matter who signed the message (i.e. the envelope), it's impossible to determine who signed it, and anytime a new actor joins or leaves the ring, we don't need complex setups to recreate it.

**This anonymous ring signature acts as a Universal API Key where the ownerships, onus and trust of signing the message and paying for it is delegated by the user to one more Gateways at once.**

![Ring Signatures - Universal API Key](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-18.png)

I'm going to tie it back to the original slide:

1. The user has a blue private & public key
2. The Gateway Entrypoint has a green private & public key
3. The golden key is the universal API key representing the ring formed by the green and blue kes
4. When signing the envelope and paying for the stamp, we use the golden key so the courier and destination bank don't know whether it was the user or Gateway that did so, nor does it matter!

![Photo from the Event](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-19.jpeg)

But wait, there's one more very exciting thing I need to share!

_This was also a pretty cool photo taken at the event, so I figured I'd insert that directly instead of the original slide 😁_

![GNAP - Grant Negotiation & Authorization Protocol](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-20.png)

In 2019, [Justin Richer](https://medium.com/u/ce3fbf1372f2) did a presentation on [Transactional Authorization](https://www.youtube.com/watch?v=U9i7YaN8v9c) at [Identiverse](https://identiverse.com/). The core idea was to present a path forward to _"OAuth 3"_ called GNAP (Grant Negotiation & Authorization Protocol), that is not directly backwards compatible with _OAuth 2_.

Over the years, a lot of the core ideas that started GNAP have made their way back to OAuth, but there are a lot more to come. Justin recently wrote about it [here.](https://justinsecurity.medium.com/gnap-a-conversation-of-authorization-5b603d850fe9)

More importantly, GNAP itself recently got an official [IETF RPC published](https://datatracker.ietf.org/doc/rfc9635/):

> The Grant Negotiation and Authorization Protocol (GNAP) defines a mechanism for delegating authorization to a piece of software and conveying the results and artifacts of that delegation to the software. This delegation can include access to a set of APIs as well as subject information passed directly to the software.

When you dive into the details, you learn that there are multiple ways to approach some of the open problems remaining. How do you delegate? How do you keep things as simpe and non-interactive as possible? How do you manage a directory of public keys and identities?

I think there's a really big opportunity to connect the ring-signature based universal API key, with GNAP and a distributed ledger for us to not only bridge Web2 products and technologies Web3, but bridge Web3 OAuth to back to Web2.

![Thank You Slide](/images/posts/gate-gateway-abstraction-technical-elements-annota-image-21.png)

That's it. Putting this together took a lot more time than I expected, but I hope it was worth the read!

If you somehow managed to make it this far, and want to work together or learn more, send me an email at either [olshansky.daniel@gmail](mailto:olshansky.daniel@gmail) or [olshansky@grove.city](mailto:olshansky@grove.city).

If you want to _"hop on a call"_, I would prefer that we exchange a few voice notes first. Feel free to send those on telegram: [t.me/dolshansky](https://t.me/dolshansky)

Again, thank you to [1kx.capital](https://1kx.capital/) for hosting [dinfra.xyz](https://dinfra.xyz/), the opportunity to speak, aggregating brilliant minds for conducive discussions, and some great swag as well.
