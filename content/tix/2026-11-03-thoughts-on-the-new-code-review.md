---
title: "Thoughts on the new code review"
date: "2026-11-03T12:00:00-08:00"
draft: false
author: "Daniel Olshansky"
tags: ["TIX", "TodayIIdeated"]
---

I did a quick reflection on how I've been approaching code reviews recently.

I recognized that I've been approaching code much more as a system than before. In particular, a code repository is a system that can be broken down into:

- **Components**: packages/directories that group the tasks.
- **Sub-components**: files that logically separate the business logic.
- **Details**: the contents of those files driving the implementation.
- **Connections**: interfaces in the form of APIs & MCPs.
- **Inputs**: configurations in the form of YAML, JSON, env variables, and user inputs.
- **Outputs**: artifacts that can take different shapes and sizes.
- **Supporting infrastructure**: documentation, testing, tooling, etc. to hold all of the above in place and maintain it.

The key differentiator today is that I don't spend time on the details. I still review the rest, but often with AI assistance rather than by scrolling through a UI.

There is a lot of detail I'm overlooking, and in some cases, you still need to look at the code. Nuance and circumstance matter.

However, for the vast majority of cases, code is just a system. With AI, we just don't need to worry about the details.
