# Demos Directory <!-- omit in toc -->

- [Overview](#overview)
- [Management Links](#management-links)
- [Adding New Demos](#adding-new-demos)
  - [1. Create demo directory](#1-create-demo-directory)
  - [2. Add routing to `vercel.json`](#2-add-routing-to-verceljson)
  - [3. Add domain in Vercel](#3-add-domain-in-vercel)
  - [4. Configure DNS (in Namecheap)](#4-configure-dns-in-namecheap)

## Overview

This directory contains static demo sites deployed as subdomains of `olshansky.info` using Vercel's multi-site routing.

## Management Links

- [Namecheap Advanced DNS](https://ap.www.namecheap.com/Domains/DomainControlPanel/olshansky.info/advancedns)
- [Vercel Domain Project Settings](https://vercel.com/olshansky/olshansk-github-io/settings/domains)

## Adding New Demos

### 1. Create demo directory

```bash
mkdir demos/[demo-name]
```

### 2. Add routing to `vercel.json`

```json
{
  "source": "/(.*)",
  "destination": "/demos/[demo-name]/$1",
  "has": [{ "type": "host", "value": "[demo-name].olshansky.info" }]
}
```

### 3. Add domain in Vercel

- Go to project settings → Domains
- Add `[demo-name].olshansky.info`
- Retrieve the records it provides for the next step

### 4. Configure DNS (in Namecheap)

`CNAME` Record:

- Type: `CNAME`
- Host: `[demo-name]`
- Value: `<REPLACE_WITH_VALUE>.vercel-dns-<REPLACE_WITH_VALUE>.com.`

`TXT` Record:

- Type: `TXT`
- Host: `_vercel`
- Value: `vc-domain-verify=[demo-name].olshansky.info,<REPLACE_WITH_VALUE>`
