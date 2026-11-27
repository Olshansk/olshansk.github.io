---
title: "Tuning: Skills vs. Parameters"
date: "2026-11-27"
draft: false
tags: ["blog"]
---

I spent about an hour thinking about what we do when we tune an agent. The part that finally clicked: we're doing a lot of the same work we did when we tuned machine-learning hyperparameters. The knobs used to be numbers. Now some of the most useful knobs are skills written in language.

The rest of the job still looks familiar. Define the inputs and outputs. Decide how the components fit together. Get reliable ground truth. Change something, run the system again, and see if it got better.

## Draw the box first

```text
       Task + context + short direction
                       |
                       v
  +--------------------------------------+
  | Agent                                |
  |   Model <-> Skills (guardrails)      |
  |     |                                |
  |     v                                |
  |   Tools: API / database              |
  +--------------------------------------+
                       |
                       v
           Output + resulting state
                       |
                       v
          Eval against ground truth
                       |
                 Revise skill
                       |
                 Run it again
```

The short direction gives the agent a goal. The integration does much of the work of specifying **what to do**: what comes in, which tools are available, how components pass data to each other, and what must come out. The model decides **how to do it** for the case in front of it. The skill can spend most of its words on **what not to do**: don't invent missing data, don't update a record outside the requested scope, and don't claim an action worked if you haven't verified it.

Sometimes the problem is deeper than the skill. If the API can't distinguish a new record from a duplicate, or the database schema can't represent the state you need, go fix that layer. Say a request times out after creating a record. A better sentence might make the agent more careful on a retry; an API that accepts an idempotency key can stop that retry from creating a duplicate. Use a hard constraint where you can enforce it, and a skill where the agent needs to exercise judgment.

## The eval is what lets you hill-climb

Take a small example: “Create one task due today with two undated subtasks.” The request and the task system together define the job. There's no need to dictate a sequence of tool calls. You can tell the agent not to date the subtasks, not to create duplicates, and not to report success until the saved records confirm it.

Ground truth is the state you can check: one parent with today's due date and exactly two linked, undated children. If the run says “done” and the database disagrees, it failed. If it got the right final state by changing an unrelated record along the way, it also failed. Check the result and the guardrails.

Then run a baseline. Keep the model, tools, and examples fixed while you change one skill. Run it again, repeat any noisy cases, and test the change on cases you didn't use to write it. Keep the revision if it helps without breaking something else. That's the hill climb: the agent figures out the steps in each run; we use the results to tune the conditions under which it chooses those steps.

A number and a paragraph look like very different things to tune. In both cases, the hard part is knowing what better looks like.
