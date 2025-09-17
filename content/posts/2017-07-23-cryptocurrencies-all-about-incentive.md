---
title: "Cryptocurrencies: It's all about incentive"
date: 2017-07-23T17:16:04.361Z
draft: false
description: "One of the major selling points of cryptocurrencies is that everything is decentralized and trust no longer lies in single a third party…"
medium_url: "https://medium.com/@olshansky/cryptocurrencies-its-all-about-incentive-77ac47a6adc4"
tags:
  ["cryptocurrency", "bitcoin", "ethereum", "incentives", "economics", "tokens"]
---

![Cryptocurrency concept image](/images/posts/2017-07-23-cryptocurrencies-all-about-incentive-image-01.jpeg)

One of the major selling points of cryptocurrencies is that everything is decentralized and trust no longer lies in single a third party. However, the trust didn't simply dissipate, it got distributed to participants of the network. In my opinion, the incentive structure built into cryptoeconomics is one of its most overlooked benefits. The fundamental idea can be summarized as follows: **no one wants to lose money, and everyone wants to maximize the profit they receive for the work that they do.**

Below are a few different examples of the role that financial incentive plays in various aspects of cryptoeconomics.

## Bitcoin

In Bitcoin, miners insert a _Coinbase_ transaction into every block that they mine. This transaction mints new coins and assigns them to the miner in exchange for the work that they did. This block is then broadcasted onto the network, validated by other full nodes, and appended to the blockchain if it's valid. If the miner were to include a non valid transaction in the block, other nodes would reject it, the miner would not been granted the newly minted coins, and all that work would have gone to waste. The miner is therefore incentivized to only expand energy on generating valid blocks.

## BIP148

At the end of this month, BIP148 UASF may or may not be activated enabling some new rules in Bitcoin. If all the nodes in the network agree to reject blocks that do not support the new rules, any miner that expands energy generating blocks according to the old rules would be wasting it. Assuming the users (full nodes) reject such blocks, miners will be incentivized to follow the new set of rules.

## Schelling Coins

One of the challenges blockchain technologies are going to face is the concept of an Oracle: a mechanism by which real world data (i.e. the weather at some location at some point in time) is inserted into the network. Vitalik Buterin discussed the concept of [Schelling Coin](https://blog.ethereum.org/2014/03/28/schellingcoin-a-minimal-trust-universal-data-feed/)s in one of his older posts as one potential solution to this problem. Assume you posed the following question to the Ethereum network: "How many planets are there in the solar system?". Every individual who wants to answer the question must deposit 1 ETH, and will get back 1.01 ETH if their answer is correct. If their answer was wrong, they will forfeit the deposit. After a sufficient number of responses has been collected, the answer with the highest frequency, which is probably 8, is accepted as "the truth". Anyone who answered anything other than 8 will lose their deposit. Since all the individuals participating in this survey assume that everyone else is going to answer the question truthfully, and would rather gain a small amount of ETH rather than losing a big chunk, they are incentivized not to lie.

## Tokens

With the recent surge in ICOs, one of the most common questions being asked is whether all these tokens are necessary at all. With Bitcoin available as a safe store of value and medium of exchange, why do we need so many alternate application-specific tokens?

To answer this question, take FileCoin as an example. FileCoin, a decentralized storage network built on top of IPFS, is going to have an ICO in the coming weeks. To achieve a truly distributed data store, their network will require many nodes spanning the whole globe to sign up as storage providers. Those individuals who will configure and offer their hardware to host files will be rewarded with FileCoins. Since it's going to be possible to trade FileCoins for BTC/ETH (and in turn USD), why not pay these individuals in BTC directly? A greater network effect and influx of new sign ups is more likely to take place if early adopters are incentivized by a new form of currency rather than a well established one due to the greater potential financial upside. Similar to how stock at a large public company is unlikely to double in a short period while the valuation of a startup could go up several fold in the first few years of it's existence, FileCoin is more likely to experience more growth than BTC in the same time period. Therefore, developers and early adopters of IPFS are more incentivized to be paid by something other than BTC.

I highly recommend listening to Olaf Carlson-Wee's [answer](https://youtu.be/9SYVX2wcMVM?t=20m13s) on this subject matter as well.

## Twitter

If Twitter were being developed from the ground up today, I believe it would have some sort of token structure in place. In my opinion, there are many opportunities where a Twitter Token (TWT) could be used to provide financial incentive for users to generate better content, create less spam, aid in better curation and promote stronger network effects.

For example, Twitter currently has a feature that allows users to create moments (a curated list of tweets). However, unless the curator is doing this out of their own interest, or if the curator includes sponsored tweets, they have no incentive to do a good job. If users had to pay a small fraction of a TWT to view a moment, and the curator received that payment in return, there is an immediate incentive for the curator to put more effort into content curation. Rather than creating clickbait titles for more ad views, the incentive for producing better content is built directly into the platform. Arguably, users would also be more invested and engaged with the content after having to spend a small fraction of a TWT to view it.

It's worth noting that while financial incentives are necessary for a cryptocurrency to operate properly, they are "nice to have" in some of the other examples I highlighted. The benefit of using Ethereum to implement this feature is because tokens are a first class citizen of the platform, a [standard](https://theethereum.wiki/w/index.php/ERC20_Token_Standard) has already been developed, and it's easily exchangeable for other tokens (services).
