+++
author = "Daniel Olshansky"
title = "KZG via ECG"
date = "2023-01-22T02:34:00.164Z"
description = "A Source of Entropy for KZG Ceremonies"
tags = ["blog",
    "crypto", "ai", "tech", "research", "investment", "productivity"
]
substack_url = "https://olshansky.substack.com/p/kzg-via-ecg"
+++

\*This is a fun open idea for Ethereum’s KZG Ceremony: **using your Apple Watch’s ECG as a source of entropy to participate in Ethereum’s KZG ceremony**.

I got a response when I first proposed it to the Ethereum foundation in December. Still, it does have some open-ended problems and requires a non-trivial amount of implementation effort. If you find it interesting and have the time to implement it, I’d love to see it come to fruition! \*

_Note that the deadline for submission is [Jan 31st](https://kzgceremony.paperform.co/)_

---

# Common Reference String (CRS) Setup Ceremonies

I remember listening to [Zcash’s setup on Radiolab](https://twitter.com/mineZcash/status/885801001621618688?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E885801001621618688%7Ctwgr%5E40644ae4683ff22b0e28ef4592acdb67c8987de5%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.redditmedia.com%2Fmediaembed%2F6n83nw%3Fresponsive%3Dtrueis_nightmode%3Dtrue) back in 2017 of how their ceremony went down with only [6 participants](https://z.cash/technology/paramgen/). Since then, projects like Aztec, Anoma, Filecoin and now Ethereum are incorporating it into their protocols with hundreds, if not thousands, of participants. Tornado.Cash had [1114 participants](https://tornado-cash.medium.com/the-biggest-trusted-setup-ceremony-in-the-world-3c6ab9c8fffa) in 2020.

The _tl;dr_ of why any of this matters: **The Powers of Tau** ceremony generates parameters to enable proofs (zkSNARKs) that can be verified in **constant time; O(1)**. Most importantly, there only needs to be **one honest participant** for the entire setup to be secure.

We don’t necessarily need **_the one_** participant to generate a secure source of entropy, but rather, **_at least one_** participant that generates, and later destroys, their secure source of entropy. We can all be Neo-Neos.

# Context

In mid-December of 2022, the EF Protocol Team posted about [the KZG Ceremony Grant Round](https://blog.ethereum.org/en/2022/12/15/kzg-ceremony-grants-round). Believing I’d have free time over the holidays, I reached out with an initial version of this proposal.

The Ethereum Foundation (EF) is not looking for solutions that check every box, but different solutions from different groups that check a subset. KZG via ECG captures some goals, requires a discussion around others, and doesn’t focus on just one.

✅ easy to use interfaces
✅ good randomness generation
✅ collect unique forms of entropy
✅ contributes this entropy to the Ceremony
❓auditable code
❓destroys the entropy afterwards
❓ implementations ready for use early in the contribution phase
❓documents the above in a credible/verifiable manner
❌ custom / bespoke BLS implementations

A recent presentation by Carl Beekhuizen shows that their goal is to bias to a larger number of participants rather than be perfectly secure with each one.

- Similarly, in Sam Parker’s [post](https://zeroknowledge.fm/the-power-of-tau-or-how-i-learned-to-stop-worrying-and-love-the-setup/), he states:

> Since then, **the goal of setup ceremonies has been to maximize the number of honest, independent participants who can participate in the scheme**. Because if there are many independent participants, then, intuitively, the likelihood that all are dishonest is reduced to the point of negligibility. Thus, technical innovations were targeted at scaling up the capability of these ceremonies to support the highest number of participants possible.

# **What 🤔 - What’s the proposal?**

This proposal aims to make it easy for 📱 and 🍏⌚ owners to participate in the KZG Ceremony by using their Electrodiagram (ECG) data as a unique entropy source.

# Why 🧐 - Why is this worth considering?

## 1. **Open Source** 📖

The code for the iOS app can be made free, public, auditable and available on GitHub. It can prove the following:

❌ 🌍 **Local:** Raw source data is not transmitted anywhere over the network

❌ 💾 **Destroyed**: Raw source data is not saved locally for later retrieval

Though tech-savvy individuals can download, build and install the application themselves, publishing it on the app store is an easy way to increase the number of participants. To do so, some trust will lie in the publisher: the development team, the Ethereum Foundation (EF), other publishers, etc. \*

## 2. **Apple’s Security** 📲

🍎 **Apple** - Apple is well-known for how much they prioritize user privacy. Unless all network requests from a user’s device are tracked (e.g. using Wireshark) to ensure nothing is transmitted without the user’s permission, I believe it is a fair assumption that Apple does not collect user data. \*

🛋️ **Read-only API**: The [HKElectrocardiogram](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram) API is read-only. Unless everyone who participates via this mechanism roots their device and uses a fork of the software provided to seed the data manually, it can be guaranteed to be non-deterministic.

## 3. **Easy** ✅

Installing the iOS & Apple Watch applications from the app store is easy.

- Any developer with a Mac (iOS dev or not) can build the Open Source Software (OSS) themselves.

- The transmission of data from the application to the sequencer will be embedded and auditable in the code.

- Doing this from mobile devices reduces friction and increases the number of participants.

After users generate their secret, they need to “wait in a lobby” until the sequencer can accept their input. Since Apple Watches and iPhones have easy mechanisms to keep background processes alive, it should be easier than keeping a tab like this open for hours:

-

## 4. Fun 🤡

To randomize data, users can 🕺🏻, 🚴🏻‍♀️, 🏊🏻‍♂️, 🏋🏻‍♀️, 🚶🏻‍♀️or even 😴 to get different sources of randomness reflecting their open body. They can do this individually or in groups.

The only exception is the anti-sibyl mechanism requiring users to have a GitHub or Ethereum account before a certain date:

# How ❓- How does someone participate?

The basic user flow would be:

User presses `Start` on their Apple Watch

- An individual performs some activity

- User presses `Stop` on their Apple Watch

- ECG data is securely sent from their Watch to their Phone; data on the watch is delete

- Follow the BLS specifications outlined [here](https://github.com/ethereum/kzg-ceremony-specs/), or use a compliant library with their API

- Securely send the data to the EF

-

# Cost 💸 - How much does it cost?

I believe this is a 4-week project for two developers, one of whom is design/UX oriented and receive distribution support from the foundation. If the EF provides a sizable grant (e.g. $5K-$10K), they could build a great product to be used in future ceremonies, especially with the help of all the tools we have today (ChatGPT, playgroundai, etc).

It’s been more than a decade since I did any iOS development, so I’m guessing things have changed.

---

\*_ Some of the points above could have a lot of “Devil’s advocate”-type discussion around them. They are not addressed in detail but would need to be evaluated on a risk-reward tradeoff matrix._

---

I got a few good questions back from [Carl Beekhuizen](https://twitter.com/carlbeek), so am diving into some of those weeds below. Unless you plan on building this, I suggest you stop reading now.

> [It] specifies that it "returns a snapshot of all the matching samples currently saved in the HealthKit store.” Which concerns me as to how this data is handled.

What is the trust model you are envisioning here? Is it “Trust Apple ™)” hope no other app requests the data at the same time?

As mentioned, unless we track all in/outgoing network requests (e.g. using Wireshark) and do "_forensic hardware analysis,_" there is some inherent trust in Apple ™.

[Watch-Phone Security](https://support.apple.com/en-ca/guide/security/secc7d85209d/web): The “**Secure pairing with iPhone” section** describes the degrees of security used to ensure communication between the phone and watch is secure.

[iOS Application Sandboxing](https://support.apple.com/en-ca/guide/security/sec15bfe098e/web): The “**Sandboxing”** section describes the lack of cross-app data leaking: _"Sandboxing is designed to prevent apps from gathering or modifying information stored by other apps."_

> hope no other app requests the [ECG] data at the same time?

Though it is unlikely that other apps will have the proper permissions and foresight to start and stop tracking the data in the background, it’s theoretically possible.

The Raw ECG data comes with a [sampling frequency](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/3551983-samplingfrequency) parameter, so we could use a random number (known only to the KZGviaECG application) to **subsample** it.

> Where do you envision the actual crypto computations taking place? Is this something that could be done on the watch (eg using a modified version of this SWIFT BLS crypto library).

For LTE-enabled watches, it could be done on the watch, but the iPhone would need to be involved in the end-to-end flow otherwise.

As a bonus, we could [stream data](https://developer.apple.com/documentation/watchconnectivity/implementing_two-way_communication_using_watch_connectivity) between the watch and the iPhone to introduce several rounds of data randomization. For example:

> Do you plan on mixing in additional entropy from the CSPRNG I assume exists on the watch

The [CSPRNG on iOS](https://support.apple.com/en-ca/guide/security/seca0c73a75b/web) uses some hardware-based sources (random intel instructions, secure enclave hardware, etc...). We could also mix IMU measurements with the ECG data since it’s already readily available.

> Also my understanding of the Apple App Store deployments is that reviewing apps etc can be quite a lengthy process. Do you have thoughts on deploying to the App Store vs self signing?

Several paths can be taken here:

The source code will be published on GitHub so developers can install the application themselves.

- In parallel to (1), anyone can self-sign the application and deploy it on [testflight](https://developer.apple.com/testflight/) so it can be distributed to up to **10,000** users per signer.

- The number of users in (2) is _theoretically_ unlimited if there is enough support from the community.

- In parallel to (3), the EF or the developer can submit the application to Apple for review.

DMs are open at [@olshansky](https://twitter.com/olshansky) if you’re interested in picking this up!

Thanks for reading Olshansky's Newsletter! Subscribe for free to receive new posts and support my work.
