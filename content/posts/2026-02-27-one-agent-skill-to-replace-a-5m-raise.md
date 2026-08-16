---
title: "One agent skill to replace a $5M raise"
date: 2026-02-27T15:26:49-0800
draft: false
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

## The $5M pitch

[Command Code AI](https://commandcode.ai/) announced that they recently [raised $5M](https://www.linkedin.com/posts/commandcodeai_big-announcement-weve-raised-5m-led-by-activity-7432486791502532608-SMbK) to build a proprietary AI agent that learns your coding style; _taste_.

Meanwhile, [session-commit](https://github.com/Olshansk/agent-skills/tree/main/skills/session-commit) does the same thing with a markdown file and some vibes.

## How I discovered Command Code AI

When I [posted about session-commit](https://x.com/olshansky/status/2026000150611828885) on X, [another developer](https://x.com/vipulgupta2048) replied that he uses [@CommandCodeAI](https://x.com/commandcodeai) for taste learning. I was intrigued.

![Command Code AI vs session-commit](/images/posts/2026-02-27-command-code-ai-vs-session-commit.png)

---

## `session-commit` vs. Command Code AI

| Dimension           | **session-commit**                                                                  | **Command Code AI**                                             |
| ------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **What it learns**  | Durable project knowledge: architecture decisions, conventions, debugging playbooks | Personal coding style: naming, patterns, formatting preferences |
| **Where it stores** | `AGENTS.md`, a human-readable, version-controlled file in your repo                 | Proprietary model weights / taste profile (opaque)              |
| **How it learns**   | Explicit: you run the skill, review proposals, approve changes                      | Implicit: watches every accept/reject/edit continuously         |
| **Granularity**     | Project-level knowledge                                                             | Developer-level preferences                                     |
| **Portability**     | Fully portable. It's just a markdown file that any agent can read                   | Locked to their CLI (`npx taste push/pull`)                     |
| **Tool lock-in**    | None. Works with Claude Code, Codex, Gemini CLI, OpenCode                           | Requires `command-code` CLI                                     |
| **Transparency**    | 100%. You see exactly what's stored and can edit it                                 | Black box. You don't see the taste model internals              |
| **Team sharing**    | Share via git (it's in the repo)                                                    | Share via `npx taste push/pull`                                 |
| **Cost**            | Free / open source                                                                  | $10 credits, then paid                                          |

## The philosophical difference

- **Command Code AI** says: _"I'll silently watch how you code and adapt to your style."_ It's implicit, continuous, and developer-scoped.
- **session-commit** says: _"Let's explicitly capture what we learned and write it down for future sessions."_ It's explicit, intentional, and project-scoped.

**In reality, they're complementary more than competitive**. Command Code optimizes _how_ code is written (style/taste), `session-commit` optimizes _what the agent knows_ about your project (architecture, conventions, gotchas).

I still find it amazing that a simple open source skill can likely get you half of the way to a product that raised a $5M seed round.

## Try it yourself

**Install the skill:**

```bash
$ npx skills add olshansk/agent-skills
```

**Start a Claude Code session and do some work:**

```bash
$ claude
```

**When you're done, tell Claude capture your learnings:**

```text
> Use your session-commit skill!
```

That's it! More details [on GitHub](https://github.com/Olshansk/agent-skills/tree/main/skills/session-commit).

![session-commit feedback loop](/images/posts/2026-02-27-feedback-loop.png)
