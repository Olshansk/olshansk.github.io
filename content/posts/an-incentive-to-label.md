+++
author = "Daniel Olshansky"
title = "An Incentive to Label"
date = "2023-04-02T21:27:01.964Z"
description = "tl;dr The incentive to label is to have a disincentive to label poorly"
tags = [
    "crypto", "ai", "tech", "research", "productivity", "book"
]
substack_url = "https://olshansky.substack.com/p/an-incentive-to-label"
+++

**GPT4 Abstract**: Large Language Models (LLMs) have made significant strides in recent years, thanks in part to Reinforcement Learning from Human Feedback (RLHF). However, the success of these models depends not only on the quantity of human labels but also on their quality. This blog post discusses the importance of high-quality labels in LLMs and proposes a blockchain-based solution to incentivize better labelling.

_tl;dr_

- _Data Quality » Data Quantity for fine-tuning a foundation model._

- _High-quality data sets are necessary, expensive and hard to come by._

- _Web3 incentives & disincentives can be leveraged to curate high-quality data sets._

# Table of Contents

- [A Secret Ingredient](https://olshansky.substack.com/i/72740291/a-secret-ingredient)

- [The Life of A Data Plumber](https://olshansky.substack.com/i/72740291/the-life-of-a-data-plumber)

- [Augmented Reality - Boxes and Labels](https://olshansky.substack.com/i/72740291/augmented-reality-boxes-and-labels)

- [Autonomous Vehicles - Risky or Not?](https://olshansky.substack.com/i/72740291/autonomous-vehicles-risky-or-not)

- [Labeling - It’s not about the Infra](https://olshansky.substack.com/i/72740291/labeling-its-not-about-the-infra)

- [OpenAI - Ahead of the Game](https://olshansky.substack.com/i/72740291/openai-ahead-of-the-game)

- [Nothing At Stake](https://olshansky.substack.com/i/72740291/nothing-at-stake)

- [Where do Blockchains fit in?](https://olshansky.substack.com/i/72740291/where-do-blockchains-fit-in)

- [Tuning User Interfaces (TUIs)](https://olshansky.substack.com/i/72740291/tuning-user-interfaces-tuis)

- [Appendix](https://olshansky.substack.com/i/72740291/appendix)

# A Secret Ingredient

Large Language Models feel like they’ve been an overnight success these past few months. But, in reality, it’s the result of more than half a century of research, the increasing availability of scalable cloud compute, the advent of tons of online data, stirred together with the hard work of hundreds of people, thousands of optimizations and countless tweaks.

The special not-so-secret ingredient that tops all of it off is [Reinforcement Learning From Human feedback (RLHF)](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback). Lex Fridman called it the “little magic ingredient” in a [recent interview with Sam Altman](https://youtu.be/L_Guz73e6fw?t=363), and Chamath Palihapitiya called it the “White Truffle” in a [recent episode of the All-In Podcast](https://youtu.be/qQ544sWC8ZQ?t=1349). Just a little bit of RLHF sprinkled atop a massive amount of data and training is one of the significant differentiators that help with alignment and makes our newfound assistant so helpful in answering questions.

Here's an example from Jan 2022 of how an older version of GPT3 performed before and after humans were in the loop.

![GPT3 Before and After RLHF](https://substack-post-media.s3.amazonaws.com/public/images/b69327de-b2b3-4992-b490-631f96c78f4e_1966x1124.png)

- [https://openai.com/research/instruction-following#sample1](https://openai.com/research/instruction-following#sample1)

Despite all this work and advances, one crucial aspect that deserves more attention is the quality, not just the quantity, of human-generated labels used to align these models.

# The Life of A Data Plumber

The unsexy truth everyone in the AI/ML industry knows is that most of your time will be spent doing data plumbing and filtering for high-quality labels. This infographic says it all.

![Data Plumbing Infographic](https://substack-post-media.s3.amazonaws.com/public/images/a9ef32af-ddf4-4703-a10e-20d97e19a5ff_913x611.png)

[@schmarzo](https://twitter.com/schmarzo/status/1029948710254329856)

Andrej Karpathy, who recently returned to OpenAI after a 5-year stint as Director of AI at Tesla, famously coined the term [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) in a 2017 blog post:

> In most practical applications today, the neural net architectures and the training systems are increasingly standardized into a commodity, so most of the active “software development” takes the form of curating, growing, massaging and cleaning labeled datasets. This is fundamentally altering the programming paradigm by which we iterate on our software, as the teams split in two: the 2.0 programmers (data labelers) edit and grow the datasets, while a few 1.0 programmers maintain and iterate on the surrounding training code infrastructure, analytics, visualizations and labeling interfaces.

Now that LLMs can write a good portion of the code for us, this statement rings even more true than it did six years ago. However, with more than a dozen daily announcements related to new product launches using LLMs or optimizations to their performance, I’m hearing very few conversations about acquiring higher-quality human annotations. As someone who has seen the importance of smooth infrastructure and high-quality labels, I believe it will be one of the catalysts to seeing the next step function.

![Software 2.0 Diagram](https://substack-post-media.s3.amazonaws.com/public/images/7ae95769-f7ba-46aa-8486-ba0c62a82d8f_1219x700.png)

[https://karpathy.medium.com/software-2-0-a64152b37c35](https://karpathy.medium.com/software-2-0-a64152b37c35)

# Augmented Reality - Boxes and Labels

At Magic Leap, we worked on a product called [Shared World](https://www.magicleap.com/spatial-mapping-ml1) that enabled multiplayer support through shared spatial mapping. The system also had an object recognition pipeline that used sensor data to understand the world around you. High-quality public databases such as [ImageNet](https://www.image-net.org/) were more than sufficient for this task.

Objective and well-defined questions, such as _“draw and label the animal in this photo_,” are arguably a solved problem. We already have large, high-quality, labeled data sets. In addition, a paper published last month showed that [ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks](https://arxiv.org/pdf/2303.15056.pdf) in terms of accuracy, time and cost, and I expect the same thing to extend to images in the near future.

Though much engineering work still needs to be done to make AR an everyday reality, there are many more nuanced open-ended problems in the AV space.

# Autonomous Vehicles - Risky or Not?

While I was at Waymo on the Planner Evaluation team, one of the critical questions we tried to answer was: _Does this on-road (actual or simulated) situation pose a risk for a Vulnerable Road User (VRU)?_

We were able to leverage Alphabet’s infrastructure and resources to collect thousands of labels but faced a ton of problems along the way. In particular, a lot of time was spent on training and evaluating labellers while accounting for cultural driving differences. It forced me to learn about the subtle differences in driving practices between the US and India…

We tried countless of different approaches to solving these problems. It ranged from writing detailed training documents, curating golden label datasets ourselves, ranking and rotating labellers, experimenting with varying mechanisms of filtering, etc. **Though we did make progress, there was no single silver bullet.**

# Labelling - It’s not about the Infra

There are a lot of tools to make labelling simpler. Platforms like [Amazon’s Mechanical Turk](https://www.mturk.com/) or [Google’s AI Platform Data Labeling Service](https://cloud.google.com/ai-platform/data-labeling/pricing) provide infrastructure to streamline annotation pipelines and gather human labels, which can be integrated with various downstream MLOps services (e.g. continuous re-training and re-testing).

With that said, the process of label collection is non-trivial.

**Example preparation**. A good set of real or simulated examples needs to be prepared and collected so they are a good use of the labeller’s time. For example, asking if a car is at risk when driving straight, under the speed limit, with no one around is pointless.

- **Question Design**. The right question needs to be asked so it is useful in training or reinforcing the model. For example, should there be a scale of the situation's risk or a true/false or multiple-choice question? Should there be an open-ended text field that explains the risk? This requires iteration and experimentation. For reference, I find the [question design OpenAI did for backflips](https://openai.com/research/learning-from-human-preferences) brilliant.

- **Labeler Training**. Labelers need to be trained to understand what’s being asked and the expectation of what/how they should be answering.

- **Label Filtering.** Even highly trained labelers make mistakes, and these outliers need to be filtered out from the dataset.

- **Labeling Fatigue**. Manual labeling is a boring and tedious task. So it’s understandable that label quality will drop as the quantity from any single individual increases.

- **Subjectivity**. The hard questions are the subjective ones. For example, asking whether an on-road situation is risky depends on personal preferences/biases (e.g. age, driving experience, personality, etc.) and cultural ones (e.g. US vs India).

![Data Science Challenges](https://substack-post-media.s3.amazonaws.com/public/images/2044ba8e-a56e-4272-947d-cd945c6dcb1a_1200x333.png)

[@data36_com](https://twitter.com/data36_com/status/1098220523811729408)

# OpenAI - Ahead of the Game

Everything I’ve said up until now isn’t news to the team at OpenAI.

In an [article from June 2017](https://openai.com/research/learning-from-human-preferences), where they first mentioned the use of RLHF, they were already aware of this problem:

> Our algorithm’s performance is only as good as the human evaluator’s intuition about what behaviors *look* correct, so if the human doesn’t have a good grasp of the task they may not offer as much helpful feedback.

And in [January of 2022](https://openai.com/research/instruction-following#sample1), they presented the flow that showed promising results in aligning language models to follow instructions

![OpenAI Instruction Following Flow](https://substack-post-media.s3.amazonaws.com/public/images/e1f4e00f-b0ba-4351-94fd-a52937744889_1140x677.png)

- https://openai.com/research/instruction-following#sample1

They did highlight that this issue was not entirely eliminated:

> Further, in many cases aligning to the average labeler preference may not be desirable. For example, when generating text that disproportionately affects a minority group, the preferences of that group should be weighted more heavily. Right now, InstructGPT is trained to follow instructions in English; thus, it is biased towards the cultural values of English-speaking people.

OpenAI is doing their best to develop and iterate in public, and I hope they’ll extend their [fine-tuning APIs](https://platform.openai.com/docs/guides/fine-tuning) to GPT4 this year. However, this doesn’t solve the problem that the labels still need to be of high quality. **We are past the era of “data quantity” and are now in the age of “data quality.”**

# Nothing At Stake

One of the core problems solved by Proof-of-Stake blockchains is the _[Nothing At Stake](https://vitalik.ca/general/2017/12/31/pos_faq.html#what-is-the-nothing-at-stake-problem-and-how-can-it-be-fixed)_ problem. In short, an actor with some upside and zero downside has more incentive to perform low-quality or malicious work. [1]

Companies usually pay out annual bonuses at the end of the year, and occasionally need to restructure based on performance. Similarly, labelers get paid based on the amount of work they do and might be rotated to a different project if their labeling quality does not meet a specific bar.

Consider if companies were to pay out annual bonuses at the beginning of the year but take back part, or more, of it at the end of the year? Similarly, what if labelers were to lose a deposit for doing a poor job at annotating?

The concept is relatively straightforward and follows patterns from [Prediction Markets](https://en.wikipedia.org/wiki/Prediction_market):

Labelers put down a deposit before doing any work

- The experimenter prepares a list of tasks and puts a deposit that’ll split amongst all the labelers doing the work

- The labelers finish their tasks

- Labelers close to the mean (i.e. the general population) get a small payout from the experimenter

- Labelers far from the mean don’t earn or lose anything

- Outliers lose a portion of their deposit

![Python Program Example](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/d2b1b8d5-123c-4a28-b99f-72418a815a95_576x455.png)

_An illustrative example outputted by a Python program generated by ChatGPT_

It's worth noting that this is not an original idea. [2] Two projects I was excited about in the earlier days of Ethereum were [Augur](https://augur.net/) and [Gnosis](https://www.gnosis.io/), leveraging ideas from the [Wisdom of the Crowds](https://www.goodreads.com/book/show/68143.The_Wisdom_of_Crowds) through public and permissionless prediction markets.

# Where do Blockchains fit in?

You might ask why this even needs a blockchain, and if you're snarky, point me to this image:

![Do you need a blockchain?](https://substack-post-media.s3.amazonaws.com/public/images/1e17d3f9-a133-4982-bf85-d927a43f592b_1060x610.png)

[https://circo.io/gigo/](https://circo.io/gigo/)

Suppose we focus solely on product and do not consider institutional or geopolitical censorship. In that case, I can steelman the case for why we could build this as a traditional web2 SaaS. However, there are a handful of primitives in the Crypto industry which make it a good contender as the platform to build on.

**Money is a first-class citizen**. Depositing, earning and slashing are core primitives of any blockchain, making things like value transfer and micropayments cheaper and simpler.

- **Permissionless Identity**. It is easy to sign up and participate regardless of where you are, keeping your identity optionally private. It also enables longer-term reputation-building mechanisms.

- **Commit & Reveal paradigms**. All the labels will be encrypted and public until the experiment is complete, so it’s hard to aim to be close to the mean unless users collude offline. No central party can game the results. [3]

- **Zero Knowledge Technology**. A lot is being done in the zk space which can be utilized here. For example, the tasks could be designed so that the experimenter only gets the final results without being able to tie a label to any single user, while still enabling an ongoing reputation system. Alternatively, the labels could be completely hidden from everyone but still be used in reinforcement learning by leveraging [fully homomorphic encryption](https://fhe.org/); _note that this is not easy._

- **Distributed Ledger Technology**. Anyone can design a set of labeling tasks or sign up as a labeler. Depending on the type of encryption, it could also enable downstream use cases, such as data markets.

![Blockchain Labeling System Diagram](https://substack-post-media.s3.amazonaws.com/public/images/75ca8b8c-01fc-4800-af00-402fc3deb7d5_6350x2756.png)

# Tuning User Interfaces (TUIs)

While some things like math and science are objective and true, others, such as _safe_ driving patterns, are nuanced and vary depending on the context. You might imagine how this extends to even more difficult political topics.

I don’t believe a single model will be able to satisfy everyone’s preferences, but fine-tuning a base model will. This will require a minimum number of labels, but will heavily rely on their quality moreso than their quantity.

Bill Gates called this the largest technological innovation he has seen [since the GUI](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun), and Stephen Wolfram has [dubbed new chat interfaces](https://writings.stephenwolfram.com/2023/03/will-ais-take-all-our-jobs-and-end-human-history-or-not-well-its-complicated/) as Linguistic User Interfaces (LUIs). I’m suggesting we also need to think about Tuning User Interfaces (TUIs), so our models can age with us like a fine wine. 🍷

Subscribe if reading this was a good use of your time :)

---

# Appendix

[1] An actor in a network that is responsible to provide a certain service (e.g. securing a blockchain, making data available, etc…) must put up a deposit that is subject to penalties (i.e. slashed/burnt) if they are proven to be faulty or malicious. Rather than just having the upside of earning money for providing a service, they also face the consequences of a negative ROI.

From my experience, labelers are exposed to the upside of labeling more examples, but the only downside they face is being removed from a certain labeling task if their label quality score becomes too low. By introducing [Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion) (the psychological pain of losing is twice as powerful as the pleasure of gaining) along with the [Endowment Effect](https://en.wikipedia.org/wiki/Endowment_effect) (an individual’s places a higher value on something they already have), I believe the quality of labels can be much higher.

[2] Most good ideas are just regurgitations of existing ideas executed on by the right team at the right time. [Vitalik’s comment](https://vitalik.ca/general/2022/12/05/excited.html) captures it well:

> Today, enough time has passed that there are few ideas that are completely unexplored: if something succeeds, it will probably be some version of something that has already been discussed in blogs and forums and conferences on multiple occasions

[3] The perceptive reader might raise the issue of Sybil Attacks. Though this is a fair consideration, a well-designed stake & burn mechanism can deter this.
