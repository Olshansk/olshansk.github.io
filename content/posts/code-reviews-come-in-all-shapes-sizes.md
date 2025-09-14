+++
author = "Daniel Olshansky"
title = "Code Reviews Come in all Shapes & Sizes"
date = "2022-04-08T22:57:53.672Z"
description = ""
tags = [
    "crypto", "ai", "tech", "productivity", "book", "personal"
]
substack_url = "https://olshansky.substack.com/p/code-reviews-come-in-all-shapes-and"
+++

> Could you split this into two PRs, please?

Could you please approve this so I can merge it in?

Why are you implementing XXX using A rather than B?

NIT: extra space

In the context of code reviews, I’ve found myself on both the giving and receiving end of these types of comments more than once. I must say that the following [tweet](https://twitter.com/iamdevloper/status/397664295875805184?lang=en) still rings true today:

- Having worked on production systems at large companies, internal systems at mid-size companies and most recently joining a small and agile team, I increasingly realize that the purpose of code reviews depends on the stage and size of both the team and project.

For example, for a mature, production-grade, critical system at a large established company:

**Purpose**: Bug fix, new feature, code improvement, documentation update, etc...

- **Size:** < 300 lines of code

- **Timelines**: 1 - 3 days

- **Number of reviewers**: 2+ from designated language approvers & code owners

- **Risk**: changes could pose a high risk to the experience of millions of users or cost the company millions in revenue

- **Testing**: new unit tests or integration tests must be added, and all-the-thing must pass

- **Open-ended comments**: an excellent opportunity to ask questions, discuss ideas and learn asynchronously via discussion in comments

- **Offline discussion**: unlikely to be needed

- **Maintainability**: documentation must be updated, and the code must be easy to read & maintain

- **Expectations**: the process is most likely well-defined and known by others

I want to emphasize that the points above are a non-exhaustive list of an endless number of different permutations that I didn’t want to outline because I also don’t think anyone would be interested in reading them. So, for example, making a one-line consensus-breaking change to a blockchain with less than 1000 contributors known by everyone around the world, or building an internal tool at a large established tech company would follow completely different code-review protocols.

With that said, I recently had to review my first `+11,997 −188` [pull request](https://github.com/pokt-network/pocket/pull/47), and while it was daunting at first, I learned a lot of great things along the way. Aside from reviewing for business logic issues, code structure, documentation, tooling and tests, I learnt the following:

- **Purpose**: The primary purpose of the code review is knowledge dissemination and increasing the bus factor

- **Code practices**: It is an opportunity to start aligning on, but not objectively defining, standard code practices

- **Follow-up work**: Both parties need to expect that there will be more follow-up work/discussion created as a result of the review than it tends to

- **Offline discussion**: Multiple offline discussion or pair-coding sessions may be required

- **Open-ended comments**: As much as possible, comments that can lead to long discussions should be avoided - only leave those which are small, actionable and require two back & forth messages at most

- **Sharing is caring**: The author has to be open to the expectation that the reviewers will be pushing changes directly to their branch, which they would be responsible for reviewing themselves

- **Timelines**: Expect the review to last multiple weeks easily

- **Instructions**: The author must provide instructions, in text or in a meeting, on how the code should be approached - this is similar to documentation covering code/folder structure

My biggest recommendation would be to leave TODOs throughout the code and a single [mega-issue](https://github.com/pokt-network/pocket/issues/58) that covers all the follow-up work to be covered over time in meetings, discussions, or other code reviews. It’s the best way to keep moving forward while also realizing as many benefits as possible from the code review process.

Most importantly, it is an opportunity for the team to learn the most effective way to work together. This is an art more than a science, and while some rules (e.g. must have at least one approver) are necessary, you have to accept that most of the rules one has in mind or is accustomed to will be broken.

A code review is just as much about the journey as it is about the destination.

---

If you’ve made it this far, you can come join us at [pokt.network](http://pokt.network) in building a truly censorship resistant Web3 middleware stack that enables decentralized RPC access to more than 40 blockchains (quickly growing) with more than 40,000 nodes (also quickly growing) by applying [here](https://angel.co/company/pocket-network) or DM me directly [@Olshansky](https://twitter.com/olshansky)
