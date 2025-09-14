+++
author = "Daniel Olshansky"
title = "Move Fast & Document Things"
date = "2024-09-22T19:45:01.728Z"
description = "Actionable tips for software teams to build sustainable codebases of any size and reduce day-to-day frustrations"
tags = [
    "ai", "nuclear", "startup", "tech", "research", "investment"
]
substack_url = "https://olshansky.substack.com/p/move-fast-and-document-things"
+++

**I'm going to share a small secret: a perfect solution to software documentation does not exist.**

It’s hard to generalize what “good documentation” entails. It depends on the team, the product, the timing, and a million other things. Have you found PMF or are you iterating? Are you a small tight-knit team or are you scaling? Is your team remote, in-office or hybrid? Is open source and external collaboration a key component of your value proposition? _I’ll stop here before it gets boring…_

The closest answer I’ve found to “good documentation” is the MVD (Minimum Viable Documentation) required to reduce the frustration engineers endure day-to-day. Here is a screenshot and quote from [StackOverflow’s 2024 developer survey](https://stackoverflow.blog/2024/07/24/developers-want-more-more-more-the-2024-results-from-stack-overflow-s-annual-developer-survey/) that speaks for itself:

- [https://stackoverflow.blog/2024/07/24/developers-want-more-more-more-the-2024-results-from-stack-overflow-s-annual-developer-survey/](https://stackoverflow.blog/2024/07/24/developers-want-more-more-more-the-2024-results-from-stack-overflow-s-annual-developer-survey/)Documentation should not be confined to design docs. It can refer to tasks, tech debt, explanations, instructions, decision logs, etc…

Whenever someone mentions having “THE MASTER docs page” that links to “ALL other docs”, I immediately point to Google as a counter-example. One of the reasons Google succeeded is because they didn’t follow Yahoo’s (RIP) footsteps in creating a [mega directory](https://www.theverge.com/2014/9/27/6854139/yahoo-directory-once-the-center-of-a-web-empire-will-shut-down). Instead, they leveraged backlinks left throughout webpages as the source of truth and built infrastructure that adapts around it. This has been my inspiration for building sustainable codebases.

I like to think of these hyperlinks as *breadcrumbs, *ingredients, that feed the search giant. Similarly, I’d extend this analogy to LLMs as any online content has become the *breadcrumbs *feeding these beasts.

**⚠️ This post is going to get a bit technical. It is meant to act as a reference for engineering teams and leaders. My goal is to share practical tips & tricks to leave \*\*\***breadcrumbs**\*** during, not before nor after, the process of software design and development. By making it part of the process and the culture, it enables teams to Move Fast & Document Things ⚠️\*\*

## Table of Contents

**[The Truth Behind Software Documentation](https://olshansky.substack.com/p/move-fast-and-document-things)**

**[What's my motivation for writing this post?](https://olshansky.substack.com/p/move-fast-and-document-things)**

**5 Tips & Tricks to Moving Fast & Documenting Things:**

**[Please Update Comment (](https://olshansky.substack.com/p/move-fast-and-document-things)\*\*\***[#PUC](https://olshansky.substack.com/p/move-fast-and-document-things)**\***[) - A quick request to move explanations into comments](https://olshansky.substack.com/p/move-fast-and-document-things)\*\*

- **\*[TODO_XXX](https://olshansky.substack.com/p/move-fast-and-document-things)\*\*\***[ - Use ](https://olshansky.substack.com/p/move-fast-and-document-things)**\***[TODO](https://olshansky.substack.com/p/move-fast-and-document-things)**\***[s to communicate everything you didn’t do in order to stay focused](https://olshansky.substack.com/p/move-fast-and-document-things)\*\*

- **[Leave Links Everywhere - Leave a trail of internal and external links everywhere](https://olshansky.substack.com/p/move-fast-and-document-things)**

- **[LLM Diagrams - Leverage LLM tools to get fast at visual documentation](https://olshansky.substack.com/p/move-fast-and-document-things)**

- **[Naming Things - You won’t regret verbosity down the line](https://olshansky.substack.com/p/move-fast-and-document-things)**

---

## **The Truth Behind Software Documentation**

Anyone who has ever worked with me knows what a PITA (_Pain In The Ass_) I could be when it comes to documentation 🥙

Though I have caught myself asking for too much on a few occasions, I put a lot of effort into trying to be pragmatic and cognizant of the tradeoffs. Most of the time this involves [time-boxing requests](https://blog.staysaasy.com/p/your-small-imprecise-ask-is-a-big), being clear about what not to document, and most importantly, reinforcing and reiterating the following question: _“Is this documentation you’d ACTUALLY want to read yourself?”_

The unfortunate truth is most people don’t want to [RTFM](https://en.wikipedia.org/wiki/RTFM) (Read The Fucking Manual). It requires a different level of concentration, effort and time investment. Things should usually either be self-explanatory, work out of the box, or adhere to the best practices of [copypasta](https://en.wikipedia.org/wiki/Copypasta).

*If this has ever been you, I hope you’ll appreciate the rest of the post *🐸

-

## **What's my motivation for writing this post?**

Whenever I document things myself, or ask someone else to document something, I have a few key motivations:

I like to be self-sufficient

- I don't like to be confused

- I don't like wasting time

- I don't like context switching

- I am always writing for my future self

- I operate under the assumption that I might get hit by a bus tomorrow

**The points above are pretty selfish, which they are, but everything I want for myself, I want even more for those around me. We choose who we want to be surrounded by, both in and out of work, which makes it easy to always optimize for the outcome where everyone wins. In this particular case, my goal is to reduce the frustrations of our engineering team to make the day-to-day of software development more fun and pleasant.**

Over the last few years, our team has been iterating on a few tips and tricks that enable us to Move Fast & Document Things. These are not philosophical ideas, nor are they plug-and-play tools. They require effort and a culture shift. However, I’m confident that it’ll be a net positive if you adopt at least one of them. If you do, I’d love to hear about it!

_Note: I'm going to be using some platform-specific terminology: GitHub, Notion, Discord, etc… These are specific to the tools we use at [Grove](https://grove.city/), but I’m assuming you’ll be able to draw analogues to the tools you use at work._

## **1. Please Update Comment (\*\*\***#PUC**\***) - A quick request to move explanations into comments\*\*

_tl;dr Use #PUC to ask each other to Document Things where additional details may be necessary so engineers have the context they need to Move Fast._

---

Reviewing code changes (i.e. [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)s), is not only an opportunity to give feedback, but also an opportunity to learn how or why something works a certain way.

I’ve seen, way too often, long insightful discussion threads get lost in the GitHub abyss. So much time and mental energy was spent on carefully curated messages that will never be seen again…

If an engineer had to ask another engineer for additional context or clarification once, there is a high chance it’ll be asked again. A new engineer will come by the same piece of code, spend time trying to make sense of something that may or may not make sense, reach out to the author of the code who may or may not be around, everyone will have to reload the prior context into memory, and before you know it, we’ve lost a whole day of engineering hours on something that has already been solved.

**#PUC: Please Update Comment
If you ask someone for an explanation, and you think it’ll help someone else, ask the other person to #PUC with some related context (document, code, comment, etc).**

The time writing out the response has already been spent. The overhead of copying it as a comment is just a small fraction of that.

An added benefit is that it keeps the explanation right alongside the implementation rather than some obscure distant document whose existence may not be known. It scales learning from a 1:1 to a 1:N, where N is any future engineer (or bot) that’ll be reading the code. It also helps the original author recall what they were doing 6 months later.

Here is a concrete example of #PUC in action. One of the reasons I love this example in particular is because it’s an exchange between two of our senior engineers while I was OOO.

#PUCing things up has really become part of our culture.

- [https://github.com/pokt-network/poktroll/pull/671#discussion_r1673676918](https://github.com/pokt-network/poktroll/pull/671#discussion_r1673676918)

## **2. \*\*\***TODO_XXX**\*** - Use **\***TODO**\***s to communicate everything you didn’t do in order to stay focused\*\*

_tl;dr Document Things that need to be done in the future using TODOs so you can Move Fast on what needs to be done today._

---

In product, we have competing requirements from different individuals leading to [Feature Creep](https://en.wikipedia.org/wiki/Feature_creep) that lose sight of the time and complexity to build something. In engineering, we have nerds having fun with the tech and programmers with OCD trying to make things perfect while losing sight of the product’s end goal.

An engineer might have an idea for how something should be refactored. There might be an edge case left unhandled or a test case that’ll never happen in real life. There might be a new tool or library we should look into. We might be intentionally introducing some tech-debt or a hack that’ll take 3 days to solve. _There’s this thing…_

This is the sort of thing that often gets called out in meetings or standups but is hard to keep track of. It’s a double-edged sword. Trying to tend to everything all the time leads to perfectionism and slow iteration cycles. Not tending to this at all leads to a big mess and poor morale on engineering teams.

A culture of using **_TODOs_** liberally throughout the codebase has a ton of upsides. Here are just a few:

**Satisfies the engineer’s “OCD craving”** of showing (to themselves or others) that they know what to do, or how to do it, if they had the time. It is a way for an engineer to allow themselves to keep Moving Fast without having TODO it.

- Similar to #PUC, it **captures the details to something that should be done** alongside the necessary context. Whoever is reading the code won’t have to re-discover the wheel.

- Documenting a TODO is a lot **less friction and overhead** than creating a fully scoped task (GitHub issue, Jira ticket, etc…).

- It is a streamlined way to **create a backlog** of future work while working on existing tasks. The best time to document a quick workaround that’ll need to be replaced is while creating it.

- **TODOs can be tracked**, filtered and updated programmatically.

**Backlog example:** When tech-debt week comes around, our team just needs to search for all instances of **_TODO_TECHDEBT_** in the codebase as a starting point. When we start preparing for our beta or production releases, we just need to search for **_TODO_BETA_** or **_TODO_PROD_** respectively.

**Filtering example**: It’s very easy to build [one-line scripts](https://github.com/pokt-network/poktroll/blob/main/makefiles/todos.mk) to track what kind of *TODO*s we have in the codebase. As of writing this document, in the span of a few seconds, I found that we have at least 36 known things to do prior to our beta release, 90 prior to our mainnet (production) release and almost 200 techdebt items to tend to someday. It’s not perfect, and it’s incomplete, but this sort of visibility doesn’t even exist in most other organizations.

$ grep -r "TODO_BETA" ./ | wc -l
36

$ grep -r "TODO_MAINNET" ./ | wc -l
90

$ grep -r "TODO*TECHDEBT" ./ | wc -l
165**Bonus example - \*\*\***TODO_XXX(#123, @olshansk)*\*\*: Being a GitHub-first organization enables us to associate a TODO with a specific individual and/or a specific GitHub issue using `_@USER*`or`*#NUM\*` respectively. It provides context on who is the primary point of contact for the issue or where more details can be found.

_I’ll end it off with a few more examples but feel free to skip to section 3 if you got the point._

Here is a **_TODO_TECHDEBT_** capturing an inefficiency. It may or may not come back to bite us sooner or later. At the very least, we know that it’s there and if it does become an issue, the solution is already documented:

Here is a **_TODO_HACK_**. Regardless of what the reason or issue is, an engineer will know not to accidentally modify it unless they’re really ready to roll up their sleeves.

Some of our most common TODOs are documented [here](https://github.com/pokt-network/poktroll/blob/main/makefiles/todos.mk).

- [https://github.com/pokt-network/poktroll/blob/main/makefiles/todos.mk](https://github.com/pokt-network/poktroll/blob/main/makefiles/todos.mk)

## **3. Leave Links Everywhere - Leave a trail of internal and external links everywhere**

_tl;dr Don’t shy away from Documenting Things by leaving links as comments in the code if you believe it’ll help a reader Move Fast in the future._

---

Until someone builds a tool that leverages LLMs to give us the answer or documentation we need, when we need it, the following is a much more common flow on engineering teams:

> _Eng 1: “What was the thought process behind this design?”
> Eng 2: “Here is a link to the design doc with all the details.”
> Eng 1: “Thanks, I’ll check it out and let you know if I have any other questions.”
> …
> Eng 1: “Did you consider doing \_\_\_ instead?”
> Eng 2: “Yup, here’s a link to the decision log with all the tradeoffs.”
> Eng 1: “Cool, let me check that out too.”
> …_

The interaction above may not seem like much, but it happens many times, every day, on every project, on every team, at every organization. The context switch from this sort of conversation compounds.

For some reason, it feels *taboo *to leave links to external resources in the code. In practice, it’s what we end up sharing anyhow.

If a certain link was the catalyst to a certain decision, throw it in! If you see yourself sharing it with someone in the future, throw it in! It doesn’t matter if it’s a Discord channel, Slack thread, Google doc, etc…

Here is an example inserting a link to a private notion doc in our public open source repository:

[pokt-network/…/x/tokenomics/keeper/token_logic_modules.go#L184](https://github.com/pokt-network/poktroll/blob/f7b579493dc8d02ebdb43ae68d79d8cd3bdfb7f6/x/tokenomics/keeper/token_logic_modules.go#L184)

## **4. LLM Diagrams - Leverage LLM tools to get fast at visual documentation**

_tl;dr Use the text-to-diagram feature in [Excalidraw](https://excalidraw.com/) to quickly Document Things in a visual manner using [Mermaid](https://mermaid.js.org/) diagrams. This enables you to Move Fast on your design docs, documentation or even conversations._

---

We’ve all heard that a picture is worth a thousand words. It’s why we generally scroll past the text and go straight to the figures when approaching new documentation.

I would bet that the next time you decide to read a whitepaper, you will likely:

Read the abstract

- Look at the figures & diagrams

- Read the conclusion

You may read the rest of the paper if all of the above captured your interest.

**As powerful as visuals are, being asked to put together a sequence-diagram, flow-chart or component-diagram always feels like a daunting task. While I do agree to some extent, I believe it’s a muscle that can be trained like any other. Once you train it, it becomes a superpower to Move Fast, Document Things and level-up your team.**

Rather than simply stating that you should “get better at diagrams”, I’m going to share the ultimate tool so you can Move Fast & Document Things: [Excalidraw’s text-to-diagram feature](https://www.linkedin.com/posts/excalidraw_text-to-diagram-activity-7134936790544621568-2TQF/).

[I’m not alone in saying](https://offbyone.us/posts/why-is-excalidraw-so-good/) that [Excalidraw](https://excalidraw.com/) is a phenomenal product. Moreso, its recent integration of LLMs is the most powerful use case I’ve found that I continue to use consistently at least once a day.

The following is a real set of bullet points I put together with someone during a pair programming session. We realized we needed to visualize the problem while going through it so we decided to use Excalidraw on the spot. _I intentionally left it raw & unedited._

Create a mermaid sequence diagram that shows:

1. User starts transfer from App A to App B

- If B is an app -> tx errors and doesn't modify state

2. Wait until transfer period elapses (at least next session)
3. When (2) happens:

- Atomic transfer from A ->B
- Unstake A
- Stake B:

4. Error case: transferring to an existing application (if B is already an app)

Add notes for reasons why we have unbonding periods:

1. Account for mid-session misalignment w.r.t usage
2. Avoid Relay Mining & account settlement complexities
3. Weak subjectivity - adversarial behaviour + unstake + run away

Assumptions:

- No collisions on App B The result is a better starting than anything we could have thrown on a whiteboard. We iterated and improved it manually, but this was a strong starting point.

-

Here is Excalidraw in action generating a mermaid sequence diagram. This tool saves me at least 30-60 minutes every single day. I’m not sponsored or affiliated with them in any way, but I do recommend you [try it yourself](https://excalidraw.com/)!

### **4.1 Diagrams - Only focus on one sub-system or flow at a time**

As a personal rule of thumb, I’ve learnt to limit the number of elements on any diagram to 10 or fewer 👐

I've both seen and created sequence diagrams that can span an entire page. This looks impressive, but it doesn’t do anyone any good. Here is an example from a paper I wrote that I bet no one ever looked at from start to finish.

[Figure 3 from the Relay Mining paper](https://arxiv.org/pdf/2305.10672)Instead, create a sequence of small palpable diagrams to avoid the cognitive overhead on the reader. It’s much easier to digest 3 diagrams with 4 steps than 1 diagram with 12 steps.

Leonardo da Vinci said it best:

> _“Simplicity is the ultimate sophistication.”_

[https://dev.poktroll.com/develop/developer_guide/quickstart#53-what-will-happen-later](https://dev.poktroll.com/develop/developer_guide/quickstart#53-what-will-happen-later)

## **5. Naming Things - You won’t regret verbosity down the line**

_tl;dr Use naming as an opportunity to Document Things so others can Move Fast by having everything be obvious and self-explanatory._

---

From my time at Twitter, I remember a service called [Gizmoduck](https://highscalability.com/the-architecture-twitter-uses-to-deal-with-150m-active-users/) 🤖 🦆

Though I do appreciate how fun and cool it is, it’s impossible to decipher that it was the User Account Service. If it was simply called UserService, it would be so much easier to search for, maintain and onboard new team members.

When it comes to document titles, you can probably pull off everyone remembering an essay titled “[Founder Mode](https://www.paulgraham.com/foundermode.html)” if you’re Paul Graham, but most of us aren’t. Having self-explanatory titles doesn’t only capture the reader’s attention, but also makes it easier to [Fuzzy Search](<https://en.wikipedia.org/wiki/Fuzzy_matching_(computer-assisted_translation)>) what you’re looking for.

For example, I could’ve titled this section “**Naming Things**”, but titling it “**Naming Things - You won’t regret verbosity down the line”** is an easy way for a larger portion of readers to get value from this post who might not be reading this particular sentence. If you’re still here, let me know ;)

Another example showcasing the importance of verbosity is this [20VC episode title](https://podcasts.apple.com/us/podcast/20vc-notions-founder-on-founder-mode-when-it-works/id958230465?i=1000669906963). It told me exactly what I should anticipate in the next 60 minutes and will be much easier to search for if I ever want to share it with a friend:

Code in software isn’t any different. Some would argue that the level of verbosity our team has in this function is excessive. However, I would say that anyone, whether you know how to code or not, can get a general understanding of what’s going on without being provided any additional context.

[https://github.com/pokt-network/poktroll/blob/f7b579493dc8d02ebdb43ae68d79d8cd3bdfb7f6/x/proof/keeper/proof.go](https://github.com/pokt-network/poktroll/blob/f7b579493dc8d02ebdb43ae68d79d8cd3bdfb7f6/x/proof/keeper/proof.go)There’s a common joke in software that naming things is hard:

> _“There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors.”_

_-- Leon Bambrick_

If this is something you struggle with, I suggest using ChatGPT or your LLM of choice. Provide it with the necessary content and ask for 10 different options for how to name something.

Everyone talks about how LLMs solved the Turing test but forgot that LLMs are also really good at one of the 2 hardest problems in computer science.

---

## **Bonus - How NOT TO document things**

Do not use long sentences

- Do not write long paragraphs

- Do not tell a story

- Do not create "the one document to rule them all"

- Do not create cognitive overload

- Assume the reader is lazy

- Assume the reader just wants to get back writing code

## **Bonus - How TO document things**

- Put yourself in the reader's shoes

- Use bullet points wherever possible

- Add visuals/diagrams whenever possible

- Keep diagrams focused on a single flow

- Write documentation you’ll only want to read yourself

- Use screenshots when appropriate

- Be pragmatic. There is a time and place to have official rules and standards, like if you’re contributing to the official cpython implementation, but on your team, just [Be Useful](https://www.amazon.com/Be-Useful-Seven-Tools-Life/dp/0593655958).

---

**These are just tools and suggestions I hope will help your team Move Fast & Document Things. They’re actionable, but do require a culture shift. Remember that good documentation is an art more than a science.**

“Learn the rules like a pro, so you can break them like an artist.”

- Pablo Picasso
