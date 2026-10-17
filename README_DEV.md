# Olshansky's Personal Site <!-- omit in toc -->

- [Source Code](#source-code)
- [Deployment](#deployment)
- [Development](#development)
- [Reading quotes](#reading-quotes)
- [Resources](#resources)
  - [TODO / Ideas](#todo--ideas)
  - [General](#general)
  - [Blogs](#blogs)
  - [Personal](#personal)
    - [Videos](#videos)
- [TV \& Movies](#tv--movies)
  - [Inspiration](#inspiration)
  - [Things I want to change:](#things-i-want-to-change)
    - [About page:](#about-page)

## Source Code

[github.com/Olshansk/olshansk.github.io](https://github.com/Olshansk/olshansk.github.io)

## Deployment

Live site: [olshansky.info](https://olshansky.info)

Deployed by **Vercel** on every push to `main`; pull requests get preview deployments.

- Dashboard: [vercel.com/olshansky/olshansk-github-io](https://vercel.com/olshansky/olshansk-github-io)
- Build config: [`vercel.json`](vercel.json) — this is the source of truth for `HUGO_VERSION`.

GitHub Pages is no longer used. When bumping Hugo, update `vercel.json` and
`.github/workflows/capture.yaml` together so CI validates the version production builds.

## Development

```bash
hugo server
```

## Reading quotes

The blog lives at `/posts/`; quotes and excerpts share `/reading/`.
The existing `/quotes/` log remains available and is tagged `quote`.
`blog`, `quote`, and `excerpt` are reserved content tags; the two blog posts previously using the topic tag `quote` now use `quotations` to keep the feeds separate.

| Content | RSS | Tag |
|---|---|---|
| Everything published | `/index.xml` | All tags |
| Blog | `/posts/index.xml` | `blog` |
| Quotes and excerpts | `/reading/index.xml` | `quote`, `excerpt` |
| Quotes (including the legacy log) | `/tags/quote/index.xml` | `quote` |
| Excerpts | `/tags/excerpt/index.xml` | `excerpt`, plus `TodayIRead` |

Each new capture target creates its own branch from `origin/main`, commits only its entry, runs capture tests and a production Hugo build, and opens a custom draft PR.
Requires authenticated `gh`, Git push access, Hugo, and uv.
The working checkout is left on its current branch. Each run reports its retained PR worktree for follow-up edits or failure recovery.
The targets never merge PRs. Blog entries also retain `draft: true` until explicitly approved for publication.

Create a blog draft from a Markdown body file (without frontmatter):

```bash
make new_blog TITLE="My post" BODY_FILE=/absolute/path/body.md
```

Capture a quote (AUTHOR and SOURCE are optional; never invent them):

```bash
make new_quote TITLE="A quote worth keeping" TEXT="Exact words" AUTHOR="Credited author" DATE=2026-10-17
```

Capture a sourced excerpt (SOURCE and AUTHOR are required):

```bash
make new_excerpt TITLE="An excerpt worth keeping" BODY_FILE=/absolute/path/excerpt.txt SOURCE="https://example.com/article" AUTHOR="Source author" DATE=2026-10-17
```

`TEXT` and `BODY_FILE` are alternatives. A body file avoids shell escaping for long text.
Dates default to the current day in America/Los_Angeles; pass `DATE` explicitly when capturing another day.
Quotes and excerpts preserve the supplied text as blockquotes with linked attribution and source author metadata.
Do not add commentary unless requested.
Existing `new_post`, `new_reading`, and `add_quote` targets remain local helpers without automatic PR creation.
When an agent invokes a PR target, attach the returned PR URL to the chat.

## Resources

Platform: [gohugo.io](https://gohugo.io/)
Theme: [hugo-coder](https://github.com/luizdepra/hugo-coder) \* [Configurations](Reference: https://github.com/luizdepra/hugo-coder/blob/main/docs/configurations.md)

### TODO / Ideas

### General

- [ ] Add search using LLMs or Algolia
- [ ] Filters by tag

### Blogs

- [ ] Export everything from substack and embed
- [ ] Export everything from medium and embed

### Personal

- [ ] Link to strava (exercise)
- [ ] Link to alltrails (hiking)
- [ ] Link to Apple Health (heart rate)
- [ ] Link to autosleep (sleep)

#### Videos

- [ ] Get control of my videos and upload to a personal channel

## TV & Movies

- [ ] Show the number of words in my review
- [ ] Make it look prettier

### Inspiration

https://howisfelix.today/?

### Things I want to change:

#### About page:

- [ ] Rename it to the now page:
  - Shorter paragraphs
  - Make it easier to read
  - Link to bluskey, mastodon, etc...
  - References:
    - https://now.page/
    - https://sive.rs/nowff
- [ ] Add a subscribe button that'll mirror the RSS feed
  - Notify people of book review
  - Notify people of movie reviews
