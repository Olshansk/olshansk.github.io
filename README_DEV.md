# Olshansky's Personal Site <!-- omit in toc -->

- [Source Code](#source-code)
- [Deployment](#deployment)
- [Development](#development)
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
