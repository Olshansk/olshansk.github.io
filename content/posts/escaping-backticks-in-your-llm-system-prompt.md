---
title: "Escaping Backticks in your LLM System Prompt"
date: 2025-05-06T20:12:32-07:00
draft: false
categories: ["Technology"]
summary: "tl;dr If you ever write documentation, add this to your LLM’s memory, system prompt, project, rules or whatever your equivalent of that is."
---

### Escaping Backticks in your LLM System Prompt

*tl;dr If you ever write documentation, add this to your LLM’s memory, system prompt, project, rules or whatever your equivalent of that is.*

```
Always render markdown responses using a method that avoidsbreaking when triple backticks are nested.Prefer one of the following in order:1. Use outer code blocks with four backticks (````) if the content includes nested triple backticks2. Escape inner backticks using \```3. Use indented code blocks
```
