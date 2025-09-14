---
title: "Great article! Just wanted to provide my own tl;dr below"
date: 2022-11-05T20:26:00-07:00
draft: false
description: "▪ MPT Ingredients: Merkle Tree + Prefix Tree + Custom Modification"
tags: ['great', 'article', 'just']
categories: ['cryptocurrency']
medium_url: "https://medium.com/@olshansky/great-article-just-wanted-to-provide-my-own-tl-dr-below-1c35fd5c74a"
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

Great article! Just wanted to provide my own **tl;dr** below

▪ **MPT Ingredients** : Merkle Tree + Prefix Tree + Custom Modification

▪ **MPT Nodes** : Leaf nodes + branch nodes + extension nodes

▪ **State root** : 256 bit hash of root

**▪** **Geth KV Store** : levelDB

▪ **Parity KV Store** : rocksDB

**▪** **Tries** :

**1\. Transaction Trie** \- mapping from transction hash → raw transactions

**2\. Transaction Reciept Trie** \- mapping from transaction hash → transaction execution Metadata

**3\. World State Trie** \- mapping from account address (including contracts) to account data

**4\. Account Storage Trie** \- mapping from integers to integers specific to an account/contract

Per the answer at [1], I'm still trying to understand if it's one transaction trie per block or one for the entirety of the state.

[1] [https://ethereum.stackexchange.com/questions/15142/how-many-tries-does-ethereum-have,](https://ethereum.stackexchange.com/questions/15142/how-many-tries-does-ethereum-have)