+++
author = "Daniel Olshansky"
title = "Vibe Checks Are All You Need"
date = "2024-05-29T20:49:40.748Z"
description = "Saying the quite part out loud"
tags = [
    "ai", "tech", "productivity", "book", "personal"
]
substack_url = "https://olshansky.substack.com/p/vibe-checks-are-all-you-need"
+++

I’ve been using [ChatGPT since the first day it launched](https://olshansky.substack.com/p/24-hours-of-chatgpt), have gone to dozens of AI events over the last couple of years, and feel like I finally have to say quite part out loud: ***vibe checks***** are how 99% of LLM “evals” are done in practice today**.

Quantitative benchmarks, evaluations, and verification are critical to the 1% tail-end, but a ***vibe check*** is the good enough solution. This is what most LLM developers and day-to-day but are afraid to admit due to the lack of rigour.

This is not new to the field of Machine Learning.
I’ve experienced this firsthand across other domains over the past decade.

At Twitter in 2014, our initial spam filtering algorithms relied on word matches manually curated based on the ***"that's not nice test."*** At Magic Leap in 2017, while building out one of the world’s earliest mixed reality experiences with spatial mapping and object recognition, the ***"that looks good test"*** often sufficed. At Waymo in 2020, I joined the planner eval team focused on evaluating risky autonomous vehicle interactions - we used the ***"that looks safe test"*** to build out a golden ground truth dataset.

Rigours KPIs, metrics, analyses, etc are great and necessary. It’s the only way towards, publication, automation and regression testing at scale. However, on a day-to-day basis, I’d bet that most ML engineers just leverage their intuition.

The big difference today is that generative AI turned all software engineers into ML engineers. You no longer need to know Bayesian statistics or classification metrics. You no longer need to know how to design loss functions or tune hyperparameters. A little bit of prompting, context building and maybe even fine-tuning will take you a long way. After doing so, a bit of back and forth with the LLM will give you a general sense of whether or not it’s more or less useful.

**Most of you can stop reading here. Hopefully you got the *****vibe***** of the point I’m trying to make.** 

---
Now that I’ve gotten that out of the way, I wanted to get ahead of some of the bold statements I made above and have a more serious conversation.

There’s no question that we need leaderboards to separate the *A’s* from the *B’s*. Thankfully, we have [chat.lmsys.org](https://chat.lmsys.org/), and more recently [scale.com/leaderboard](https://scale.com/leaderboard).

Screenshot from chat.lmsys.org on May 28th, 2024Screenshot from scale.com/leaderboard on May 29th, 2024It’s also true that when Llama 3 was first released, this is exactly the sort of table I was looking for to get a sense of where it ranks next to the other leading models.

https://llama.meta.com/llama3/However, having gotten accustomed to using [my own GPT](https://olshansky.substack.com/p/from-pc-personal-computer-to-pgpt) daily, I used [Ollama](https://ollama.com/) to download llama:70b, customized it [using my own prompt](https://github.com/Olshansk/olshansky-bot) and played around with it. **There was no formal evaluation process for me to decide that I still prefer GPT-4 for now. **

One of the big issues I find with LLMs is that you get used to how it performs and behaves. It’s like building rapport with someone at work. Simon Willison captures it best [here](https://simonwillison.net/2023/Dec/31/ai-in-2023/#vibes-based-development):

> I find I have to work with an LLM for a few weeks in order to get a good intuition for it’s strengths and weaknesses. This greatly limits how many I can evaluate myself!

Ideally, all of us would have our own holdout data sets and convert our individual vibe-based evals into quantifiable benchmarks. But, while thinking about this, I came across the tweet below from [@minimaxir](https://x.com/minimaxir/status/1795178516838756387). In short, why have a holdout set when you can give your LLM more data, and potentially get a result better than you could have ever expected?

https://x.com/minimaxir/status/1795178516838756387I also came by this [lengthy discussion](https://www.reddit.com/r/ChatGPT/comments/17nzewn/a_theory_on_why_gpt4_got_worse/) on Reddit concerning the quality of GPT-4. The takeaway is that a model can easily overfit to an “official benchmark”, but our subjective interaction with it is still what ultimately matters at the end of the day:

> **This is more subjective, but the writing has gotten less creative, and the code worse and lazier**. Since we know that "All Tools" will have 32k context, I find it highly unlikely that it will be using the existing GPT-4-32k model, as that would be very expensive. I think what we're seeing is a dumbed down, GPT-4.5-turbo version, which is what will be used from now on. 

Putting a lot of these concepts together, Andrej Karpathy’s at Tesla from a recent [tweet](https://x.com/karpathy/status/1795873666481402010) speaks volumes:

> This is because good evals are very difficult to build - at Tesla I probably spent 1/3 of my time on data, 1/3 on evals, and 1/3 on everything else. They have to be comprehensive, representative, of high quality, and measure gradient signal (i.e. not too easy, not too hard), and there are a lot of details to think through and get right before your qualitative and quantitative assessments line up.

[…]

Anyway, good evals are unintuitively difficult, highly work-intensive, but quite important, so I'm happy to see more organizations join the effort to do it well.

There are thousands of brilliant individuals working on quantifying the eval process. I’m sure that as an industry, we will slowly iterate towards a better solution, but I don’t expect to find a silver bullet. For now, it’s okay to admit to using vibe checks. It’s a vibe 😎

Want to hear more from Olshansky?