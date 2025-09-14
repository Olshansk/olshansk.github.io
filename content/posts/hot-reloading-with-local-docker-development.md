---
title: "Hot Reloading with Local Docker Development"
date: 2020-07-19T21:01:38-07:00
draft: false
tags: ["docker", "ai", "python"]
categories: ["Programming", "DevOps", "Technology"]
summary: "tl;dr You can find the source code for a bare-bones dockerized python HTTP server with hot reloading using fastapi on this Github page."
---

### Hot Reloading with Local Docker Development

*tl;dr You can find the source code for a bare-bones dockerized python HTTP server with hot reloading using fastapi on this Github page.*

I recently came by this tweet:

- While there are many reasons to have separate Docker images for your development and production environments, it may be overkill for a small project you’re just starting. Over the past several years, I’ve been using the [volume mounting](https://docs.docker.com/storage/volumes/) feature in order to:Use the same Dockerfile for local development and production.
- Test against a locally running docker container.
- Have the docker container reflect changes I make to the source code on my host machine.
