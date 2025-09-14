---
title: "Monetizing User Data on the Blockchain"
date: 2018-07-20T14:31:19-07:00
draft: false
tags: ["blockchain", "smart-contracts", "data-privacy", "cryptography", "web3"]
categories: ["Technology", "Blockchain", "Privacy"]
summary: "Note: This is a repost of a blog published in early 2018."
medium_url: "https://medium.com/@olshansky/monetizing-user-data-on-the-blockchain-3584351a752e"
ShowToc: true
---

_Note: This is a repost of a blog published in early 2018._

With the advent of blockchain technology there has been a lot of discussion surrounding the monetization of user data. While this idea is great in theory, it took me a while to understand how something like this could be implemented in practice.

Depending on the type of user data at hand, it could be hundreds of megabytes or gigabytes in size. Blockchain is a distributed ledger and should not be thought of as an alternative to cloud storage. Though there are projects such as [Sia](https://sia.tech/), [Storj](https://storj.io/) and [Filecoin](https://filecoin.io/) working to build a distributed cloud, these projects are nascent and transfer the burden of paying for data storage directly to the user. There is a reason why Google is willing to store your photos for free, and it's not a form of altruism. However, most of the people I've talked to still opt for using Google's services.

As long as people care more about saving money than having self sovereignty over their data, they will have to sacrifice censorship resistance. If you choose to use Google to store your photos, you must understand that they can delete your photos or lock out your account at any point in time. Even if you encrypt all of your photos before saving them to the cloud, they are still in control of your data. For the rest of this article assume that the user is willing to sacrifice censorship resistance to a company named Hooli, who is offering to host the user's data in exchange for a small cut.

## Technical Implementation

This data monetization platform can be built using a relatively basic smart contract in conjunction with basic public key cryptography and a few lessons from OpenPGP.

### Smart Contract

At a high level, the smart contract schema would look something like this:

```solidity
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
```

**Contract Components Explained:**

- **userAddresses** is a list of addresses belonging to users willing to sell their data
- **acceptedBuyers** is a list of structs containing the buyers the user has agreed to share their data with along with a decryption key
- **pendingBuyers** is a list of buyers who want to get access to the user's data but have not been granted permission yet
- **userData** is a list of structs pointing to a URI where the encrypted data is stored along with some metadata the user is willing to publicize (this can be used for buyers to find which user's data they'd like to buy)

### Data Storage Flow

The complete workflow for storing and monetizing user data would follow these steps:

1. **Key Generation**: User generates a symmetric file encryption key: _Ks_

2. **Data Encryption**: User Data (UD) is encrypted using the key above: _Ks(UD)_

3. **Hash Creation**: User computes a hash of UD as well: _H(UD)_

4. **Cloud Storage**: _Ks(UD)_ from step 2 is stored to Hooli's servers. Even though Hooli is hosting the data, it cannot decrypt the data.

5. **Buyer Selection**: User queries the smart contract to retrieve _pendingBuyers_ and decides which buyers they'd like to grant access to. Without public key infrastructure and a certificate authority, it is impossible to tell whom a certain public key belongs to, but that problem is outside the scope of this article...

6. **Payment Processing**: In exchange for granting a pending buyer permission to their data, a transfer of funds would take place from the buyer to the user. This could be done in many different ways including a flat upfront fee, a subscription model, a negotiation, or even some sort of bid. A small portion of these funds would go to Hooli in exchange for hosting the user's encrypted data.

7. **Key Distribution**: For each buyer from step 5, the user would encrypt the symmetric key from step 1 with the buyer's public keys: _Kp1(Ks)_, _Kp2(Ks)_, _Kp3(Ks)_, etc...

8. **Contract Update**: All of the encrypted keys along with the buyer addresses from step 7 are stored in _acceptedBuyers_

9. **Data Updates**: Every time the user creates more data, they would encrypt it with _Ks_ and upload it to Hooli's servers. The user would then add the hash, metadata and URI to _userData._

10. **Data Access**: All of the selected parties from step 6 can query the smart contract at any time, use their private keys to retrieve _Ks_, download the data, decrypt it, and check its integrity by comparing it against the hash in the contract.

11. **Access Revocation**: Whenever the user wants to remove someone from the list of accepted buyers, they would need to recompute _Ks_ and repeat step 7. All the data would need to be downloaded, re-encrypted and re-uploaded. Alternatively, since the buyer being removed may have previously downloaded the data anyhow, only new data generated from that point on would be encrypted using the new _Ks_. For security purposes, it is good practice to recompute _Ks_ on a regular basis anyhow.

### Handling Broken Trust

When you share a secret with someone, you are trusting the other person to keep that secret private. If you agreed to give someone your data in exchange for a payment, the buyer is technically free to do as they wish with the data. This is a human factor that cannot be solved by any blockchain or form of cryptography.

The only solution to this problem is to have a Decentralized Autonomous Organization (DAO) make decisions regarding whether there was a breach of trust. At the time of the transaction, the user and buyer will need to stake some amount of tokens. If the buyer shares the user's data without their consent, the user can make a claim to the DAO that there was a breach of trust. Alternatively, if the user is saving unintelligible or bogus data, the buyer can make a similar claim to the DAO. Using a platform being developed by the likes of [OpenZeppelin](https://openzeppelin.org/) or [Aragon](https://aragon.one/), the DAO will decide who is at fault and whether the staked funds should be transferred or burnt.

## Future Implications

Most importantly, Hooli can be completely cut out of the picture once decentralized cloud solutions become fast, cheap and scalable enough. The user will be in control of who has access to their data, and be able to monetize it in a secure manner if they choose to.

## Key Benefits

This blockchain-based approach to data monetization offers several advantages:

- **User Control**: Users maintain sovereignty over their data and who can access it
- **Transparent Transactions**: All data access permissions and payments are recorded on-chain
- **Cryptographic Security**: Data remains encrypted and secure even when stored by third parties
- **Direct Monetization**: Users can directly profit from their data without intermediaries
- **Revocable Access**: Users can remove access at any time by rotating encryption keys
- **Integrity Verification**: Hash verification ensures data hasn't been tampered with

## Challenges and Considerations

While this system provides a foundation for user data monetization, several challenges remain:

1. **Identity Verification**: Without a robust PKI system, verifying buyer identities is difficult
2. **Scalability**: Current blockchain networks have limitations for high-frequency data transactions
3. **Storage Costs**: Decentralized storage is still more expensive than centralized alternatives
4. **User Experience**: The technical complexity may be barrier to mainstream adoption
5. **Regulatory Compliance**: Data privacy laws may impose additional requirements

This early framework demonstrates how blockchain technology could fundamentally change the relationship between users, their data, and the companies that want to use it.

[@olshansky](http://twitter.com/olshansky)
