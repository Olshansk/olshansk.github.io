---
title: "5P;1R — Bitcoin’s Elliptic Curve Cryptography"
date: 2022-04-23T15:26:37-07:00
draft: false
description: "This is the first of a potential series of articles I want to call “5 points & 1 resource” (think tl;dr but 5p;1r) where I summarize a…"
tags: ["bitcoin", "elliptic", "curve"]
categories: ["cryptocurrency", "technology", "machine-learning"]
medium_url: "https://medium.com/@olshansky/5p-1r-bitcoins-elliptic-curve-cryptography-196fc74a1bf1"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

### 5P;1R — Bitcoin’s Elliptic Curve Cryptography

This is the first of a potential series of articles I want to call “ _5 points & 1 resource_” (think tl;dr but 5p;1r) where I summarize a list of bullet points that would have helped me start learning a new topic. It is intentionally far from a complete source of data.

1.  This is an **Elliptic Curve** : `y^2 = x^3 + ax + b`; see the continuous function Image 1.
2.  **Elliptic Curve Cryptography** is defined over a **Finite Field** (very large prime) **p** along with a **Generator Point**((x,y) coordinate) **G like so** : `y^2 ≡ (x^3 + ax + b) mod p` ; see the scatter plot Image 2.
3.  Bitcoin uses a **secp256k1** , which is an Elliptic Curve with carefully selected parameters to achieve certain security guarantees:
    • `a=0
`• `b = 7
`• `p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1
`• `G = 04 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`
4.  A public key **P** (a point on the curve) is just a private key **pk**(a random integer) multiplied by the **Generator Point (** the pre-selected point on the curve): `P = pk * G.`
5.  The **Elliptic Curve Discrete Logarim Problem** makes it hard to find the integer **pk** when you know (x,y) coordinates of **P** and **G** fitting the equation in (2) using the parameters in (3) or some other elliptic curve.

If I only had to recommend one resource out of all the references I looked through, it would be: <https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#the-generator-point-in-ecc>

![Elliptic curve over real numbers showing continuous smooth curve](/images/posts/2022-04-23-5p1r-bitcoins-elliptic-curve-cryptography-image-01.png)

Image 1: Elliptic curve over real numbers

![Elliptic curve over a finite field showing discrete points in a scatter plot](/images/posts/2022-04-23-5p1r-bitcoins-elliptic-curve-cryptography-image-02.png)

Image 2: Elliptic curve over a finite field

> Join Coinmonks[ Telegram Channel](https://t.me/coincodecap) and[ Youtube Channel](https://www.youtube.com/c/coinmonks/videos) learn about crypto trading and investing

### Also, Read

- [Best Bitcoin Margin Trading](https://medium.com/coinmonks/bitcoin-margin-trading-exchange-bcbfcbf7b8e3) |[ Lolli Review](https://medium.com/coinmonks/lolli-review-e6ddc7895ad8) |[ Bityard Margin Trading](https://coincodecap.com/bityard-margin-trading)
- [Create and sell your first NFT](https://coincodecap.com/create-nft) |[ Crypto Trading Bot](https://coincodecap.com/best-crypto-trading-bots)
- [How to buy Shiba (SHIB) Coin on CoinDCX?](https://coincodecap.com/buy-shiba-coindcx)
- [CBET Review](https://coincodecap.com/cbet-casino-review) | [KuCoin vs Coinbase](https://coincodecap.com/kucoin-vs-coinbase) | [Bybit vs Coinbase](https://coincodecap.com/bybit-vs-coinbase)
- [Fold App Review](https://coincodecap.com/fold-app-review) |[ LocalBitcoins review](https://medium.com/coinmonks/localbitcoins-review-6cc001c6ed56) |[ Bybit vs Binance](https://coincodecap.com/bybit-binance-moonxbt)
- [Crypto Margin Trading Exchanges](https://medium.com/coinmonks/crypto-margin-trading-exchanges-428b1f7ad108) |[ Earn Bitcoin](https://medium.com/coinmonks/earn-bitcoin-6e8bd3c592d9) |[ Mudrex Invest](https://coincodecap.com/mudrex-invest-review-the-best-way-to-invest-in-crypto)
