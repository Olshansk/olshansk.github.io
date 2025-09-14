+++
author = "Daniel Olshansky"
title = "Data Odyssey: Taking Control of my Rotten Tomatoes"
date = "2023-07-02T20:10:33.625Z"
description = "Episode I: Rise of the Independent Critic"
tags = [
    "ai", "tech", "productivity", "book", "personal"
]
substack_url = "https://olshansky.substack.com/p/data-odyssey-taking-control-of-my"
+++

# The Exposition: Roll Camera on Your Average Movie Watcher

Not much different from your typical consumer, I've been a fan of films and TV shows since I was a kid. The genres have changed and my viewing frequency has dropped, but the essence remains. Once streaming became available, I never got into the habit of binging shows with the exception of a few cases (_cough Lost cough_); if I really like a show, I try to prolong that experience for as long as possible. About a decade ago, I realized that I was investing so many hours consuming the hard work and passion of others, so it seemed fair to spend a few minutes leaving a public rating or review. That's when Olshansky's [Rotten Tomatoes](https://www.rottentomatoes.com/profiles/GeDt0zCK1fenF8NTwehrduK0seeCXJTL4H28fjquRRCzRi1zIknSwBFllCxgFepIjgSZRuYYCdOcNGtk2Fv2HmWu9zSxLTZQfJjIB1FVKuYj) account was born 🍅.

As someone who thinks a lot about decentralization, I've never proclaimed that "_you **MUST ALWAYS** own your data."_ I believe it depends on the situation and involves trade-offs across several dimensions, including privacy, convenience, cost, and others. What I do champion, however, is user optionality. The decision about how much responsibility and effort a person is willing to take on in exchange for privacy and control should be theirs. For example, I derive so much value from Google Photos for the price I pay that I'm okay with all the training and modeling they likely do with it.

Regarding my TV and movie ratings and reviews, I never worried about the privacy or control of my data as long as it was always accessible and searchable when I needed it. Over the years, I got into the habit of heading to Rotten Tomatoes to leave a rating and a couple of sentences after finishing a show season or watching a film. At this point, I’ve reviewed hundreds of shows and movies and have hundreds on my _to-watch_ list as well:

# The Conflict: Rotten Support

Although it’s far from perfect, and arguably quite a distance from good, Rotten Tomatoes has gotten the job done for over a decade. It's been an invaluable tool to help me track what I've watched, what I plan to watch, and most importantly, I've found the ratings to be a dependable indicator of whether I’d like a certain show or movie; a Tomatometer score above 90% has yet to let me down.

That said, I can't shake the impression that Fandango, the parent company of Rotten Tomatoes, has stopped investing resourcing into maintaining or improving the site. It’s functional but feels antiquated, sluggish, and unreliable. The rating format is restricted to plaintext, some of my reviews have been lost on occasion, and there's no easy way to sift through my watch history besides repeatedly clicking _`next`,_ over and over….

** I give Rotten Tomatoes 1 ⭐️ and 5 rotten 🍅s **

One day I woke up (_worked out, took a cold shower, meditated_) and decided: I no longer felt comfortable entrusting Rotten Tomatoes with the long-term security and accessibility of my data. To put it in perspective, I still do trust Google to keep my photos safe, redundant, and readily available for the time being.

My first step was reaching out to request a data export.

After a ten-day wait, a response came through.

The thought crossed my mind to play the GDPR card, but it seemed like it might be a futile effort with the same disappointing result. So, I took things into my own fingertips. If anything, this experience only reaffirmed my prior sentiments about Rotten Tomatoes.

# The Rising Action: The Pursuit of Independence

A trip to their [developer page](https://developer.fandango.com/rotten_tomatoes) revealed a process that needed an application and appeared as though it hadn’t seen an update in ages. Their so-called _“Interactive API”_ was about as interactive as watching a painted wall dry.

But never fear, Chrome DevTools was here to save the day! 🔧

A dive into the Network tab in console led me to the request that loads the next set of movies or shows when scrolling through the user interface.

Following this, I headed over to one of my go-to websites, [curlconverter.com](https://curlconverter.com/). It’s a handy site that lets you paste in a curl command and outputs the corresponding Python code.

From there, it was as simple as removing the _'after'_ key, increasing the `*pagecount`\* from 10 to 1000, and dumping everything into a JSON file.

And just like that, **Voila!** 🪄

I now had a JSON dump of all my reviews at my fingertips.

# The Climax: One Small (_git_) Push for Olshansk

With a little bit of Python foo that you can check out [here](https://github.com/Olshansk/olshansk.github.io/blob/main/rotten_tomatoes_to_hugo/hugo.py), and one small git push to [olshansk.github.io](https://github.com/olshansk/olshansk.github.io) (a [Hugo](https://gohugo.io/) powered personal site using the [Coder](https://github.com/luizdepra/hugo-coder) theme), everything fell into place.

The climax of this page of the story, it turns out, was far from climactic.

# The Falling Action: Gateway to a New Universe

Not only did this journey grant me ownership and searchability of my data, but it also opened the gate to a whole universe of new opportunities!

Consider [this recent review](https://olshansky.info/movie/spider-man_across_the_spider_verse/) I did of the new Spider-Man movie. I can now use paragraphs, apply markdown formatting, go wild with emojis, share it with friends, and there's absolutely nothing stopping me from rating it more than 5/5! 🧙‍♂️

# The Denouement: Next on the Menu, The Cheese

This is merely just the opening act. While it might have gone undocumented, the foundation of this data odyssey was setting up my personal site, [olshansky.info](https://olshansky.info/), the dough of my pizza if you will. Now that I've reclaimed the Rotten Tomatoes, slathering a flavorful sauce over my dough, it's high time to start grating the cheese. 🧀

Goodreads, Medium, social networks, and not least of all Substack, where you're likely reading this at the moment, should take note that this pizza 🍕 is ready for an unlimited array of toppings.

** For my Italian friends reading this, I apologize if I’m getting the order wrong with the toppings. **

---

Thanks for reading Olshansky's Newsletter!

If you read kept reading this far and are interested in doing it yourself, I’ve provided some more tactical documentation others can reference [here](https://github.com/Olshansk/olshansk.github.io/tree/main/rotten_tomatoes_to_hugo).

In case you’ve been keeping count, I wrote "Rotten Tomatoes" 9 times in this post. Counting the previous sentence, we're now at an even 10.

A special shoutout to my trusty companion, GPT-4, for the meticulous review and edits of this post, and for the indispensable assistance with the scripts.

☝️ This last sentence came straight from GPT-4 so you can tell it thinks quite highly of itself.
