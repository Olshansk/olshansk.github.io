+++
author = "Daniel Olshansky"
title = "5P;1R - Bitcoin's Elliptic Curve Cryptography"
date = "2022-04-14T21:13:35.645Z"
description = ""
tags = [
    "crypto", "ai", "book", "5p1r"
]
substack_url = "https://olshansky.substack.com/p/5p1r-bitcoins-elliptic-curve-cryptography"
+++

This is the first of a potential series of articles I want to call “_5 points & 1 resource_” (think tl;dr but 5p;1r) where I summarize a list of bullet points that would have helped me start learning a new topic. It is intentionally far from a complete source of data.

---

- This is an **Elliptic Curve**: `y^2 = x^3 + ax + b`; see the continuous function Image 1.

- **Elliptic Curve Cryptography** is defined over a **Finite Field** (very large prime) **p** along with a **Generator Point **((x,y) coordinate) **G like so**: `y^2 ≡ (x^3 + ax + b) mod p` ; see the scatter plot Image 2.

- Bitcoin uses a **secp256k1**, which is an Elliptic Curve with carefully selected parametesr to achieve certain security guarantees:

`a = 0`

- `b = 7`

- `p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1`

- `G = 04 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

- A public key **P** (a point on the curve) is just a private key **pk **(a random integer) multiplied by the **Generator Point (**the pre-selected point on the curve): `P = pk * G.`

- The **Elliptic Curve Discrete Logarim Problem** makes it hard to find the integer **pk** when you know (x,y) coordinates of **P** and **G** fitting the equation in (2) using the parameters in (3) or some other elliptic curve.

---

If I only had to recommend one resource out of all the references I looked through, it would be: [https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#the-generator-point-in-ecc](https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#the-generator-point-in-ecc)

---

## Image 1Image 2
