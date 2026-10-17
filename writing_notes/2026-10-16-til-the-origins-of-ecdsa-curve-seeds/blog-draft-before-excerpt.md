---
title: "TIL: The Origins of ECDSA Curve Seeds"
date: 2026-10-16T21:36:38-0700
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

From Anthropic’s [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins):

> In under half an hour, Claude discovered the origins of the NIST P-192, P-224, P-256, P-384 and P-521 seeds. None of them were the results of any hash algorithm at all, but rather the output of the C library’s lrand48 random-number generator, seeded with a Unix timestamp!

TIL that the origins of these ECDSA curve seeds had been a mystery for decades, and the answer was a timestamp and a standard C random-number generator.
Anthropic says this discovery adds confidence in how the curves were chosen; it does not reveal a new cryptographic weakness.
