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

`/reading/` collects sourced excerpts under the `TodayIRead` tag, separate from original writing in `/posts/`.
Each excerpt has its own dated permalink, and `/reading/index.xml` includes the complete quote and attribution.
Reading entries are excluded from the main `/index.xml` feed; other existing feed content is unchanged.

Create a draft using the local date:

```bash
TZ=America/Los_Angeles make new_reading TITLE="Human Attention Is the Bottleneck"
```

Replace the template comment with the exact excerpt as a Markdown blockquote and a linked attribution containing the source title and author(s).
Set the frontmatter `author` to the source author(s) so metadata credits the quoted work.
Preserve spelling, punctuation, and paragraph breaks; do not add commentary unless requested.
Check for an existing entry with the same excerpt and source before creating another.
Use `draft: false` when publication is authorized, then run `make test` and `make test_workflow` before opening a PR.
Ordinary blog drafts retain their separate publishing workflow.

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
