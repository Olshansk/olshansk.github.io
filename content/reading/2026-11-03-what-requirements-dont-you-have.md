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

- `StatsD` uses UDP because dropping some data is fine in high-volume/high-throughput analytics environments.
- `S3` doesn't support multi-key atomic updates.
- `uvicorn` has no shared mutable state between servers.
- `SQLite` is just a file.

We all know things need to be kept simple, yet we find ourselves overcomplicating them. Sometimes, it's human nature, and we just need to catch our peers, and ourselves, in the act.

The harder part goes beyond the requirements we set for ourselves. It extends into requirements we get from our users or clients. The larger the client, the less malleable the requirements. This is where understanding, challenging, compromising on, and aligning on requirements are critical. And it's not always a binary choice between accepting and rejecting a requirement. More often than not, it's about building a roadmap of milestones so you do not sacrifice delivery to satisfy every requirement and instead focus only on the ones that are critical at any point in time. In some ways, we're reinventing agile. In other ways, it's incentive alignment to create a win-win scenario.

So when requirements come up, don't always accept them at face value. Also, don't reject them outright. Identify which are critical for the business, and then stagger them accordingly to balance customer asks, security, and the need to deliver value as fast as possible.
