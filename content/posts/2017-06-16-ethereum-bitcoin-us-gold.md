---
title: "Ethereum is to Bitcoin as the US is to Gold"
date: 2017-06-16T02:45:36.623Z
draft: false
description: "This post was originally written as a follow up email to this tweet where one of the hosts of The Investor's Podcast ran a poll regarding people's thoughts on Bitcoin."
medium_url: "https://medium.com/@olshansky/ethereum-is-to-bitcoin-as-the-us-is-to-gold-b35131565392"
tags: ["ethereum", "bitcoin", "cryptocurrency", "blockchain", "economics"]
---

This post was originally written as a follow up email to [this tweet](https://twitter.com/PrestonPysh/status/868983834255147009) where one of the hosts of [The Investor's Podcast](http://theinvestorspodcast.com) ran a poll regarding people's thoughts on Bitcoin.

— — — — — — — — — —

To provide a fair comparison between Ethereum and Bitcoin I will start by defining the basics, and expand on how each of them can be used without drilling down too deep into the technical details

A transaction is some change of state. This could be the transfer of value from one individual to another, the delivery of a private message, the broadcast of a public message, the creation of an account, or anything else that we do on the internet today.

The blockchain is the underlying technology of all crypto-technologies. You can think of it as a ledger that keeps track of all transactions that have ever occurred. The transactions themselves are entirely public but the identities of the individuals participating in the transaction are anonymized. Rather than having a central authority (i.e. government, bank, etc…) maintain this ledger, it is maintained through consensus by a distributed set of actors who chose to participate. The blockchain can be downloaded by anyone, and participants are free to leave and join whenever they choose to. Using cryptography, the blockchain can verify the validity of a certain transaction (e.g. Alice indubitably sent Bob $5) and guarantee that previous transactions can never be edited or overwritten.¹

A protocol is a set of rules that two parties must strictly adhere to in order to successfully communicate with each other. In modern networking, HTTP is a protocol that runs on top of a different set of protocols called TCP/IP. In crypto, there are many different types of protocols that run on top of the blockchain. If you think of a protocol as a language that we speak, then the blockchain could be vocal sounds we produce. While all humans have the capability to produce the same sets of sounds, more or less, we cannot understand each other unless we speak the same language.

Bitcoin is a crypto-currency protocol built on top of the blockchain, meaning it is simply a digital store of value.

During the gold rush of the 1800s, miners expanded resources (physical energy) to extract gold from the ground. Eventually, this gold was deposited to banks for safekeeping or in exchange for an IOU note backed by the bank. The bank was responsible for maintaining a ledger of all the notes it issued. Since running a bank is not free, some of the gold mined had to be paid to facilitate the operations of the bank.²

Bitcoin miners are currently expanding resources (electricity) to facilitate transactions of value transfer. In return, they are receiving newly minted (mined) bitcoin and a small transaction fee. These bitcoins can be used to pay miners to facilitate other transactions on the blockchain. If no transactions happen on the blockchain then bitcoins would be rendered priceless, aside from the value our economy ties to them in exchange for goods & services.

Ethereum is a platform that runs smart contracts atop the blockchain. This means that it provides a programming language that can be used to create any type of transaction you want. Such a language is known as [**Turing Complete**](https://en.wikipedia.org/wiki/Turing_completeness). Like in Bitcoin, there is a fee associated with every transaction. The unit of currency used to pay for these transactions is called gas, which is a small fraction of the underlying currency of Ethereum called Ether (ETH).

There are dozens of applications that use this language to build blockchain applications using the Ethereum protocol, but a few that I'm personally interested in are:

- [**Gnosis**](https://gnosis.pm/): A prediction market that gathers information through both machine and human resources. One individual can provide useful trustworthy information in exchange for GNU, while other individuals can offer GNU to purchase it.
- [**Aragon**](https://aragon.one/): A distributed application that helps you manage a company (shareholder voting, "stock" vesting, etc…) without all the intermediaries. Companies that want to use this application must purchase Aragon Network Tokens (ANT).
- [**Filecoin**](http://filecoin.io/): A distributed file storage mechanism that lets individuals offer unused disk space they have at home. If I have an unused 10TB hard drive at home, I would be able to connect it to the Filecoin network and earn Filecoins (token name is still TBD). Individuals who want to use my hard drive must pay me some Filecoins.

While each of these applications has it's own application specific currency, they must pay some Ether every time a transaction takes place. You can think of ETH as the US Dollar, and GNU or ANT as the tokens you purchase at chuck-e-cheese.

One of the most interesting things about ethereum is the concept of proof-of-stake. The process of adding a new transaction (entry) to the blockchain (ledger) requires mining using a process called proof-of-work. For cryptographic reasons this requires a fair amount of CPU power and therefore wastes electricity. The team at ethereum is currently working on an alternative to this solution that eliminates the wasted electricity component. Individuals who own ETH can deposit it to some account and become bonded validators. Once deposited, it can not be withdrawn for a fixed predetermined amount of time. Bonded validators earn interest on their deposit, and gain the power to vote on whether new transactions are valid or not. If a bonded validator falsely validates an invalid transaction, they must forfeit their funds, or continue gaining interest otherwise. It is kind of a mix of buying a CD and joining a jury. This is still an ongoing effort, but it'll make block creation both faster and more economical in the future.

Linking these ideas back to my original [**tweet.**](https://twitter.com/olshansky/status/868979714177871872)

The Bitcoin protocol is both the protocol and the application. Excluding gold's uses as a commodity, it is just a store of value that can be moved or exchanged. To facilitate storage and transfer of gold from one person to another, a tiny fraction of the gold must be paid.

The Ethereum protocol is kind of like the US government. It paved the road for any type of vehicle, and these vehicles must pay ETH in order to use it.

With that said, why is it Bitcoin still the cryptocurrency with the highest market cap on the market? In my opinion it's simply because it was the first kid on the block. The original Bitcoin whitepaper and initiative was responsible for designing the first version of the blockchain, provided a very compelling use cases (currency), and showed that there is sufficient interest and incentive in the public to support and maintain a distributed network. However, a lot of new development has happened since then, it's uses are very limited, and it is facing technical limitations as well.³

For completeness, it's important to mention that there are other distributed applications running on top of their own blockchain completely separate from both Bitcoin and Ethereum. Two such examples are:

- [**Ripple**](https://ripple.com/): Enables a fast and easy way for international money transfer between institutional banks.
- [**Namecoin**](https://namecoin.org/): A distributed Domain Name Server (DNS) implementation.

## Additional Resources

A list of all tokens and their market caps can be found [**here**](http://coinmarketcap.com/all/views/all/).

Vitalik Buterin, the founder of Ethereum, gave a really interesting talk on [**crypto-economics**](https://www.youtube.com/watch?v=pKqdjaH1dRo). Though it gets a little technical, it covers a lot of economic incentive principles associated with crypto.

Balaji Srinivasan recently wrote a really good [**primer on tokens**](https://medium.com/@balajis/thoughts-on-tokens-436109aabcbe) describing what a token really is.

The [**Enterprise Ethereum Alliance**](https://entethalliance.org/) is an organization that has been helping bridge institutional corporations to blockchain technology via ethereum. Similar to how most companies no longer need to provision their own servers, new companies will no longer need to build their own blockchain from the ground up.

**_Disclosure: I am long ETH and ANT._**

¹ — It's worth mentioning that there as a caveat to the fact that the ledger cannot be overwritten, but it's highly impractical and we can therefore assume that it'll never happen.

² — Due to the practice of fractional-reserve banking, the bank might be inclined to offer free services due to the interest they earn via loans they make thanks to your deposit. I'm choosing to ignore that scenario for the sake of the argument and assume that all bank transactions come at a cost.

³ — Bitcoin does provide a scripting language, but it's extremely limited and not being used by anyone. Also, the rate at which new blocks are created is fixed which limits how quickly transactions can take to validate.
