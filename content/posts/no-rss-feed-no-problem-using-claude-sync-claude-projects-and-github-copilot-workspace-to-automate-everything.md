+++
author = "Daniel Olshansky"
title = "No RSS Feed? No Problem. Using Claude Sync, Claude Projects and GitHub Copilot Workspace to automate everything"
date = "2025-01-08T00:50:14.843Z"
description = "For anyone frustrated by missing RSS feeds in 2025."
tags = [
    "ai", "tech", "productivity", "book", "personal"
]
substack_url = "https://olshansky.substack.com/p/no-rss-feed-no-problem-using-claude"
+++

One of the things I love in our post _“ChatGPT Moment”_ era is the fact that I increasingly get to follow through on more and more side projects.

One of the things I find ridiculous in our 2025 post _“ChatGPT Moment”_ era is the fact that there are still a ton of blogs that don’t have a way for me to subscribe, be it through a proprietary service or a standardized RSS feed.

If a blog doesn’t have a **_Subscribe_**, I usually check for an existing _/feed.xml_ or _/index.xml_ file and use [blogtrottr.com](https://blogtrottr.com/) to send that feed into my email inbox. If neither exists, I now have an approach to adding and maintaining new RSS feed generators: [github.com/Olshansk/rss-feeds](https://github.com/Olshansk/rss-feeds).

# Exploring new tools

One of the things I love about [MrBeast](https://en.wikipedia.org/wiki/MrBeast) is that he actually does all the random crazy things we talk about with friends rather than just think about it. Similarly, AI tooling and infrastructure is enabling builders to materialize our creativity into real products.

More importantly, all the skills I build and learn from these little weekend quests directly transfer over into my day-to-day job as CTO of [Grove](https://grove.city). The team is more productive, we get more done in the same amount of time, and rather than spending time on hiring and recruiting, we invest that time in up-leveling each other instead. It feels like [Transfer Learning](https://en.wikipedia.org/wiki/Transfer_learning) but for humans.

This post is about how I used three new tools I got acquainted with over the holidays to easily create RSS feeds for any blog I want to follow that doesn’t already have one. Specifically, the tools I discuss here are:

- [Claude Projects](https://www.anthropic.com/news/projects); _launched by Anthropic in 06/2024_

- [ClaudeSync](http://ClaudeSync); _independent, open-source project_ _by [@jahwag](https://github.com/jahwag)_

- [GitHub Copilot Workspace](https://githubnext.com/projects/copilot-workspace); _technical preview by GitHub as of 01/2025_

# Missing RSS Feeds

A couple of months ago I discovered that the [RSS feed](https://paulgraham.com/rss.html) Aaron Swartz (RIP) created for from [Paul Graham’s essays](https://paulgraham.com/articles.html) was no longer getting updated. *Superlinear Returns, *from October 2023, was the last essay included in the feed.

- [https://www.paulgraham.com/](https://www.paulgraham.com/)I created [Olshansk/pgessays-rss](https://github.com/Olshansk/pgessays-rss) to solve this problem. I had a [short conversation](https://github.com/Olshansk/pgessays-rss/blob/main/prompt.md) with ChatGPT, had it create a python file that parses the HTML to generate an XML feed that’s RSS compatible, fixed a few bugs, used [GitHub actions](https://github.com/features/actions) to have the script run on a [cron schedule](https://en.wikipedia.org/wiki/Cron), and it’s been working pretty well.

_Little did I know that I would run into a similar problem again..._

Last week I was trying to subscribe to updates from [Ollama’s Blog](https://ollama.com/blog), but couldn’t find a subscribe button or an RSS feed. I wasn’t the only one with this request as I made my way to [GitHub issues](https://github.com/ollama/ollama/issues/1669) searching for a solution.

[https://github.com/ollama/ollama/issues/1669](https://github.com/ollama/ollama/issues/1669)I realized that this won’t be the last time I hit this issue, so I wanted to build something that’ll be more “sustainable.”

# Claude Projects

When it comes to coding tasks, Claude Sonnet 3.5 is competing for the top spots by some [mainstream benchmarks](https://lmarena.ai/), but more importantly, it’s leading the charge per [my personal vibe checks](https://olshansky.substack.com/p/vibe-checks-are-all-you-need). I’ve also been very happy with the UI that [Claude Projects](https://www.anthropic.com/news/projects) put together. It’s easy to setup the instructions, add knowledge, navigate past conversations, start new conversations, etc.

With the easy decision of using Claude and Claude Projects for development, what I wanted next was an easy way to introduce new parsers (i.e. feed generators) for blogs I come across.

Here is what I’m assuming:

Not all blogs have a subscribe button or an RSS feed

- All blogs I will care about will be rendered via HTML

Here is what I want:

- Foundational infrastructure to add, maintain and run multiple RSS feed generators

- Easily add new parsers (i.e. python files) anytime I want to subscribe to a new blog

- Convert any HTML into XML that’s RSS feed compatible

- Enable others to add their own parsers once things mature a bit; _i.e. make the Claude Project public_

- Limit the number of moving parts and overall complexity of this mini side project; _i.e. GitHub actions instead of maintaining a server_

With that in place, I create a Claude project with the following (v0) instructions:

The goal of this project is to generate rss (feed.xml) files from web pages (\*.html) that contain blogs or updates but do not provide a subscribe button or a default RSS feed.

Here is the expected flow and instructions:

1. You will be given an HTML file that needs to be parsed and understood.

2. You will provide a python script that writes a `feed_{}.xml` file that is RSS feed compatible.

3. The `{}` in `feed_{}.xml` will refer to the name of a particular RSS feed.

4. GitHub actions will take care of triggering this periodically, so you don't have to worry about it

5. If you are not given an HTML file that you can parse into an rss feed, either ask for it or explain what the issue with the provided file is.One of the great things about Claude Projects isn’t just the fact that you have baseline instructions, but also the fact that you can add knowledge to the project. I’m assuming it's a basic [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) pipeline behind the scenes.

However, keeping the knowledge up to date is a tedious and manual task, so I was sure there’s something better.

# Claude Sync

I only have support for two blogs at the moment ([Paul Graham](https://www.paulgraham.com/articles.html) and [Ollama](https://ollama.com/blog)), but every blog comes with some nuances when it comes to parsing.

Generating a parser for Ollama’s blog worked on the first time, but Paul Graham’s blog took a few iterations. I’m going to omit those the details because there’s nothing interesting to share. After some back & forth with Claude, we figured it out.

However, I want to reduce the amount of back & forth I (or others) have in the future. For that, I need to continue building up the project’s knowledge of which parsers I have and how they work.

[ClaudeSync](https://github.com/jahwag/ClaudeSync) is exactly what I needed. Here’s the pitch:

> ClaudeSync bridges your local development environment with Claude.ai projects, enabling seamless synchronization to enhance your AI-powered workflow.

I think it’s just a matter of time before Anthropic creates a native GitHub integration, but I’ve also worked for large companies, and know that good things take time to get right.

The `ClaudeSync` [README](https://github.com/jahwag/ClaudeSync/blob/master/README.md) is targeted at users that do not have an existing Claude Project created, so I had to associate my existing git repo with an existing Claude Project.

After installing `claudesync`*, *this was relatively straightforward. Each of the following instructions was supplemented with an intuitive REPL UX (give it a shot), and I just followed the instructions.

claudesync auth login
claudesync project init --name "RSS Feed Generator"
claudesync organization set
claudesync project setIt generated the following config file:

cat .claudesync/config.local.json
{
"active_provider": "claude.ai",
"local_path": "/Users/olshansky/workspace/rss-feeds",
"active_organization_id": "redacted-reda-cted-reda-cteredacted",
"active_project_id": "redacted-reda-cted-reda-cteredacted",
"active_project_name": "RSS Feed Generator"
}%I can set up an automatic schedule to push my local changes using `claudesync schedule`. For now, I’m just sticking with a manual `claudesync push`.

# GitHub Copilot Workspace

I recently got access to the GitHub Copilot [Workspace technical preview](https://githubnext.com/projects/copilot-workspace). Here’s the pitch:

> A Copilot-native dev environment, designed for everyday tasks.

The obvious things they forgot to mention is that it natively integrates with all the GitHub workflows and tooling we’re familiar with: GitHub workflows, PRs, Issues, etc.

Since the code to generate the RSS feeds was already in place, what I needed next was a GitHub Action that:

- Runs on an hourly basis

- Iterate and execute all the parsers I have today and will have in the future

My [zero-shot prompt](https://www.promptingguide.ai/techniques/zeroshot) with GitHub Copilot Workspace worked flawlessly. The UX was intuitive, the UI had everything I needed, and [generating the corresponding PR](https://github.com/Olshansk/rss-feeds/pull/1) was a simple click of a button.

https://copilot-workspace.githubnext.com/Olshansk/rss-feeds/pull/1I merged it in and it has been running smoothly since then. **Too easy.**

https://github.com/Olshansk/rss-feeds/actions

# Architecture Diagram: GitHub Copilot vs Claude

Once everything was in place, I realized that both GitHub Copilot and the Claude Project both have access to the entire repository. It felt like a good opportunity to generate an architecture diagram in case any future readers are interested in seeing how things work.

I use the following prompt and am showing the comparison between what the Claude Project and GitHub Workspace Copilot generated.

Can you create a mermaid diagram for how this repo works?

Include the following:

1. GitHub Action gets triggered hourly as a cron job.
2. run_all_feeds.py iterates through all the python files (one per blog) and generates an RSS feed for each one
3. The GitHub repo gets updated
4. External programs (e.g. blogtrottr) read it and process appropriatelyMermaid architecture diagram of the git repository comparison between Claude Project (left) and GitHub Copilot Workspace (right).Also, I’ve got to call out one of the killer features Claude has that ChatGPT is missing out on is native mermaid rendering.

Native rendering of mermaid diagrams in Claude

# Culminating Thoughts

I’ve been using [ChatGPT since the first day it came out](https://olshansky.substack.com/p/24-hours-of-chatgpt) and was using the GitHub Copilot technical preview back in 2021, but am still increasingly amazed and grateful by the tooling that we’re building.

All three of the tools I called out in this post are going to become part of my day-to-day and I’m going to make sure our entire team is using it. I don’t expect GitHub Copilot Workspace to compete with Claude on mermaid generation. It’s not an OR, it’s an AND.

I blog about a bunch of random stuff, and have more posts similar to this in the pipeline. If you enjoyed it, subscribe to my substack below. If you also want to keep up with some of my tv and book review, you can use my RSS feed: [olshansky.info/index.xml](https://olshansky.info/index.xml)

I’ll end it with one of [my favorite quotes](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/) from Simon Willison:

“The thing I’m most excited about in our weird new AI-enhanced reality is the way it allows me to be more _ambitious_ with my projects.”

- Simon Willison
