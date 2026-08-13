---
title: "Ledger - A Stripe System Design Problem"
date: 2026-06-23T14:49:25-0400
draft: false
description: "A system design problem: build a bookkeeping service that tracks money sent and received on behalf of a merchant."
tags: []
categories: ["System Design"]
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

## Problem Statement

Stripe is a payments platform that provides the ability for online businesses to charge money from customers and then get paid out periodically.

For example, a Stripe merchant called ShirtyPuff runs a website that sells t-shirts. Every time one of ShirtyPuff's customers buys a t-shirt, we collect money on behalf of the merchant. Periodically we pay the merchant an amount which is calculated by aggregating all the transactions.

There are other teams that take care of building software for actually sending and receiving money.

Your aim is to build a bookkeeping service (called Ledger) that keeps track of money sent and money received on behalf of a merchant. The purpose of this service is to record all financial activity and allow getting the account balance for a given merchant.

## Operations

The Ledger should support the following operations:

- Record money sent or received on behalf of a merchant
- Get account balance for a given merchant
