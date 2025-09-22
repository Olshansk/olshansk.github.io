# Demos Directory <!-- omit in toc -->

- [Overview](#overview)
- [Management Links](#management-links)
  - [DNS Management](#dns-management)
  - [Vercel Project Settings](#vercel-project-settings)
- [Adding New Demos](#adding-new-demos)
- [DNS Configuration](#dns-configuration)
- [Current Demos](#current-demos)
  - [XSwipe (`xswipe.olshansky.info`)](#xswipe-xswipeolshanskyinfo)

## Overview

This directory contains static demo sites deployed as subdomains of `olshansky.info` using Vercel's multi-site routing.

## Management Links

### DNS Management

- [Namecheap Advanced DNS](https://ap.www.namecheap.com/Domains/DomainControlPanel/olshansky.info/advancedns)

### Vercel Project Settings

- [Domain Settings](https://vercel.com/olshansky/olshansk-github-io/settings/domains)

## Adding New Demos

1. **Create demo directory**:

   ```bash
   mkdir demos/[demo-name]
   ```

2. **Add routing to `vercel.json`**:

   ```json
   {
     "source": "/(.*)",
     "destination": "/demos/[demo-name]/$1",
     "has": [{ "type": "host", "value": "[demo-name].olshansky.info" }]
   }
   ```

3. **Configure DNS** (in Namecheap):

   - Type: `CNAME`
   - Host: `[demo-name]`
   - Value: `cname.vercel-dns.com`

4. **Add domain in Vercel**:
   - Go to project settings → Domains
   - Add `[demo-name].olshansky.info`

## DNS Configuration

For each subdomain, add a CNAME record:

- **Type**: CNAME
- **Host**: `subdomain-name`
- **Value**: `cname.vercel-dns.com`
- **TTL**: Automatic

## Current Demos

### XSwipe (`xswipe.olshansky.info`)

- **Directory**: `demos/xswipe/`
- **Description**: Smart gesture navigation landing page
- **Status**: Configured, needs DNS verification
