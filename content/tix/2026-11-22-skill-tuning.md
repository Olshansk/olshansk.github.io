---
title: "Skill Tuning"
date: "2026-11-22T14:22:17-08:00"
draft: false
author: "Daniel Olshansky"
tags: ["TIX", "TodayIIdeated"]
source: "https://x.com/olshansky/status/2124629445218623685"
---

How did we do things before? Hyperparameter tuning. How do we do things now? Skill tuning.

Instead of changing a learning rate or a batch size, I might change what a skill asks the agent to check, which examples it gets, or when it should stop and ask for help. I can change any of those in a few minutes. Knowing whether the change helped takes longer.

The work that hasn't changed is collecting reliable ground truth. If I'm tuning a code review skill, for example, I want a few real changes where I already know what a good review would catch and what it should leave alone. A longer review isn't necessarily a better one.

The question I keep coming back to: **Which hill do you climb?** Before I tweak the skill, I want to know what I actually want it to get better at.

[Original post on X](https://x.com/olshansky/status/2124629445218623685).
