---
title: "Signal vs Noise in the Skills Ecosystem"
date: 2026-02-28T13:00:00-0800
draft: true
description: ""
tags:
  [
    "AI Coding",
    "Agent Skills",
    "Claude Code",
    "Developer Tools",
    "Agentic Coding",
  ]
categories: ["Posts"]
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

## tl;dr <!-- omit in toc -->

There are 78K+ agent skills across 8K publishers. Most of them don't matter.

The data from [skills.sh](https://skills.sh/) tells a clear story:

1. Discovery is the killer app
2. Distribution follows a power law
3. Adoption rewards quality over quantity

**Ref**: [Skills Dashboard](https://skills-dashboard.olshansky.info/).

## 78K skills and counting

The skills ecosystem has exploded. As of the last day of February 2026, [skills.sh](https://skills.sh/) tracks:

- **78,362** total skills
- **8,064** publishers
- **9,996** repos
- **8M+** total installs

**I decided to visualize the data. You can access the dashboard [here](https://skills-dashboard.olshansky.info/).**

![Skills.sh Ecosystem Dashboard](/images/posts/skills_sh_summary.png)

That's a lot of skills. But raw counts don't tell you much.

## A long tail with a few giants

Like every marketplace, the distribution is a power law.

A handful of publishers (Microsoft, Vercel, inference-sh) dominate installs while thousands of others have near-zero adoption.

![Treemap: Install Share by Publisher](/images/posts/skills_sh_treemap.png)

Microsoft alone accounts for **~1.7M installs**. These are mostly Azure-related skills that I'd assume ship as part of their toolchain.

Vercel is second with **~893K installs**, largely driven by their own skills CLI ecosystem.

**The treemap makes it obvious**: if you're not in the top ~20 publishers, you're a pixel.

## The most popular skill is search

The #1 most installed skill? `find-skills` at **358K installs**.

![Top 30 Skills by Installs](/images/posts/skills_sh_top_installs.png)

**The most valuable thing in any ecosystem is helping people find what they need. Google won the internet with this insight**.

The skills ecosystem is no different: the meta-skill of _finding skills_ beats every individual skill.

After that, the top skills are opinionated best-practice guides: `vercel-react-best-practices`, `web-design-guidelines`, `remotion-best-practices`, `frontend-design`.

In the age of AI, developers don't just want tools, they want guardrails.

The Azure skills cluster (~89K installs each) is interesting too. Microsoft continues to win on bundling. Every Azure skill ships together, so they all have roughly identical install counts.

## Quality over quantity

**Here's where it gets spicy**. The publishers with the _most skills_ are not the ones with the _most installs_.

![Skill Count vs Total Installs by Publisher](/images/posts/skills_sh_count_vs_installs.png)

- `jeremylongshore` leads skill count at **935 skills**, but doesn't crack the top installs chart
- `Microsoft` has **98 skills**, but with **1.7M installs**
- `Vercel` has **56 skills**, but with **893K installs**

Publishing 900+ skills doesn't buy you adoption. Publishing 50 high-quality skills that solve real problems does.

This is the npm lesson all over again: flooding a registry with packages doesn't build trust. Curating a few excellent ones does.

## What this means if you're building skills

- **Discovery is everything.** If people can't find your skill, it doesn't exist. Write good descriptions, pick obvious names, and tag appropriately.
- **Opinionated > generic.** The top skills aren't utilities, they're best-practice guides. Developers want someone to tell them the right way to do things.
- **Bundling works.** Microsoft's Azure skills prove that distribution through an existing toolchain is a cheat code.
- **Don't spam the registry.** 10 great skills will outperform 1,000 mediocre ones every time.

## How can you replicate this analysis?

Install the skills:

```bash
npx skills add olshansk/agent-skills
```

Fire up Claude code:

```bash
claude

>  Can you prepare a dashboard of the distribution of skills at skills.sh?
```
