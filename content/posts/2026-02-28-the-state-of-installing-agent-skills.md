---
title: "The state of installing agent skills"
date: 2026-02-28T12:08:07-0800
draft: true
description: "It's simpler than you think as long as you meet the user where they are"
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

We used to talk about "scaling software teams". Now we talk about "closing the loop".
Everyone says it, but no one does it, and all it requires is regularly maintaining your `AGENTS.md` file.

**It's simpler than you think as long as you meet the user where they are.**

## What is AGENTS.md?

- A single markdown file that tells AI agents how to work in your repo
- Think of it as onboarding docs, but for agents instead of humans
- Lives at the root of your repo (or nested per directory for monorepos)
- Every agentic CLI (Claude Code, Codex, Gemini CLI, etc.) reads it automatically
- I put together an easy-to-install extension: [agent-skills](https://github.com/Olshansk/agent-skills)

<!-- TODO: Add a gif showing installation via: npx skills add olshansk/agent-skill -->

## Why it matters

- Agents don't have tribal knowledge — they need it written down
- A good `AGENTS.md` eliminates 80% of "the agent did something dumb" complaints
- It compounds: every correction you capture prevents the same mistake forever
- It's the lowest-effort, highest-leverage thing you can do for agentic coding

## What goes in it?

- Project structure and architecture decisions
- Build, test, and lint commands
- Coding conventions and style preferences
- Common pitfalls and things to avoid
- Workflow preferences (e.g., "don't commit without asking")

## It can be as simple or as complex as you want

The point is to **start simple and iterate**. Here's one example from a developer who keeps it thorough:

<details>
<summary>Boris Cherny's CLAUDE.md</summary>

```bash
## Workflow Orchestration

### 1. Plan Node Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One tack per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests - then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.
```

</details>

## Nested CLAUDE.md files for monorepos

- For larger codebases, you can nest `CLAUDE.md` files in subdirectories
- Each subdirectory's file adds context specific to that part of the codebase
- The agent merges them: root-level conventions + directory-specific details
- See [this writeup](https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-md-for-larger-mono-repos.md) for a detailed breakdown

## The feedback loop

- You tell the agent what to do
- The agent does it (sometimes wrong)
- You correct it
- **You (or the agent) updates `AGENTS.md` with the correction**
- The agent never makes that mistake again

That last step is the one everyone skips.
It's the whole game.

## Every org should have a public agent-skills repo

Every org should have a public "agent-skills" repo similar to [Vercel's](https://github.com/vercel-labs/agent-skills).
It's the easiest way to share institutional knowledge with every agent that touches your stack.

## The Skills Ecosystem

The "skills" paradigm is being adopted across every major agentic CLI:

- Open standard: https://agentskills.io/
- Anthropic: https://github.com/anthropic/skills
- OpenAI: https://developers.openai.com/codex/skills/
- Gemini: https://geminicli.com/docs/cli/skills/

### Finding a Skill

Vercel has a [useful article](https://skills.sh/vercel-labs/skills/find-skills) on this.

It's as easy as this:

```bash
npx skills find "earning as a content creator"
```

<details>
<summary>Output</summary>

```bash
Install with npx skills add <owner/repo@skill>

rocket-repos/agent-skills@amazon-associates 36 installs
└ https://skills.sh/rocket-repos/agent-skills/amazon-associates

guia-matthieu/clawfu-skills@transcription-to-content 7 installs
└ https://skills.sh/guia-matthieu/clawfu-skills/transcription-to-content

chadboyda/agent-gtm-skills@content-to-pipeline 5 installs
└ https://skills.sh/chadboyda/agent-gtm-skills/content-to-pipeline

maigentic/stratarts@social-media-strategist 5 installs
└ https://skills.sh/maigentic/stratarts/social-media-strategist

chadboyda/agent-gtm-skills@solo-founder-gtm 5 installs
└ https://skills.sh/chadboyda/agent-gtm-skills/solo-founder-gtm

maigentic/stratarts@content-marketing-strategist 4 installs
└ https://skills.sh/maigentic/stratarts/content-marketing-strategist
```

</details>

### Vercel

Vercel introduced the [skills CLI](https://github.com/vercel-labs/skills).

You can read about it [in this announcement](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem) or view their [skill.sh](https://skill.sh/) directory.

It's pretty straightforward to use and navigate. The setup process is quick and easy too.

```bash
$ npx skills

The open agent skills ecosystem

  $ npx skills add <package>        Add a new skill
  $ npx skills remove               Remove installed skills
  $ npx skills list                 List installed skills
  $ npx skills find [query]         Search for skills

  $ npx skills check                Check for updates
  $ npx skills update               Update all skills

  $ npx skills experimental_install Restore from skills-lock.json
  $ npx skills init [name]          Create a new skill
  $ npx skills experimental_sync    Sync skills from node_modules
```

### Coinbase

The payment skills by [Coinbase](https://docs.cdp.coinbase.com/agentic-wallet/skills/overview) are really useful IMO:

```bash
Skill	Description
authenticate-wallet	Sign in to the wallet via email OTP
fund	Add money to the wallet via Coinbase Onramp
send-usdc	Send USDC to Ethereum addresses or ENS names
trade	Trade tokens on Base
search-for-service	Search the x402 bazaar for paid API services
pay-for-service	Make paid API requests via x402
monetize-service	Build and deploy a paid API that other agents can use via x402
```

### OpenClaw

[clawhub.ai](https://clawhub.ai/) is the equivalent of [skill.sh](https://skills.sh/) for [OpenClaw](https://openclaw.ai/).

It has it's own [clawhub](https://docs.openclaw.ai/tools/clawhub) CLI, which I anticipate is going to be deprecated in the not too distant future.

### Add skills via CLI

#### HuggingFace

A [cool pattern](https://www.linkedin.com/posts/julienchaumond_from-now-on-each-library-or-cli-should-bundle-activity-7424122218856656896-JKq_) from the CTO of HuggingFace is leveraging their CLI to install skills.

Assuming you already have the [hf CLI](https://huggingface.co/docs/huggingface_hub/en/guides/cli) installed,

```bash
hf skills add --claude --codex --opencode
```

which simply downloads your files and creates the necessary symlinks:

```bash
$ hf skills add --claude --codex
Installed 'hf-cli' to central location: /Users/olshansky/workspace/.agents/skills/hf-cli
Created symlink: /Users/olshansky/workspace/.claude/skills/hf-cli
Created symlink: /Users/olshansky/workspace/.codex/skills/hf-cli
```

There's more to understand here: https://huggingface.co/docs/huggingface_hub/en/guides/cli

#### Sentry

npm install -g @sentry/warden

Need to dive in and understand this a little more: https://warden.sentry.dev/

### Codex UI

![Codex Skills](/images/posts/codex_skills.png)

Here's an example of using [render](https://www.linkedin.com/posts/renderco_build-with-agents-deploy-on-render-the-activity-7424169721782124546-Sd4z)

### Skills Directories

- [skills.sh/](https://skills.sh/) by Vercel
- [anthropics/skills](https://github.com/anthropics/skills)
- [openai/skills](https://github.com/openai/skills)
- [clawhub.ai/](https://clawhub.ai/) by OpenClaw for your claws
- [vibeindex.ai/skills](https://www.vibeindex.ai/skills)

## References

- [agent-skills](https://github.com/Olshansk/agent-skills) — Easy-to-install AGENTS.md extension for your agentic CLI of choice
- [Claude Code best practices: nested CLAUDE.md files](https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-md-for-larger-mono-repos.md)
- [Boris Cherny's tips on using Claude](https://gist.github.com/joyrexus/e20ead11b3df4de46ab32b4a7269abe0)
