---
title: "A Boring but Practical 10-Step Guide to Data Labeling & Evaluation"
date: 2025-03-03T01:42:57-07:00
draft: false
tags: ["ai", "data-science", "machine-learning"]
categories: ["Technology", "AI"]
summary: "Below is a very terse and opinionated set of steps to data labeling and model evaluation."
medium_url: "https://medium.com/@olshansky/the-unsexy-truth-a-10-step-guide-to-data-labeling-that-actually-works-47f75828fd16"
ShowToc: true
---

### A Boring but Practical 10-Step Guide to Data Labeling & Evaluation

Below is a very **terse and opinionated** set of steps to data labeling and model evaluation.

I’ve found myself repeating this on a few occasions lately, so I’m publishing a short guide [I can link people to](https://simonwillison.net/2024/Jul/13/give-people-something-to-link-to/).

What’s written is applicable to traditional ML models before the infamous “ChatGPT moment,”* but it has become a much more ubiquitous concern nowadays. This omits a ton of details and nuances, but it’s enough to help build an intuitive foundation.

You might be wondering [who I am](https://olshansky.info/) and why I’m writing on this topic.

### From 2016 to 2020, I had the opportunity to architect [Magic Leap’s Augmented Reality Cloud](https://www.magicleap.care/hc/en-us/articles/9312806819597-AR-Cloud), focusing on mapping, localization, and spatial anchors. Later, I worked on [Waymo’s Planner Evaluation team](https://www.linkedin.com/jobs/view/senior-software-engineer-ml-planner-evaluation-at-waymo-4120748430/) with an emphasis on Vulnerable Road User (VRU) safety. In both roles, I wasn’t the lead algorithm or model developer, but I was “that engineer” — IYKYK — who got to collaborate closely with some of the most brilliant minds I’ve ever met.

### 10-Step Guide

- **Subjective Problem Definition**: Identify a problem that lacks a clear, objective answer.
- **Question Generation**: Build a set of simple binary or multiple-choice questions, including an “unsure” option for edge cases.
- **Expert Hunt**: Gather the world’s top experts (dozens), focusing on those who live and breathe the niche topic.
- **Expert Surveys**: Have these specialists answer the questions from Step 2.
- **Golden Data Creation**: Combine expert answers into a “[golden dataset](https://en.wikipedia.org/wiki/Golden_record_%28informatics%29).”
- **Large-Scale Labeling**: Expand to a crowd-sourced pool (hundreds or thousands). Aim for volume.
- **Labeler Scoring**: Compare the crowd’s labels to your golden data and assign each labeler (not label) a score.
- **Weighted Integration**: Use those scores to weigh the crowd-sourced labels during training, fine-tuning, RLHF, or downstream evaluations.
- **Embrace the Boredom**: Labeling is tedious and unsexy. Remind yourself that ‘true ground truth’* may not exist even with the world’s top experts in the same room.
- **Repeat the Cycle**: Keep iterating until you get lucky and see good results.

### **10-Step Example**

- **Subjective Problem Definition**: Is a particular crosswalk interaction between vehicles and pedestrians risky?
- **Question Generation**: Present a set of videos with multiple-choice answers ranging from ‘not risky’ to ‘very risky’ showing real or synthetic interactions between a vehicle and a pedestrian (i.e., a VRU).
- **Expert Hunt**: Gather dozens of high-paid PhDs from the world’s top academic institutions who specialize in the autonomous vehicle industry.
- **Expert Surveys**: Have them spend half their day labeling data instead of doing ‘intellectual’ work. Maybe host a pizza party to make it less dull.
- **Golden Data Creation**: Compile their answers into 1,000 golden labels (10 experts × 100 questions).
- **Large-Scale Labeling**: Use a crowd-sourcing system like [Mechanical Turk](https://www.mturk.com/) to scale labels from 1,000 to 100,000.
- **Labeler Scoring**: Compare the crowd labels to the golden dataset; grade each labeler’s [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall).
- **Weighted Integration**: Develop an internal, proprietary metric and discard labels that fall below a quality threshold.
- **Embrace the Boredom**: Acknowledge repetitive, unglamorous work and the absence of a perfect ground truth.
- **Repeat the Cycle**: Keep looping until the model behaves "good enough."

## Conclusion

Nothing here is ground breaking and companies like [Scale AI](https://scale.com/) are heavily leaning in this direction. I wouldn't be surprised if we'll see a marketplace of small but very expensive labeled data sets in the near future.

In the meantime, I hope this helped!

*[Note: Original post contained an AI-generated image here]*
