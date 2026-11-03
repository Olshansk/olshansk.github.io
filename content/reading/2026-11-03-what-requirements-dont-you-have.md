---
title: "What requirements can you have later?"
date: "2026-11-03T12:00:00-08:00"
draft: true
author: "Daniel Olshansky"
tags: ["TodayIRead", "Today I Read"]
capture_kind: "TIR"
source: "https://www.seangoedecke.com/what-requirements-dont-you-have/"
source_author: "Sean Goedecke"
---

This [short post](https://www.seangoedecke.com/what-requirements-dont-you-have/) by Sean Goedecke is a hidden treasure obscured by a simple title: `What requirements don't you have?`

He had a few cool callouts:
- `Statsd` uses UDP becomes dropping some data is fine in high volume/throughput analytics environments.
- `S3` doesn't support multi-key atomic updates.
- `uvicorn` has not shared mutable state between servers
- `sqlite` is just a file

We all know things need to be kept simple, yet we find ourselves overcomplicating it. Sometimes, it' human nature and we just need to catch our peers, and ourselves, in the act. 

The harder part goes beyond the requirements we set for ourselves. It extends into requirements we get from our users, or clients. The larger the client, the less maleable the requirements. This is where understanding, challengining, compromising and aligning on requirements is critical. And, it's not always a binary scale of accepting or rejecting a requirement. More often than not, it's about building a roadmap of milestones so you do not sacrifice delivery in liu of requirements, and only focus on the ones that are critical at any point in time. In some ways, we're reinventing agile. In other ways, it's incentive alignment to creat a win-win scenario.

So when requirements come up, don't always accept them at face value. Also, don't reject them outright. Identify which are critical for the business, and then stagger them accoringly to balance everything from customer asks, to security and deliverying value as fast as possible. 