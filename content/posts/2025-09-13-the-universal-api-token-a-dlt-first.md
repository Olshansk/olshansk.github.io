---
title: "The universal api token a dlt first"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: []
categories: []
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

https://docs.near.org/build/chain-abstraction/what-is

https://medium.com/@prophet.one/what-is-chain-abstraction-f86c5aa229a0

The purpose of Auth is to:

> Allow others to behave on your behalf (i.e. read / write data) on your behalf

What if we want to allow someone else to:

> Sign on our behalf?

https://simonwillison.net/2024/Oct/14/grant-negotiation-and-authorization-protocol-gnap/

Not your keys, not your relays

Not your keys → Not your relays

[![](https://substack-post-media.s3.amazonaws.com/public/images/a8b5ad06-ef3c-4e5d-a6fe-50b16b82b40a_512x512.png)Squishy ComputerNature's many attempts to evolve a NostrHere is the architecture of a typical app: a big centralized server in the cloud supporting many clients. The web works this way. So do apps…Read morea year ago · 41 likes · Gordon Brander](https://newsletter.squishy.computer/p/natures-many-attempts-to-evolve-a?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

* * *

A recent article on [OAuth from First Principles](https://stack-auth.com/blog/oauth-from-first-principles) caught my attention through the use of cathartic references that hit a cord in my memories.

It starts of with a great example of why we need OAuth by showing an example of a world without OAuth:

[![](https://substack-post-media.s3.amazonaws.com/public/images/433f4c29-dd96-4aeb-b94a-65b4946c013d_3025x1285.png)](https://substackcdn.com/image/fetch/$s_!Lig-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F433f4c29-dd96-4aeb-b94a-65b4946c013d_3025x1285.png)[The world without OAuth](https://stack-auth.com/blog/oauth-from-first-principles#without-oauth)

No matter how sophisticated internet infrastructure becomes, it’s still built on a foundation of having an email address, password, and more recently, passkeys. [1]

In order to Read & Write across different services and data sources, we have a bunch of authentication protocols with varying tradeoffs; API Keys, OAuth, OpenID Connect, LDAP, etc..

In _Web3_ , we talk a lot about how you don’t only Read & Write, but also Own. See @[cdixo](https://x.com/cdixon)n’s [Read Write Own](https://readwriteown.com/). [2]

In case you’re _crypto-allergic_ , keep reading. This isn’t about pushing a cypherpunk philosophy. It’s about how we use a few cryptographic primitives

[![](https://substack-post-media.s3.amazonaws.com/public/images/7f41c365-b0f5-42ef-8d05-befeb0537ceb_607x445.png)](https://substackcdn.com/image/fetch/$s_!TnBP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f41c365-b0f5-42ef-8d05-befeb0537ceb_607x445.png)

Our work at [grove.city](http://grove.city) on [pokt.network](http://pokt.network)

https://en.wikipedia.org/wiki/Public_key_infrastructure

One of the core value propositions I’ve been in the web3 space for a little while now and though I haven’t read Chris Dixon’s [Read Write Own](https://readwriteown.com), 

What this provides:

  * Annonimity

  * Single signature

  * Multiple providers




Mention Chris Dixon’s read-write-own book.

https://stack-auth.com/blog/oauth-from-first-principles

https://www.nango.dev/blog/why-is-oauth-still-hard

https://dev.poktroll.com/protocol/primitives/gateways#relay-signatures

AATs: https://discord.com/channels/824324475256438814/997160443300814918/1272691640611639347

* * *

[1] I’m intentionally avoiding the topic of password security and privacy. Personally, I’m still amazed how many people don’t use a password manager in 2024.  
  
[2] I reference cdixon’s’ book but have to call out I haven’t actually read it. However, having been in the crypto space since 2016 and following him for years, I can guess what the sentiment is. I just wanted to make a reference to the catchy title.  
  
[3] 

### [1] Assumptions

**Social recovery** : https://vitalik.eth.limo/general/2021/01/11/recovery.html

**Worldcoin** : https://worldcoin.org/

Assumption: There is a **distributed ledger**

### [2] Alternatives

**Aptos keyless** : https://aptos.dev/en/build/guides/aptos-keyless

**Web3Auth** Shamir Secret Sharing, Threshold Cryptorapy and MPC: https://web3auth.io/docs/how-web3auth-works

**Delegation:** Just on-chain delegation
