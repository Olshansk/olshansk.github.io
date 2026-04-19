---
title: "Five Lessons from Agentic Backend Development"
date: 2026-01-21T10:27:20-0500
draft: false
description: ""
tags: []
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

1. **Iterate on a plan with agent**. Ask it questions and have it ask you questions. This is where focus, reading comprehension, learning and understanding the problem comes in. Show toggles in each agent
2. **Focus on E2E tests**. Different permutations of calling APIs, transforming data, etc… put this after the review. You can use this in CI, prevent regressions, and even have the agent fix itself.
3. **Review the interfaces**. Focus on reviewing APIS, schemas, functions. Also review the accompanying documentation because that’s what your agent will use to building understanding. Periodically ask your agent to reduce branching, make the code more idiomatic, simplify, remove and reduce the code’s surface area.
4. **Update AGENTs.md**. This is your teams best practices, except you only have to write it once, you don’t have to teach anyone, then don’t forget, and I’ve created a plugin you can install to make it even easier.
5. **Use logs to see what’s happening**. Emojis, colors, etc. As your E2E tests run, you don’t have a UI to check, so your visibility into what’s going on are the logs. Don’t be afraid of colors and emojis. Make them verbose

Bonus:

- Show examples
- Make my plugin installable
- Mention Todos
- Have a high-level and a deep dive
