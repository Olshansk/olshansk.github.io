---
title: "Blockchain’s Killer Use Case"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: ["Post"]
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

* * *

### Blockchain’s Killer Use Case

There is a lot of discussion surrounding what the killer app for Blockchain will be. Whatever it is, it’ll have to solve a problem founded on a breach of Data Integrity or in need of more enforceable Non-repudiation.

**Blockchain is not a datastore, it is a ledger**

Trustless, permissionless, 

  


  * Integrity
  * Non-repudiation: Easily enforceable contracts and cannot deny having received a message.
  *   




### Integrity and authenticity are first class citizens of the, and Non-repudiation follows after. Is it worth sacrificing in exchange for the freedom and price of a centralized service

One of the most elegant things about blockchain technology is the amalgamation of existing concepts and solution from several different fields. Game theory, distributed computing, cryptography, decentralized governance, economics holistically come together to create a trustless and censorship-free system. However, this creates many vectors of attack or scrutiny, causing conversations about Blockchain to often lose focus of one specific characteristic. There are a lot of brilliant minds solving a lot of interesting problems to create a scalable and secure foundation, and that’s just one of the many reasons why this industry is so exciting. In the meantime, we’re seeing a lot of individuals thinking about the types of applications that could be built on top of it, but they’re missing the point that unless Data Integrity is a concern, there is no reason to use blockchain as an alternative to traditional centralized systems.

Economics aside, not a lot of these problems will exist in first world countries. Most of the services built by big tech giants would modify your data, because it would cause them to lose business if the information gets out. Similarly, whenever a law-enforced 

A simple way of thinking about Blockchain is as a slow and expensive mainframe that everyone has access to, with a completely public append only database. Discussions of which consensus protocol to choose (Proof-of-Work, Proof-of-Stake, Delegated Proof-Of-Stake, Raft, etc…), whether a certain Blockchain has finality, how it can be attacked, or scaled are all problems related to building the foundation. For the purposes of this discussion, assume that there is a single, secure, sufficiently scalable and decentralized blockchain that will not be attacked or forked. While companies like EOS claim to eventually provide a cheap and scalable solution, I believe it’s unlikely that public blockchains will ever be as fast or or cheap as traditional centralized servers.

  * Assume there is finality.
  * Should I discuss different consensus protocols
  * There is a tradeof between price/security and speed/price



Whenever these exceptions are broke, I will be explicit about it.

PoW: No finality. Expensive to override. slow. Expensive. Really distribtued

Delegated PoS. EOS. SteemIt. BitShares. Quick. Free. Fast. Small (several dozen) of people can collude.

[1] Asking to agree that we have a sufficiently secure, scalalbA blockchain without finality is arguably not immutable. In Bitcoin, history can be rewritten from scratch if someone decides to spend enough compute power to do so. A hard fork or collusion of the miners can also harm the integrity of the data on the blockchain. These are all discussions for another for another post…

### Information Security

Information Security deals with a broad range of subjects related to data security and privacy. There are different sets of principles, which together account for most of the cases. The classic CIA triad encompasses data Confidentiality, Integrity and Availability. It was expanded by Donn Parker in 1998 to the Parkerian Hexad, which also includes Possession/Control, Authenticity, and Utility. In my opinion, this is incomplete unless you also consider Non-repudiation.

A lot of the problems related to Information Security can be solved by [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), which has been around since the 1970s, and doesn’t necessarily need a blockchain. Without delving into the details, public-key cryptography works by generating two keys (text files): a public key and a private key. The public key is shared with everyone, and the private key is kept secret by the owner. Anything that’s encrypted by the public key can be decrypted by the private key and vice versa.

Whenever I make a reference to to the _cloud_ , I’m referring to a traditional centralized 3rd party cloud storage solution or service. This could be any one of Apple, Google, Microsoft, Facebook, Twitter, Dropbox, Box, etc... These are mostly reliable high market cap companies. Whenever I make a reference to _blockchain_ , I’m referring to a secure, scalable, decentralized blockchain with support for Turing complete smart contracts.

  * * I should replace cloud with “centralized cloud”



