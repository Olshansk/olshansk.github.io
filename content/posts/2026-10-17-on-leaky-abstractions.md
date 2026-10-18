---
title: "On Leaky Abstractions"
date: "2026-10-17"
draft: true
tags: ["blog"]
---

[Elijah Potter's post](https://elijahpotter.dev/articles/everything_is_a_leaky_abstraction) led me to Andrej Karpathy's [Yes you should understand backprop](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b), which led me to the [Wikipedia page on leaky abstractions](https://en.wikipedia.org/wiki/Leaky_abstraction).

That reading trail left me thinking: **understanding where abstractions leak is what experience really is.**

An abstraction lets you use a system without keeping all of its inner workings in your head. A leaky abstraction is where those inner workings start to matter anyway.

## It works, until it doesn't

TCP/IP, Postgres and SQL, SMB, and networking more generally are good examples. These abstractions work well enough that most people using them rarely need to look under the hood.

But TCP's reliable delivery still depends on an unreliable network. A SQL query can return the right result while taking far longer than you expect. A remote file can look local until the network slows down or disappears. [Joel Spolsky's original essay](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/) walks through these kinds of leaks.

In the age of AI, there's even more to reflect on here. Theoretically, you can get something functional without understanding any of the inner workings at all. An LLM can help you build it, and it works.

Then it stops working.

If you don't understand the system underneath what the LLM produced, the abstraction leaves you stuck. You can ask for another fix, but you don't necessarily know why it broke or whether the next fix makes sense.

## Recognizing the words isn't the same as understanding

I notice this in my own experience across different domains.

With networking protocols, I have a better sense of how things work underneath. With cryptography, I have an idea of the protocols and the exchanges, but not the underlying cryptography.

With machine learning, I can throw out some words, and I have a good intuition around what's necessary for evals. But reading Karpathy's post, I recognized all the words—TensorFlow, RNNs, ReLUs, backprop—without having an intuition for how the underlying system works.

Karpathy's examples make that gap concrete: a framework can calculate gradients for you, but understanding why learning stalls still requires understanding what those gradients are doing.

So should you understand what's underneath, or should you just use the abstraction?

## The useful part of the leak

The usual complaint about leaky abstractions is that they create cognitive overhead and slow you down. You have to learn the details that the abstraction was supposed to let you ignore.

But there's something useful in that friction. It forces you to flex your brain and understand the system.

What I've found is that putting a bit of effort—and a bit of pain—into understanding something doesn't only help me in that domain. It teaches me to think more clearly.

That's the part I keep coming back to. Experience is knowing where the abstraction stops helping and having some intuition for what to do next.

**Leaky abstractions aren't a bug. They're a feature.**

<!-- Original dictation and supplied links, preserved verbatim for later editing:
https://elijahpotter.dev/articles/everything_is_a_leaky_abstraction

https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b

https://en.wikipedia.org/wiki/Leaky_abstraction

Create a new PR for a blog post called On Leaky Abstractions. And in it talk about this, like a Potter blog post led me to this Andrej Karpathy blog post, which led me to the Wikipedia page for leaky abstractions. And this is actually really interesting because leaky abstractions is what experience really is. And in the age of AI, there's even more to reflect on in this point, where theoretically you can get something functional without understanding any of the inner workings at all. But then the moment it stops working, the leaky abstraction of the LLM basically prevents you from being able to fix it. So they have some really good examples like TCP/IP and Postgres and SQL and SMB and networking, where the abstractions work really well and most people don't ever look under the hood into how it works. Now, with networking protocols, I have a better sense of how it works. With cryptography, I just have an idea of the protocols and the exchanges, but not the underlying cryptography. With machine learning, I can throw out some words and I have a good intuition around what's necessary for evals. But reading Andrej Karpathy's blog post, I recognize all the words, like TensorFlow and RNNs and relu's and backprop, but I don't have intuition into how the underlying system works. So should you or should you not understand? Originally, leaky abstractions were complex because they created cognitive overhead and slow things down. But leaky abstractions are useful because they force you to flex your brain and understand the system. And what I found is that if you actually put a bit of effort into understanding it and a bit of pain, it doesn't only help you in that domain, but it teaches you to think more clearly. So I say leaky abstractions aren't a bug, they're a feature.
-->

