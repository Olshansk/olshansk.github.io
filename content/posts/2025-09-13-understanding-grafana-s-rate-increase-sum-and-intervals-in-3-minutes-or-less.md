---
title: "Understanding Grafana’s rate, increase, sum and intervals in 3 minutes or less"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: ["Thought"]
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

* * *

### Understanding Grafana’s rate, increase, sum and intervals in 3 minutes or less

### tl;dr

  * Use `rate` when measuring `reuests-per-second`
  * Use `increase`



### **tips**

  * **Always use** an explicit time interval to reduce ambiguity of how you’re measuring things `[10m]`
  * Avoid using `$__rate_interval `Avoid using this in production dashboards. It can mislead you unless you know what’s happening
  * `AAvoid `
  * You need to add guards 