#### Confidentiality

Confidentiality refers to the limits of who can and cannot access your data. A breach of confidentiality implies that someone gained access to your data without your consent.

Any data stored on the blockchain is completely public and accessibly by anyone with an internet connection. In order to store confidential information on the blockchain, you would have to encrypt it with your public key first. Though the encrypted data is accessible to everyone, it is gibberish anyone who does not have access to the private key: just you. This approach can be extended to share data with a specific set of people using using file specific encryption keys which is discussed [here](https://security.stackexchange.com/questions/71911/pattern-to-allow-multiple-persons-to-decrypt-a-document-without-sharing-the-enc).

Any data you store in the cloud is not secure. Though the company’s User Terms and Conditions may promise to not access your data, they do have access to it. The only way to secure your data is by encrypting it on your local machine before saving it to the cloud.

When it comes to confidentiality, the same approach and the same amount of effort is necessary regardless of whether you’re using the blockchain or the cloud.

#### Possession/Control

Possession/control pertains to who could potentially have access or possession of your information, without necessarily breaking confidentiality. For example, knowing that someone else has a sealed envelope with your bank information even though none of your funds were lost is still a reason for concern.

The moment you store any data on the blockchain, there is an immediate breach of confidentiality since all the data on the blockchain is public. However, since tokens/cryptocurrency is a first class citizen of the blockchain, it’s worth mentioning that your funds are always secure as long as you private key is not compromised.

The moment you store anything to the cloud, the provider of your preferred cloud storage solution has immediate control and possession of your data. If this company is hacked or compromised (Yahoo, Equifax, Sony, Facebook, etc…), then hackers also have access to your information. In the context of banking, your bank has possession and control of your funds. If the bank is closed, shuts down, gets hacked or if everyone decided to withdraw their money at the same time, it is likely that you will lose access to your funds.

Neither blockchain nor cloud solutions are good at helping you matain possession of digital data you want to back up outside of cold storage, but blockchain does a much better job at helping you maintain control of your funds assuming your private key is kept secure.

#### Availability

Availability refers to having access to your information within a timely manner.

Provided that you have an internet connection, you can start up a full node and sync all information that was ever stored on the blockchain. The latency associated with how long it’ll take to retrieve your data or how long it’ll take to commit a transaction will depend on how congested other nodes on the network are, and how closely they’re geolocated to you. The only time you will lose full access to your data is if there the number of nodes or miners drops to zero. [IPFS](https://ipfs.io/) is currently working on building a faster, safer and more open web to solve this exact problem. 

Most of the cloud solutions out there do not suffer availability issues. You establish fast direct connections with their servers, which are up 99.99% of the time. I can recall of only a handfull of cases over over the past few years where Amazon’s AWS or Facebook’s messenger was down. When a data center in a certain geolocation goes down, traffic is rerouted elsewhere. This could cause a bottleneck or increase latency as most a lot of the caches may be cold.

A key distinction between the cloud and blockchain, is that a company could make your data completely unavailable if they choose to lock you out. If the government provides explicit instructions to prevent you from having access to your account, they would most likely have to comply. In order for a similar situation to occur on the blockchain, all nodes would need to unanimously agree to fork from a block prior to which your data was stored, which is extremely unlikely.

I don’t think storing and retrieving your data from the blockchain will ever be as fast or as cheap as alternative cloud solutions. However, there’s the risk of a your cloud provider being able to decide whether or not you should have access to your data at all.

#### Authenticity 

Authenticity refers to the veracity of the ownership of some piece of information. In other words, if I claim to have made a certain statement, how can you be sure if it was really me?

Authenticity is a first class citizen of the blockchain because every single transaction must be signed by a private key. Assuming you’re sure that the private key was not comprised, you are guaranteed that the owner of the key is the author of some transaction or the owner of some piece of data.

Data stored 3rd party cloud storage solutions are often tied to an account, which is tied to an email. While a cloud storage provider could author a piece of data or perform a transaction on your behalf, public-key cryptography can be used to guarantee authenticity with the exception that it’s not built into the system you’re most likely using.

In both cases, the main issue of key security remains unsolved. How do we solve the problem of tying the public key to a specific individual? Do we trust an internet page stating that public key X belong to user Y? Do we trust an audio recording? Do we trust a person we’re speaking to on the phone? Are we sure that someone we’re meeting in person is not be coerced into lying with regard to what their public key is? Authenticity can be solved on both the blockchain and and in traditional centralized services with the same caveats. This is a solved problem in [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) through the use of certificates and trust in about a dozen companies Certificate Authorities. However, assume we have a way to associate a private key to an individual.

#### Utility

Utility pertains to the usefulness of data. Data that cannot be decrypted, or data that was corrupted is deemed “not useful” and therefore implies a breach of utility.

Blockchain consensus follows a very specific set of protocols. If a miner tries to broadcast a misconfigured block, it’ll be rejected by all the other nodes. Since every full node contains the entire history of the blockchain, the data is highly replicated and remain retrievable even if a few of the nodes get corrupted. However, if you encrypted your data with your public key and lose your private key, it will never be accessible again. It is also worth mentioning that your funds are tied directly to your private key, so they will be inaccessible if you ever lose your private key.

A centralized cloud often replicates your data across different geozones, and performs regular backups. It is unlikely that your data will be irreversibly corrupted due to an issue by the service your using. As in the blockchain case, your data will not be useful if you encrypted it and lost the private key. In the context of banking, there are ways retrieve your funds even if you get locked out of your account. These methods might now be completely secure, but they are possible which a lot of people sleep well at night.

#### Integrity

Integrity refers to the correctness and stableness of the information. Unless deliberately authorized, the data stored cannot be changed through accidental or malicious means.

A sufficiently secure and decentralized blockchain is immutable.¹ With the exception of a few extreme cases, history on the blockchain cannot be rewritten. A great use case of this property is [Proof of Existence](http://Any%20https://poex.io/about); allowing you to prove that you owned a certain document or made a certain statement at a specific point in time; it’s great for making predictions or in the “patent” use case. In addition, since every transaction is signed with a private key, it cannot be modified to mean something other than what the original author intended. Together, these two properties guarantee the integrity of your data through both correctness and and existence.

A centralized cloud is not necessarily immutable. Your cloud storage provider could easily go in and change your data if they choose to. However, if you sign everything with your private key, you could guarantee the integrity of your data in a very similar fashion.

#### Non-repudiation

Non-repudiation requires Integrity and Authenticity as pre-requisites and can be split into two parts. The first implies an individual’s conform to a contract, meaning they cannot avoid doing something after signing a contract promising to do so. The second implies an individual’s inability to deny having sent or received a transaction.

Non-repudiation is another first class citizen of blockchains with a smart contract ecosystem. Once a contract has been signed and included in the blockchain, the code associated with it either already has or will be executed and. The only exception to this are [upgradable smart contracts](https://blog.zeppelin.solutions/proxy-libraries-in-solidity-79fbe4b970fd) being developed by organization such as [OpenZeppelin](https://openzeppelin.org/), but that is outside the scope of this discussion. Secondly, since blockchains are entirely public and immutable, it is impossible to deny having sent or received a message.

implies one’s intention to fulfill their obligations to a contract. It also implies that one party of a transaction cannot deny having received a transaction

IThe first implies an individual’s intention to conform to a contract, meaning they cannot deny doing something after a contract has been signed. The second implies, Non-repudiation Any data you store on a 3rd party cloud storage is theoretically safe and can only be 
