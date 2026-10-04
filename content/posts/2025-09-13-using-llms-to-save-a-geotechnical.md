---
title: "Using llms to save a geotechnical"
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

 _tl;dr I used ChatGPT & Claude to create a script that moves PDFs around, saved my dad months of tedious work, and it made me reflect on what dev shops might look like in the future._

Есть какие-то фолдеры, в которых я знаю, что мы никогда из них файлы не брали. Это значит, что они не прошли процесс Google Earth Software. Я знаю, что я вижу по названиям и по размеру, что эти файлы уже на Google Earth. Поэтому я хочу просто, и поэтому вот это Sources. Те, которые Compere, это там, где уже файлы processed through Google Earth Software. Вот разница между Sources и Compere Folders. Скрипт не работал. Все, давай, пока.

# Spending time at home

Hopefully the tacky title caught you’re attention, but I can assure you that it’s not an exaggeration.

My [dad](https://www.linkedin.com/in/dmitry-olshansky-m-sc-m-eng-p-eng-54285048/?originalSubdomain=ca) is a Senior Geotechnical Engineer for the [Toronto Transmit Commission](https://www.ttc.ca/). Every time I visit my parents, Saturday morning brunch usually starts with _“can you write a program for me that does…”_  
  
On the surface, the ask always trivial enough that a high-school programming student could do it. In practice, you’d need to consider all of these:

  * What is the full scope of requirements? _There’s no PM here…_

  * How many edge cases does this proprietary data have? _Sifting through civil engineering data is painfull…_

  * What kind of UX (User Experience) do I need for an a non tech-savvy individual to use? _This is an industry that’s very averse to trying new software…_

  * How do I make it run on Windows and account for any firewall or permission issues their IT team put in place?_😮‍💨_




I’ve learned the painful lesson of not even trying unless it’s how I want to dedicate my entire weekend to it. Once you’ve built a few things, you know that this is the reality that lies beneath the surface:

[![](https://substack-post-media.s3.amazonaws.com/public/images/3140acd0-9627-4f7e-9e23-c637adb65244_1200x419.jpeg)](https://substackcdn.com/image/fetch/$s_!h70a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3140acd0-9627-4f7e-9e23-c637adb65244_1200x419.jpeg)

# Taking on The Project

Prior to AI-enhanced development, I wouldn’t even consider it. However, because we live in a different world now, I thought I’d give it a shot. As  said in [one of his blogs](https://simonwillison.net/2023/Mar/27/ai-enhanced-development/) last year:

> The thing I’m most excited about in our weird new AI-enhanced reality is the way it allows me to **be more** _**ambitious**_ with my projects.

More importantly, I’m really curious how close we are to having individuals who don’t know any software engineering being able to write _SoloWare_ for themselves.

Darmesh, CTO of HubSpot, [defines one of the use-cases for SoloWare](https://www.linkedin.com/posts/dharmesh_for-3-decades-now-in-addition-to-my-day-activity-7166500611247583232-kZgb/) as:

> There's something I want software to do for me -- and what I specifically need doesn't seem to exist (or I couldn't find it).
> 
> …
> 
> And most importantly, you don't have to worry about shutting it down if it's no longer serving a useful purpose.

# Kicking Things Off

The goal of what we’re trying to do is to identify unique files in **compare_dir** :

  1. Compare all PDF files in the **src_dir** against those in the **compare_dir** accounting for any nested directories that may exist

  2. If there is a **> 90% overlap in file names** AND < **2% difference in file size** , we’ve got a match!

     1. **compare_dir** has lots of duplicates from years (decades?) of copying, sharing, duplicating, renaming and mismanaging files

  3. Create a **dst_dir** asd that contains 




I asked my dad to put together a proper set of requirements.
    
    
    - Check the names of the PDF files in the source folder.
    
    - Compare those names to the PDF file names in the other folder (which contains subfolders).
    
    - If a PDF file from the source folder matches a PDF file in the other folder (same name or at least 90% of the name), the script should then compare the number of pages in both files.
    
    - If both the file name and the number of pages are the same, the script should move the PDF from the source folder to a new folder (I will provide the path to this folder).
    
    - At the same time, the script should create a Word document. This document will list:
    
    - The name of the source PDF file.
    
    - The path to the matching PDF file from the other folder.
    
    - I need just one Word file where all the matching file names and paths will be added.

# Attempt #1 - ChatGPT & Python

I cleaned it up into something more ChatGPT appropriate and got a Python script working fairly quickly. You can find the conversation [here](https://chatgpt.com/share/670dc66e-9a30-8002-8972-ad24400f2fb1). All you have have to do is run:
    
    
    python main.py src_folder compare_folder dest_folder

 _Easy, right? Not quite…_

I don’t want to go through the process of installing python on my dad’s windows machine and teaching him how to use a shell. I’m also not sure if this is something he’d be able to do at work either.

I asked ChatGPT to build a Windows GUI for me and bundle it into one `_.exe_ `. This was pretty easy, but all of my attempts a using [WineHQ](https://www.winehq.org/) (a Windows emulator on macOS) to run it resulted in “ __tkinter”_ dependency issue.

[![](https://substack-post-media.s3.amazonaws.com/public/images/5e9b7c60-99b8-4f82-937f-c6e3709f66c5_2254x1470.png)](https://substackcdn.com/image/fetch/$s_!GtLg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e9b7c60-99b8-4f82-937f-c6e3709f66c5_2254x1470.png)

I’m sure I could figure it out, but after ~40 minutes of wasted time on dependency management, I decided to try something different.

# Attempt #2 - Claude Artifacts & HTML

I’ve been seeing lots of use-cases for Claude Artifacts, and thought that a publically accessible web app would be perfect for this.

I started a [chat with Claude](https://claude.ai/chat/dbcbd52d-0cf0-4631-9c37-4e92efdd4b0e), published the [artifact online](https://claude.site/artifacts/a7db83af-bc4b-445d-8d57-0f0b930433c2), and hit an error related to Sandboxing:

[![](https://substack-post-media.s3.amazonaws.com/public/images/1a029a52-22e2-4edb-81e3-9541f459d875_2322x1958.png)](https://substackcdn.com/image/fetch/$s_!kKT5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a029a52-22e2-4edb-81e3-9541f459d875_2322x1958.png)

Having recently read [How Anthropic build Artifacts](https://newsletter.pragmaticengineer.com/p/how-anthropic-built-artifacts) by , I figured that artifacts is not mature enough to manipulate around permissions and sandboxing issues, so I immediately decided not to go down this path.

I could, and I might have solved it, but I had a better, faster and simpler idea just to get it working: **local HTML**. 

# Attempt #3 - Local HTML

Rather than deploying the HTML somewhere, I figured my dad could just open the `.html` file in his browser and have access to the full filesystem. We don’t have to deal with any server communication, firewall permissions, filesystem issues, and we don’t require any executables.

It’s as simpler as it gets from a UX and “deployment” perspective.

I took the HTML app from Claude and went back to ChatGPT 4o, irritated on [a few small things](https://chatgpt.com/share/671e75d3-33e8-8002-92a7-1e08d7458424), and bam:

[![](https://substack-post-media.s3.amazonaws.com/public/images/fd3db8e9-1b9a-4d5c-a902-a8fa453eed3d_1976x1458.png)](https://substackcdn.com/image/fetch/$s_!SHxB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd3db8e9-1b9a-4d5c-a902-a8fa453eed3d_1976x1458.png)

# Result

My dad had to do this for thousands of 

All the code is publicly accessible [here](https://github.com/Olshansk/ttc_move_pdfs).

# Reflections

If you’re not a software engineer, I think it’s impossible for you to built it today. 

Assuming you’re good at outlining the requirements and iterating with an LLM of your choice, this particular use-case still required specific experience and intuition as to when and how to change course.

# Rough Notes && The future of Dev Shops

  * The future of tech is deployed engineers

  * Get answers from them

    * 1\. Can you send me a message explaining how you got this weird source and compare folders in the first place?

    * 2\. Let me know how the script goes today (we will likely need to iterate on it a few times). I’ll use it for my blog

  * Make the requirements simple and digestible for the reader

  * What, how why




FDE Learnings:

  * From reflections on Palantir: FDEs tend to write code that gets the job done fast, which usually means – politely – technical debt and hacky workarounds

  * I wanted to hack it together

  * After 5 iterations or so, I realize we need a unit test and some simulation.




Talk about how these people won’t become engineers and that I don’t think LOM’s will be good enough to support them. The difference is that instead of having a team of software engineers internally you would only have one or two. So rather than seeing Software go away I think we’re gonna goin the same way that service has every single company will start having their own internal software engineering team that’s where things are going.

News try to get in front of the CEO see what else we can figure out here and it should be good

We talk about training in how to use LLMs, but I see a bigger opportunity for code camps tagrg Ted at embedded engineers in legacy systemsIt’s no longer about building and selling your service from the outside in, but building it from withinInstead of a dev ship where you outsource, what if it’s a dev ship where you embedYou don’t need seniorsJust ciders

Embedded engineers that go in office.

Hubs all around the world.

They have access to a share software team, with internal tools.

It’s similar to the description of Forward Deployed engineers at Palantir, recently covered in [Reflections on Palantir be Nabeel](https://nabeelqu.substack.com/p/reflections-on-palantir), but with a much greater, and arguably simpler, scope.

How I save the civil engineer, four months and four hours. Spoiler the engineers, my dad. Every once in a while, my dad asks me to write a script for him, which I can, but we all know that the business logic is a very small piece of a real user experience, especially for those that are less tech savvy.so I tried. And then explain the flow from python script to a Windows executable to a quad artifact hitting issues and needing to build a tuition to get a real functioning product.

And how in civil and construction it’s really really different and the reason attack is behind is partially because of option part.

  * Defining requirements is hard

  * Iterating on requrements is hard

  * Identifying a problem is hard

  * Everything is iterative

    * Sitting, thinking ,writing it hard (see paul graham’s post)

  * Human in the loop

  * Forward developed engineers

    * See reflections on palantir blog post

  * It’s no longer about converting “source code” to “machine code”

  * It’s about converting “an idea” into “language”

    * Transforming ambious needs into a workflow

    * Technical PMs are the future

    * In particular, those that are good at writing




On AI agents

  * https://share.snipd.com/snip/5fbcb36b-7ac9-4df9-bc16-0cc1aa29ef97

  * An agent is gonna be someone who doesn’t background task in long-term the missing link here is the agent prototyping and emulating the software lifecycle talking to the actual engineer so they can give them feedback because it’s actually form of requirements which always needs human. That’s the hardest part.



