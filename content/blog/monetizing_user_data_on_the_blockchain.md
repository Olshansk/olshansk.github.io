
# Monetizing User Data on the Blockchain

Note: This is a repost of a blog published in early 2018.

With the advent of blockchain technology there has been a lot of discussion surrounding the monetization of user data. While this idea is great in theory, it took me a while to understand how something like this could be implemented in practice.

Depending on the type of user data at hand, it could be hundreds of megabytes or gigabytes in size. Blockchain is a distributed ledger and should not be thought of as an alternative to cloud storage. Though there are projects such as [Sia](https://sia.tech/), [Storj](https://storj.io/) and [Filecoin](https://filecoin.io/) working to build a distributed cloud, these projects are nascent and transfer the burden of paying for data storage directly to the user. There is a reason why Google is willing to store your photos for free, and it’s not a form of altruism. However, most of the people I’ve talked to still opt for using Google’s services.

As long as people care more about saving money than having self sovereignty over their data, they will have to sacrifice censorship resistance. If you choose to use Google to store your photos, you must understand that they can delete your photos or lock out your account at any point in time. Even if you encrypt all of your photos before saving them to the cloud, they are still in control of your data. For the rest of this article assume that the user is willing to sacrifice censorship resistance to a company named Hooli, who is offering to host the user’s data in exchange for a small cut.

This data monetization platform can be built using a relatively basic smart contract in conjunction with basic public key cryptography and a flew lessons from OpenPGP.

### Smart Contract

At a high level, the smart contract schema would look something like this:

    contract UserMonetizationContract {

    struct UserData {
      string URI;
      string metadata;
      string hash;
     }

    struct AcceptedBuyer {
      address acceptedBuyer;
      string key;
     }
        
     address[] userAddresses;
     mapping(address => AcceptedBuyer[]) acceptedBuyers;
     mapping(address => address[]) pendingBuyers;
     mapping(address => UserData[]) userData;
    }

* *userAddresses* is a list of addresses belonging to users willing to sell their data

* *acceptedBuyers* is a list of structs containing the buyers the user has agreed to share their data with along with a decryption key

* *pendingBuyers* is a list of buyers who want to get access to the user’s data but have not been granted permission yet

* *userData *is a list of structs pointing to a URI where the encrypted data is stored along with some metadata the user is willing to publicize (this can be used for buyers to find which user’s data they’d like to buy)

### Data Storage Flow

1. User generates a symmetric file encryption key: *Ks*

1. User Data (UD) is encrypted using the key above: *Ks(UD)*

1. User computes a hash of UD as well: *H(UD)*

1. *Ks(UD)* from step 2 is stored to Hooli’s servers. Even though Hooli is hosting the data, it cannot decrypt the data.

1. User queries the smart contract to retrieve *pendingBuyers* and decides which buyers they’d like to grant access to. Without public key infrastructure and a certificate authority, it is impossible to tell whom a certain public key belongs to, but that problem is outside the scope of this article…

1. In exchange for granting a pending buyer permission to their data, a transfer of funds would take place from the buyer to the user. This could be done in many different ways including a flat upfront fee, a subscription model, a negotiation, or even some sort of bid. A small portion of these funds would go to Hooli in exchange for hosting the user’s encrypted data.

1. For each buyer from step 5, the user would encrypt the symmetric key from step 1 with the buyer’s public keys: *Kp1(Ks)*, *Kp2(Ks)*, *Kp3(Ks)*, etc…

1. All of the encrypted keys along with the buyer addresses from step 7 are stored in *acceptedBuyers*

1. Every time the user creates more data, they would encrypt it with *Ks* and upload it to Hooli’s servers. The user would then add the hash, metadata and URI to *userData.*

1. All of the selected parties from step 6 can query the smart contract at any time, use their private keys to retrieve *Ks*, download the data, decrypt it, and check it’s integrity by comparing it against the hash in the contract.

1. Whenever the user wants to remove someone from the list of accepted buyers, they would need to recompute *Ks *and repeat step 7. All the data would need to be downloaded, re-encrypted and re-uploaded. Alternatively, since the buyer being removed may have previously downloaded the data anyhow, only new data generated from that point on would be encrypted using the new *Ks*. For security purposes, it is good practice to recompute *Ks* on a regular basis anyhow.

### Broken Trust

When you share a secret with someone, you are trusting the other person to keep that secret private. If you agreed to give someone your data in exchange for a payment, the buyer is technically free to do as they wish with the data. This is a human factor that cannot be solved by any blockchain or form of cryptography.

The only solution to this problem is to have a Decentralized Autonomous Organization (DAO) make decisions regarding whether there was a breach of trust. At the time of the transaction, the user and buyer will need to stake some amount of tokens. If the buyer shares the user’s data without their consent, the user can make a claim to the DAO that there was a breach of trust. Alternatively, if the user is saving unintelligible or bogus data, the buyer can make a similar claim to the DAO. Using a platform being developed by the likes of [OpenZeppelin](https://openzeppelin.org/) or [Aragon](https://aragon.one/), the DAO will decide who is at fault and whether the staked funds should be transferred or burnt.

Most importantly, Hooli can be completely cut out of the picture once decentralized cloud solutions become fast, cheap and scalable enough. The user will be in control of who has has access to their data, and be able to monetize it in a secure manner if they choose to.

[@olshansky](http://twitter.com/olshansky)
