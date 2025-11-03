---
title: "TIL: The two phases in LLM inference"
date: 2025-11-02T16:48:07-0800
draft: false
description: ""
tags: []
categories: []
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

This is a TIL of a TIL.

Simon Willison wrong of using an NVIDIA DGX Spark with an Apple Mac Studio for faster inference, with [all the details here](https://simonwillison.net/2025/Oct/16/nvidia-dgx-spark-apple-mac-studio/).

He talks about the two phases of inference:

1. **Prefill**: Influence Time-To-First-Token (TTFT)
2. **Decode**: Influence Tokens Per Second (TPS)

### Prefill

1. Read the prompt
2. Build a Key-Value Cache for each transformer layer in the model

**Bound by compute** as it initializes the model's internal state and does a lot of matrix multiplication.

### Decode

1. Read the prompt
2. Build a Key-Value Cache for each transformer layer in the model

**Bound by memory bandwidth** as it leverage the KV cache from the prefill.
