---
title: "My Claude Code Agent for Writing Prompts"
date: 2025-09-28T14:55:44-0700
draft: false
description: "The only agent you'll ever need to write, maintain and update prompts."
tags: ["ai", "prompts", "tools", "agents"]
categories: []
medium_url: ""
substack_url: ""
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
---

As we shift from [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering) to [Context Engineering](https://x.com/tobi/status/1935533422589399127), one of the things I find myself ([and others](https://simonwillison.net/2025/Sep/14/models-can-prompt/)) doing is working with LLMs to craft the right prompt first.

## My LLM Stack

First, here’s my obligatory AI stack.

Daily drivers:

- **LLM Desktop Apps**: [ChatGPT](https://chatgpt.com/download/) and [Claude](https://claude.ai/download)
- **LLM CLIs**: [Codex](https://github.com/openai/codex), [Claude Code](https://github.com/anthropics/claude-code), [Gemini](https://github.com/google-gemini/gemini-cli), and more recently, [Copilot CLI](https://github.com/features/copilot/cli)
- [**Windsurf**](https://windsurf.com/): All the benefits of Visual Studio, which I use for editing and reviewing code. I still think its intelligent multiline autocomplete is unmatched.

Weekly tools:

- [**llm CLI**](https://github.com/simonw/llm): CLI by [Simon Willison](https://simonwillison.net/). If you’re into LLMs and don’t follow Simon, what are you even doing 😅
- [**LM Studio**](https://lmstudio.ai/): Replaced [Ollama](https://ollama.com) for me. Same value, better GUI, and more toggles for building intuition on how models run and can be tuned.

## Prompts Are Never Done

If you use LLMs regularly, you’ve probably written a bunch of prompts for slash commands, projects, experiments.

I’ve got around 10–20 I use consistently for ideation, writing, editing tweets, emails, docs, code reviews, and more.

What saddens me: most people treat prompts as **_“one and done.”_**

Prompts are like documentation. They’re living documents. They should be updated, tuned, and improved on a regular basis.

## Enter: The Prompt Writer Agent

**Problem:** Nobody wants to update prompts every day. It takes focus, clarity, and energy. Most of us just move on.

**Solution:** [Prompt Writer Agent](https://github.com/Olshansk/prompts/blob/main/agents/prompt-writer.md).

I’ve been running [this agent prompt](https://github.com/Olshansk/prompts/blob/main/agents/prompt-writer.md) as a [Claude Code](https://docs.claude.com/en/docs/claude-code/slash-commands) slash command for about a month. It’s already paying off.

## Workflow in Practice

Here’s how I usually wrap up a long, useful session in Claude Code:

1. Kick off the prompt writer agent. Literally, I just say: `Kick off the prompt writer agent`.
2. `cd ~/.claude` & run `git diff .`
3. Inspect and edit the changes to a new or existing slash command
4. Commit and push
5. QED.

Example: I used it during a session wrangling release builds across different architectures with custom tags. Not fun work, but AI made it manageable.

![Check it out here](/images/prompt-writer.png)

**Bonus:** If you drop this agent into `~/.claude/agents/prompt-writer.md`, you can use Claude’s `/resume` to turn past conversations into reusable slash commands.

## Why Claude Code?

To preempt the _“Why Claude Code and not X?”_ question…

Between [Anthropic’s recent postmortem](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) and the launch of [GPT-5 on Codex](https://openai.com/index/introducing-upgrades-to-codex/), OpenAI clearly has the lead on raw model quality.

But if history teaches us anything, the lead will keep flipping until both hit diminishing returns. That’s a bigger topic for another day.

Right now, Claude Code has the better UI. Even with the release of [Claude Code 2.0](https://www.npmjs.com/package/@anthropic-ai/claude-code), I expect all these tools will converge on the same feature sets soon.

## What’s Next?

If you find this useful, leave a ⭐ on the [repo](https://github.com/Olshansk/prompts) with the prompt. I plan to add all my prompts over time.

You can follow my [RSS feed](https://olshansky.info/index.xml), [Substack](https://olshansky.substack.com), [X](https://x.com/olshansky), [LinkedIn](https://www.linkedin.com/in/dolshansky/), or my newsletter:

{{< mailerlite >}}
