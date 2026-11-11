---
title: "TIL: The Origins of ECDSA Curve Seeds"
date: 2026-10-16T21:36:38-0700
draft: true
tags: ["TodayIRead", "excerpt"]
ShowToc: false
ShowReadingTime: false
ShowWordCount: false
ShowPostNavLinks: false
author: ["Anthropic"]
---

> In under half an hour, Claude discovered the origins of the NIST P-192, P-224, P-256, P-384 and P-521 seeds. None of them were the results of any hash algorithm at all, but rather the output of the C library’s lrand48 random-number generator, seeded with a Unix timestamp!

— Anthropic, [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins), October 16, 2026.
