---
title: "A view on ai agents through the less"
date: 2025-09-13T12:00:00-07:00
draft: true
description: ""
tags: ["Post"]
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

Monday morning rough thoughts:  
Task: 

Ai agents finding and downloading new tools is complex

  * Dependencies are still hard to work around

  * I build a self updating homebrew tap but even gpt4o made lots of mistakes

  * I tried fine tuning models, but I’ve found that it’s good at changing tone but know context or speciality

  * My intuition is telling me that you kind need very large, diverse high quality data sets in the pre training phase

  * I don’t think this is something.l a hacker does

  * Look - the only models I used are by those with deca billions in funding

  * The original blog post is now just an appendix

  * Search for what ai agent levels are

  * Create my own

  * I get at least one person sending me a tweet to something ai agent related

  * Most data is the same

  * It’s used too statically and not easy to get a real data sets

  * Even if you go into a megacorp like Bloomberg, I’m sure 80% of the data is either noisy, reparative or garbage

  * Most models are@overturned to benchmarks

  * Solving benchmarks is like saying SATs are a direct representation of how successful someone will be




 _tl;dr_

  1.  _Picking up a nearly year old draft really forced me to reflect on how much things have changed_

  2.  _There’s an open question of what the definition for “AI Agent” is and when they’ll be fully autonomous_

  3.  _LLM enhanced development enables 10x Software Engineering at 0.1x the cost_

  4.  _I argue that that having a Software-Engineer-In-The-Loop is where most of the gains will be_




* * *

I originally started writing this blog post early in 2024 when I wanted to document how I used AI-enhanced development to retrieve my photos from an old iOS backup.

Since then, one could say that everything has changed yet nothing has changed in the world of LLMs. 

While brushing up the post, I started reflecting on when (if?) an autonomous AI agent could fully replaced my prior workflow, so the scope grew quite a bit.

This blog post is therefore split into two parts:

  1. **A reflection of AI agents today** (late 2024)

  2. **How I use LLMs to retrieve my photos from depreciated iOS apps** (early 2024)

  3. 


# Preface - A retrospective on capabilities of AI Agents over the past year

## A blog post that’s 242 days late

 _Better late than never, right?_

I’ve taken 242 daily photos since I first started working on this blog post. That’s how long it took me to finish this. There was no technical hurdle. Life didn’t get in the way. I could have prioritized it if I wanted to…

If you’re reading this, it means I got it to a publishable state. More interestingly, it enabled me to reflect on almost a year of advancement in the AI space.

Originally, when I started writing this blog post, my goal was to capture how I use LLMs (_aka AI_) to navigate multiple technical challenges that I otherwise would not have taken on in my free time. 

If I were to do it all over again today, I would not have done anything differently. I find this interesting because I think it points to a particular subset of problems where LLMs will continue needing a human in the loop.

## AI Agents In Theory - An autonomous world of limitless capability

The story below documents how I used different environments, platforms, tools and multiple programming languages to retrieve my photos stored on multiple applications. Being somewhat technically astute, [AI-enhanced development gave me the ambition to figure out](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/) how to extract everything. If it weren’t for modern AI tooling, I wouldn’t attempt it. If I wasn’t a software engineer, I wouldn’t even consider it.

I posed a question to myself: can the workflow I outlined below every be replicated by fully autonomous AI agents?

