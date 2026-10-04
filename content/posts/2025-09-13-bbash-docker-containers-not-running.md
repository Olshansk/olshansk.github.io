---
title: "BBash Docker containers not running"
date: 2025-09-13T12:00:00-07:00
draft: true
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

* * *

### BBash Docker containers not running

diff <(docker ps — format ‘{{.Names}}’ | grep ‘sage’) <(docker ps -a — format ‘{{.Names}}’ | grep ‘sage’)
