---
title: "Gateway abstraction"
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

Convo with Wei

  * See message with DAI Wei

  * What else will use them for?

  * Anonymous sampling of

  * We can do ZK eventually, but for now we e can ship something without worrying about performance

  * Yes. The private key is essentially the API key. The one responsible for paying for RPC services. You can’t embed it on clients, unless you choose to be completely sovereign (privacy Maxie’s). I see it as a web3 first approach to OAuth that uses DLT+RingSignatures instead of an interactive auto service. <https://stack-auth.com/blog/oauth-from-first-principles>

  * Could this be oauth4 with our ring signature approach?

    * https://simonwillison.net/2024/Oct/14/grant-negotiation-and-authorization-protocol-gnap/#atom-everything

  * It’s a problem in the current version of pocket (Morse) that we haven’t really been able to solve yet

  * I also see this as being the web3 first approach to OAuth3 (still in the proposal stages): <https://www.rfc-editor.org/rfc/rfc9635>

**[www.rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9635)**

  * The Grant Negotiation and Authorization Protocol (GNAP) defines a mechanism for delegating authorization to a piece of software and conveying th...

06:54 AM

  * I see it as a way of turning the private key into a “universal API key” that enables non interactive delegation. There’s definitely a paper that can be written here at some point, but just not something that’s a priority right now. It’s why a presentation could be fun and useful




Tenative Prsentation:

  * I slide on Ring signatures

  * I slide on how Cloudflare does this

  * I slide on how it works in Morris and Wei interactive

  * I slide on the fact that the distributor ledger narrative has gone away

  * I slide on one arrow, which is the inspiration for all of

  * A slide showing Jason Webb token and static KPI tokens and other things

  * I slide on how everyone uses zero off and even us and gateways

  * I slide on the new Simon Wilson block post on how they want to do often in the future

  * I slide on how we ended together with something like preview, which is the leader and user accounts right now

  * I slide showing how would release to chain obstruction and account abstraction, and how necessary middleground

  * Show other centralized gateways, and how this actually enables you to use multiple because things are actually decent information with




Rough Notes

  * Between Account attraction the left and hand on the right is where we have gateway attraction in the middle.

  * Ring Signatures

  * Refer to Privy: https://x.com/privy_io/status/1805982382098440332?s=46&t=8olZxrFxcm2TYFP8K5upkg

  * Refer to Account Abstraction

  * Refer to Chain ABstraction

  * Explain that gateways aren’t going anywhere

  * Went to conferences

  * Everyone hardcodes an RPC link

    * You’ll always need to 

    * Even for a light client

    * There’s no way around it

    * It’s about optionality

  * Show what we do with gateways

  * Show we we do with ring signatures

    * Come up with the best terms

    * Explain what PATH does

    * Explain what theprotocol does

  * Come up with good names for all the different modes




@red.0ne @arash.d I know all the "mode" conversations are tiresome and a bit abstract, but I think what we're defining as "Gateway

**Account Abstraction**:

\- https://ethereum.org/en/roadmap/account-abstraction/

\- https://www.coinbase.com/learn/crypto-glossary/what-is-account-abstraction-and-why-is-it-important

**Chain Abstraction**:

\- https://app.devcon.org/schedule/DCSCA7

\- https://docs.near.org/build/chain-abstraction/what-is

**Gateway Abstraction**: https://dev.poktroll.com/protocol/primitives/gateways

[![](https://substack-post-media.s3.amazonaws.com/public/images/33af4a67-f135-4391-ab89-7ae1014edb6a_887x706.png)](https://substackcdn.com/image/fetch/$s_!-WIj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33af4a67-f135-4391-ab89-7ae1014edb6a_887x706.png)