If I put on my sci-fi hat 🧑‍🔬️🎩, I’d envision a world where different entities (for-profit organizations, academic institutions, professors, students, hackers, or other AIs) would train and custom models with a very particular set of skills. They would specialize in a narrow stack like databases, cryptography, iOS, computer vision, and so on… Through a Monte Carlo simulation like mechanisms, these models would talk to each other, working through every possible scenario. We can even draw an analogy from Hugh Everett’s [Many Worlds interpretation](https://en.wikipedia.org/wiki/Many-worlds_interpretation), where the agents hit hundreds of thousands of dead ends, but since every possible outcome would be iterated, some of those branches would have a successful resolution. More importantly, all of it is near-instantaneous because Meta and others have lots latent NVIDIA GPUs that we can leverage for inference as we prepare to kickoff pre-training for the next set of major foundation models.

[![](https://substack-post-media.s3.amazonaws.com/public/images/502bba7a-f39a-481f-a4ff-3051a8e9d2eb_698x400.jpeg)](https://substackcdn.com/image/fetch/$s_!rIhG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F502bba7a-f39a-481f-a4ff-3051a8e9d2eb_698x400.jpeg)What if agents actually refer to secret agents?

Is this theoretically possible possible? Yes. But, there are a lot of technical hurdles that need to be overcome from network effects, decentralization, access to compute as well as agent quality on both the pre-training, fine-tuning and feedback fronts. 

## AI Agents In Practice - Intelligence Amplification

Practically speaking, I want to but struggle to believe that completely autonomous agents will struggle to replicate what I outlined below.

I’m fortunate enough to have multiple friends who work on AI research across several of the leading players in the field. The general vision everyone is aligning are what I like to refer to as **Cron Agents:** long-lived AI agents that operate like cron jobs. They process things asynchronously for multiple hours or days at time, come back with some intermediate results, ask for feedback and off they go again.

This is getting more real, but the question remains of how autonomous could or should something be for it to be called an AI Agent?

has literally been harping on this topic for over a year   


[![](https://substack-post-media.s3.amazonaws.com/public/images/eb0bf617-0a61-456f-b182-3720c761e974_1344x594.png)](https://substackcdn.com/image/fetch/$s_!eBE8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb0bf617-0a61-456f-b182-3720c761e974_1344x594.png)[Post from October 2023](https://x.com/simonw/status/1718255087947255870)

[![](https://substack-post-media.s3.amazonaws.com/public/images/8a801528-e668-4f4d-a2e0-fb21b3f92363_1348x1396.png)](https://substackcdn.com/image/fetch/$s_!H0D1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a801528-e668-4f4d-a2e0-fb21b3f92363_1348x1396.png)[Post from October 2024](https://x.com/simonw/status/1845080654918119547)

Andrej Karpathy [famously tweeted](https://x.com/karpathy/status/1744179910347039080) that we should be thinking of AI more as IA, _**Intelligence Amplification**_.

Bill Guerly recently talked about how everyone is seeing models top out

https://share.snipd.com/snip/7a10cd72-6b39-475a-9868-1fdde70bc7d3

  1. Humans

  2. Machine Learning Assisted

  3. Intelligence Amplification

  4. Humans in the loop (developers)

  5. Humans in the loop (non developers)

  6. No Humans




We are currently at 3.5. 

https://www.faistgroup.com/news/autonomous-vehicles-levels/

I think it’s similar to the Autonomous Vehicle Levels but is going to take much longer to play out.

It’s really hard for me to imagine how an AI agen

**Call To Action (📣👉💥) : If you read through the entire post below and have thoughts on how AI agentswhole post, I’d love to hear if you think AI will ever be capable of tackling this independently.**

* * *

# Taking control of my photos with ChatGPT

## Daily Photos - An Origin Story

A little over four years ago I decided to start taking a daily morning photo to keep track of how my body is changing. I figured there must be at least a dozen apps already built for this, so I ended up settling on [seeyourprogress.com](https://www.seeyourprogress.com/) which seemed to have a pretty good set of features.

[![](https://substack-post-media.s3.amazonaws.com/public/images/c73b2e92-98ce-4e67-8af2-b3140a5f3571_1270x2394.png)](https://substackcdn.com/image/fetch/$s_!GafI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc73b2e92-98ce-4e67-8af2-b3140a5f3571_1270x2394.png)[seeyourpgoress.com](https://seeyourprogress.com/)

In 2021 I upgraded from my iPhone XS to my iPhone 13, which I still have to this day, and learnt that the _Progress_ app was no longer maintained or supported on newer versions of iOS. **I created an offline backup of my phone, stored it on an external hard drive, and decided that one day I’d figure out how to get my data out.**

In the meantime, I started using [Body Tracker](https://apps.apple.com/us/app/body-tracker-photo-measure/id1265152738) instead. I learnt my lesson and made sure to choose an application that lets me export my data. It was newer, had a lot of positive ratings and even claimed to have iCloud sync, as see in the image below.

[![](https://substack-post-media.s3.amazonaws.com/public/images/00dadccd-eeaa-480c-a088-3cc55f0c7112_1446x2394.png)](https://substackcdn.com/image/fetch/$s_!p4mK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00dadccd-eeaa-480c-a088-3cc55f0c7112_1446x2394.png)[Body Tracker on the iOS App Store](https://apps.apple.com/us/app/body-tracker-photo-measure/id1265152738)

After using this app for a couple of years, I noticed that its performance started to degrade. It would take longer to open up, the buttons would be less responsive, and everyone ever more frequently, the photos I took simply disappeared into the abyss.

Having built a few non-performant iOS Applications as an intern [ModiFace](https://modiface.com/) in 2011, I knew that the all of the images must be stored and loaded into memory every time I opened the app.

The performance continued to degrade. The app started crashing on me. It become completely unusable.

## Asking for help with no response…

I knew I could figure out how to extract the photos for both the Progress & Body Tracker applications, but didn’t want to invest the time.

I tried reaching out to the developers of both applications in various ways: reviews, contact us forms, online stalking, etc… I reasoned that if they had access to the original source code, I could send them a backup of my data and they’d be able to get my photos in less than 15 minutes. I’d be more than happy to pay them whatever they deem is fair as well.

I had a TODO where I tried reaching out to the authors of both applications on a monthly basis, and it just kept rolling from one month to another.

Eventually, I got frustrated and decided to do it myself. The only reason I took this on is because I knew I had ChatGPT to help me out. When I first created the backup of the Progress App on my iPhone XS, ChatGPT didn’t even exist!

## ChatGPT - Solving the Cold Start Problem

In the past, embarking into a new technical domain was always scary, daunting, and challenging. It would involve browsing many web pages, finding the perfect “Getting Started” guide if you’re lucky, potentially taking an online course if you’re committed, or reaching out to an expert friend (i.e. a consultant) if you’re network is big enough.

**ChatGPT has completely solved the cold start problem.**

Off the top of my head, here are just a few prompts to easily go from 0% to 50% in any domain:

  1. Help me build intuition around X.

  2. I need to accomplish Y, what are the top 10 questions I should ask to get started?

  3. What are the top 10 tools to do Z? Provide 1-3 bullet points with pros & cons for each one.

  4. I have zero expertise in domain D, help me get started.




A custom tool, product or company can definitely help, but vanilla ChatGPT is good enough.

## Progress Application - Getting my photos

The progress app has a [crunchbase page](https://www.crunchbase.com/organization/progress-app) but I still had no luck or success in reaching out to them.  
  
I asked ChatGPT what’s a good free tool I can use to extract data from an iPhone backup and it led me [iPhone Backup Extractor](https://www.iphonebackupextractor.com/).

[![](https://substack-post-media.s3.amazonaws.com/public/images/3833f5a9-3f1b-4786-b9b7-182fda7fc2b9_2724x1490.png)](https://substackcdn.com/image/fetch/$s_!im0e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3833f5a9-3f1b-4786-b9b7-182fda7fc2b9_2724x1490.png)

After a little bit of meddling and filesystem exploration, I found a `.realm` file. 

[![](https://substack-post-media.s3.amazonaws.com/public/images/f95295b1-9489-4f4e-b908-feabd6694aed_2064x1096.png)](https://substackcdn.com/image/fetch/$s_!TWWK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff95295b1-9489-4f4e-b908-feabd6694aed_2064x1096.png)

I found [realm-studio](https://docs.realm.io/sync/realm-studio) to explore and understand what kind of data exists in the underlying database and it looked promising!

[![](https://substack-post-media.s3.amazonaws.com/public/images/7457b816-c066-47f1-b478-caebd82c03ad_2930x1292.png)](https://substackcdn.com/image/fetch/$s_!Ix0y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7457b816-c066-47f1-b478-caebd82c03ad_2930x1292.png)

Unfortunately, this tool did not let me export blobs…

Once again, I asked ChatGPT what I should do with it. It gave me some ideas but I had to resolve to some good ol’ Googling and hit a few dead ends:

  * I tried to a [realm-to-csv exporter](https://github.com/aromajoin/realm-to-csv) but that didn’t really work

  * Apparently [Realm’s official GitHub](https://github.com/realm/) has SDKs in swift, kotlin, Java, JS, .NET, Dart and anything else you want but not Python (my preferred language for scripting)

  * I used [realm-studio](https://docs.realm.io/sync/realm-studio) what kind of data even exists in the underlying database

  * 


<https://apps.apple.com/us/app/realm-browser/id1007457278?mt=12>

[git@github.com](mailto:git@github.com):realm/realm-cocoa-converter.git

  1.   2. I lost the encryption password. Luckily saved an unencrypted version

  3. The browser (<https://docs.realm.io/sync/realm-studio>) can export to CSV but doesn’t export blobs

  4. I had to quickly learn to configure a swift project. <https://www.mongodb.com/docs/realm/sdk/swift/install/>




https://stackoverflow.com/questions/24026308/accessing-swift-extension-from-objective-c

File is on dropbox

Python can’t open a .realm file directly

But wait there’s more! That was about 700 photos There were 800 more photos when I transitioned from an app called “progress” to an the “body tracker app”.

I forgot my encryption password, but when I was upgrading my phone, I accidently saved an unecnrypoted version. WOW!

TUrns out it used REALM. There’s no python SDK. I had to learn to write swift. Thank you chatGPT!

https://www.notion.so/olshansky/Blog-Extracting-My-Data-38383678a86b4a4399f2768a15a59613?pvs=4

## Body Tracker Application - Getting my photos

With a Sunday afternoon set aside, and frustration pent up, I was ready to get going. I made some coffee, connected my iPhone to my Mac, booted up ChatGPT and got going. I had no clue where to start so I asked a very general question and got the answer I needed.

[![](https://substack-post-media.s3.amazonaws.com/public/images/a7f23f2d-51d9-4607-93a0-feaf8692d5fe_622x1125.png)](https://substackcdn.com/image/fetch/$s_!paCl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7f23f2d-51d9-4607-93a0-feaf8692d5fe_622x1125.png)Asking ChatGPT “how do I get data from an app on my phone?”

I downloaded [iExplorer](https://macroplant.com/iexplorer) and started looking around until I found a _**suspicious 2GB .sqlite**_ file.

[![](https://substack-post-media.s3.amazonaws.com/public/images/45bcb823-9b3a-4190-91b7-c7169831a809_1283x1140.png)](https://substackcdn.com/image/fetch/$s_!I0XJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45bcb823-9b3a-4190-91b7-c7169831a809_1283x1140.png)Exploring a recent backup of my iPhone 13 using iExplorer.

Since it’s been a while since I’ve had to explore new sqlite files, I would’ve asked ChatGPT to give me a list of 10 common commands I need to get a feel for a sqlite schema. However, as someone who’s been subscribed to [Simon Willison](https://simonwillison.net/)’s blog for years, I finally had a reason to try out one of his flagship product: [datasette.io/desktop](https://datasette.io/desktop).

[![](https://substack-post-media.s3.amazonaws.com/public/images/26b2fbef-60f2-4bff-b0b4-acab73be5156_3000x3000.jpeg)](https://substackcdn.com/image/fetch/$s_!ezRD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26b2fbef-60f2-4bff-b0b4-acab73be5156_3000x3000.jpeg)Using Datasette to explore a .sqlite file

Clicking around and exploring the data using Datasette felt pretty intuitive so I don’t have much to say here. When I came across the Binary files in the ZDATA column, my 🕷️ senses started tingling. 

I clicked around and exploreAfter opening the database, it was a simple and visual way to understand what it contains.

I think it’s pretty clear where my data is:

I downloaded one of the files, asked ChatGPT to write me a python script to convert blobs to Python, and it worked flawlessley.

asdasd

[![](https://substack-post-media.s3.amazonaws.com/public/images/c4f4f63d-b370-4e0e-a3d6-b23e15cdbef7_636x322.png)](https://substackcdn.com/image/fetch/$s_!bMK6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4f4f63d-b370-4e0e-a3d6-b23e15cdbef7_636x322.png)

This was a quick & easy way to validate what I was working with, so it was time to automate!

Python Script

# What I have done this without ChatGPT?

  * Makes me more ambitious

  * Would have taken much longer otherwise

  * Mention Simon Willison: https://simonwillison.net/2023/Mar/27/ai-enhanced-development/

  * Link to my #ChatGPtip blog




https://simonwillison.net/2023/Mar/27/ai-enhanced-development/

Could I have done this without Datasette and ChatGPT? Yes.

Did these tools make it more fun, easy and quick? Yes

  * I am a human agent

  * Instructed GPT to help get my data

  * Make sure I quote Simon about being more ambitious

  * I would not have done this if it weren’t for ChatGPT.

  * Backup iPhone

  * iExplorer - https://macroplant.com/iexplorer

  * Copy Paste the DB

  * DataSette Explore - 

  * ChatGPT

  * Python Script

  * Export

  * Upload to google photos




* * *

I spent this whole blog post talking about photos, so you might wonder why I didn’t include them. Some of them are NSFW, so a bit of editing is required. After that, I promise I’ll do a really cool time lapse and post it on TikTok or something.

If there was ever a reason to subscribe, I hope that’s enough.

# Epilogue

  * ChatGPT → LLM (Claude)

  * Chat Interface → Voice

  * o4 model

  * Since then, one could say that everything has changed yet nothing has changed in the world of LLMs.

Light LLM wrappers have gone out of fashion, but agentic use-cases are coming in. The major foundation model builders are coming out with new tools, like Anthropic’s Artifacts & Computer Use. GPT4 level models have made incremental improvements, but we are yet to see any , but haven’t seen any step functions yet. Chain-of-Thought workflows have com.



