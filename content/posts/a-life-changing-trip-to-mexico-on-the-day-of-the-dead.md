+++
author = "Daniel Olshansky"
title = "A life-changing trip to Mexico on the Day of the Dead"
date = "2021-11-29T16:04:52.834Z"
description = "My personal journey into joining the Crypto space full-time at Pocket"
tags = [
    "crypto", "ai", "startup", "tech", "research", "investment"
]
substack_url = "https://olshansky.substack.com/p/a-life-changing-trip-to-mexico-on"
+++

**Tl;dr** I am incredibly excited to announce that I'm joining [pokt.network](https://pokt.network/) today as a full-time Protocol Specialist! This post documents my realization of how I want to devote my time to shape and build out the future of Web3.

#### A bit of background
Without diving into my life-long story, I spent most of my adolescence growing up in Toronto. I love the city and where it's headed, but I'll save that discussion for another post.

I studied Electrical and Computer Engineering at the University of Toronto but mainly concentrated on various pillars of Software Engineering in my senior years. One of my most memorable courses was [ECE419](https://www.ece.utoronto.ca/wp-content/uploads/2019/05/syllabus419.pdf) (Distributed Systems), taught by [Professor Amza](https://www.eecg.utoronto.ca/~amza/). I enjoyed the course so much that I did my undergraduate thesis aiming to optimize fMRI analysis through distributed computing under her supervision. This was back in the days when Hadoop and MapReduce were all the rage.

#### Catching the crypto bug
Like many others, I heard about Bitcoin when Silk Road was on the front page of every news publication. But, other than discussing Bitcoin's price fluctuation and how it enables black markets, I never dove too deep into the technology behind it.

I joined Twitter in 2014 as a new grad and quickly realized how little I knew about financial markets and economics. I remember asking [@krupenin](https://twitter.com/krupenin) to explain what the S&P 500 is. After that, I started learning about 401Ks, IRAs, hedge funds, mutual funds, Robo-advisors, value investing, momentum investing, and so much more. I spent the better part of the following year listening to [The Investor's Podcast](https://www.theinvestorspodcast.com/) and reading any book they recommend on investing (see my [GoodReads](https://www.goodreads.com/user/show/19157738-daniel-olshansky)) until they all started sounding repetitive. This learning process also exposed me to various schools of economic thought.

In 2015, while working at Twitter, I remember [@fredwilson](https://twitter.com/fredwilson) writing about Ethereum in one of his newsletters. That weekend I decided to listen to a random interview with [@VitalikButerin](https://twitter.com/VitalikButerin) I found on YouTube while cleaning my room. When the interview was done, I remember being confused by what the platform offered but was intrigued by the fact that there seemed to be an interesting distributed system problem at its root, which somehow related to economics. In addition, I was drawn by Vitalik's mannerism and clear explanation of technical concepts and impressed by his writing style, thinking outside the box, and natural ability to lead a decentralized organization when a playbook did not exist, all at a very young age. This was a significant factor that drew me into Ethereum in the first place.

I can't say I was hooked since day one. Still, I started to slowly join the crypto community by reading online resources available at the time, following others in the crypto space on Twitter, and joining one of the Ethereum Gitter channels. I remember fanboying pretty hard when Vitalik was online answering some of my n00b questions at the time or just excited to meet like-minded people on Twitter, such as [@o_rourke](https://twitter.com/o_rourke).

Twitter was a great place to work, and I'm very thankful for all the mentorship I had there as a Junior Engineer. However, crypto was just a hobby, and I was very excited about the potential of Computer Vision and Augmented Reality. I did my GREs thinking I'd go to grad school for Computer Vision but ended up finding the opportunity to join an AR startup instead. In the summer of 2016, I moved to Florida and joined Magic Leap as a Cloud API Engineer to build out their then non-existent cloud infrastructure.

Having moved to a new state where I didn't know anyone, I had more time for hobbies and interests. So, naturally, I caught the crypto bug.

#### Crypto at Magic Leap
Magic Leap was a rollercoaster in more ways than one, but it is where I consider myself to have matured from a Junior to a Senior Engineer. I learned how to build, design, lead, collaborate, present, evaluate tradeoffs, and so much more. But, again, I'll leave the full details of my experience there for another post.

With the need to process a lot of streaming image data, most employees had both a MacBook and a pretty beefy workstation to offload heavy lifting for local development. One of my immediate questions was why these NVIDIA graphics cards were sitting idle at night when they could be mining Ethereum. 😅

I spent a couple of nights setting up my workstation to mine Ethereum and was excited to see the ETH slowly starting to trickle in. Unfortunately, three days later, the IT department showed up at my desk in the middle of the day, unplugged the machine and took it away without saying a word. Our team was situated in the dead center of an open office space and everyone, including my manager, was very confused. I tried to play it cool, but was also mentally preparing to get fired in the near future…

Luckily, Magic Leap's Chief Software Architect at the time, [@yeraze](https://twitter.com/yeraze), was also dabbling in the crypto space. After a meeting with him, my manager and HR, where I signed a document promising not to do this again, I got involved in ideating how Magic Leap could help users protect their data using distributed ledger technology. We started building a prototype, but it was ultimately a project that couldn't be staffed, and all we had to show for it was a [patent](https://worldwide.espacenet.com/patent/search/family/074230813/publication/WO2021021942A1?q=pn%3DWO2021021942A1).

***Fun fact**: I later learnt that my workstation was taken offline because it was causing internal networking issues.*

#### Pocket Genesis
I continued to entrench myself in the online crypto community, studied all the projects appearing right as the ICO craze started, and published a few short posts on [medium](https://olshansky.medium.com/). Most notably, The Investor's Podcast featured one of my articles on [Bitcoin vs Ethereum](https://www.theinvestorspodcast.com/blog/bitcoin-vs-ethereum/) and [@TIPMayerMultple](https://twitter.com/TIPMayerMultple) continues to run on one of Heroku's free dynos.

In parallel to all of this, I was having a blockchain-related discussion with [Michael O'Rourke](https://twitter.com/o_rourke) on Twitter. We realized that we're both located in Florida, and he was planning on visiting South Florida soon. So the two of us met up a few times just as he was getting into programming, talked about life, work, and of course, how *Bitcoin is king and how Ethereum is going to change the world*.

This was the time when other [Infura](https://infura.io/) started gaining a lot of usage, and other blockchains such as [Cardano](https://cardano.org/) and [EOS](https://eos.io/) started popping up. Mike and a few of his friends had the early realization that we're heading into a multi-chain world and that there will need to be some sort of distributed node infrastructure to support it in the future. This is how [Pocket](https://www.pokt.network/) came to be.

At the time, I was working on an extremely interesting project at Magic Leap related to building the cloud infrastructure needed to [persist virtual content](https://developer.magicleap.com/en-us/learn/guides/persistent-coordinate-frames) and enable [shared experiences](https://developer.magicleap.com/en-us/learn/guides/shared-world-faq). However, when Mike asked me to look over a few of their early design documents and jump on a couple of calls with [@luyzdeleon](https://twitter.com/luyzdeleon), Pocket's CTO at the time, I couldn't say no. Overall, the designs were solid, and all the ideas were very novel, but what's more incredible is seeing how far the project has come over the last few years.

#### Taking a step back
Once the ICO craze cooled down and crypto winter finally came, my involvement in the space slowed down. I remember going to a couple of conferences in Miami and only meeting people in suits looking to launch the next ICO and make the next million (billion?). Overall, I was a bit disenchanted that those excited about the mission of Web3 were being outnumbered by those looking to make a quick buck.

Raising money in the crypto industry around this time became much harder, but in retrospect, this is when everyone went heads down and got serious about building. As a result, most of the infrastructure and projects gaining traction today were built during the crypto winter when there were no mainstream distractions.

At the same time, I, unfortunately, hit a few emotionally draining health issues (a herniated disc, torn meniscus, unexplained vertigo…) and burnt out at Magic Leap for various reasons, including self-imposed 80 hour work weeks…

In January of 2020, after 3.5 years in the Augmented Reality space, I decided to move back to California and see what exciting things are happening in the Autonomous Vehicle space with an offer from Waymo!

#### Life at Waymo
I joined the Planner Evaluation team at Waymo just a few months before shelter-in-place was enforced in the US and have been there for nearly the past two years. The team was new and has almost tripled in size since I started. I had the luxury of getting to know my team in person while enjoying all the perks of the Google X office. If you don't know, it was originally a mall that was retrofitted into an office and is probably one of the coolest offices I've ever been to with large ceilings and open spaces everywhere you go. I also got to see Sergei Brin a handful of times since it seems to be where he spent most of his time before retiring from Google.

Waymo is a great place to work. It has a large team of intelligent and humble individuals that are always supportive of each other. The company is tackling a very challenging problem while taking care of its employees, providing all the resources necessary, prioritizes work-life balance and is very bottom-up engineering-driven. The last point was a nice change, given that Magic Leap was a much more top-down product-driven organization.

My most significant takeaway from building ML infrastructure at both Waymo and Magic Leap is that MLOps will have a much more substantial impact on the adoption of ML in mainstream society. 2012 saw a significant step function in the academic space, and I'm sure we'll see another such step function in the coming decade, but there is a lot more low-hanging fruit in the Machine Learning Ops/Infrastructure space today. One project in the space that I'm particularly excited about is [Netflix's Metaflow](https://metaflow.org/).

However, with all of that being said, something was missing… I wanted to be more excited and passionate about my work on a day-to-day basis. I wanted to have more impact on the organization's success as a whole. I wanted to move the needle and shape the future. I was looking for something but wasn't sure what. ***Spoiler**: it was a small and passionate team with a thriving and supportive community in the Crypto space.*

I was debating whether I should join a startup or do my own, so I started some casual *"startup dating"* to see what kind of opportunities were out there and heavily considered joining one in particular.

#### A life-changing trip to Mexico on the Day of the Dead
Even after leaving Florida, Mike and I kept in touch and would jump on a call once every few months. I would see how Pocket would grow & develop from afar but was not an active community member.

In August, he invited me to join his team's offsite in Mexico, planned for October. I was a bit hesitant because I already had other vacation trips planned, and there was a lot of work to do at Waymo, but the latter point is moot because it'll always be the case. I was contemplating as to whether I should go and ended up booking my ticket 3 days before the offsite began. You can get a small glimpse of what happened at the offsite in the following thread:

@POKTnetwork fam was last week?🧵\n\nWe were busy planning our next big moves at our yearly offsite👀\n\nThis year it was in a gorgeous hacienda in Malinalco, then spent a few days at a hotel in the heart of Mexico City - just in time for día de los muertos! ","username":"POKTnetwork","name":"Pocket Network | Is Hiring 👀🚀","date":"Wed Nov 10 17:23:33 +0000 2021","photos":[{"img_url":"https://pbs.substack.com/media/FD2UyvlXsA060v6.jpg","link_url":"https://t.co/ksw9ppnNHe","alt_text":null},{"img_url":"https://pbs.substack.com/media/FD2Uyv9XsAcObL_.jpg","link_url":"https://t.co/ksw9ppnNHe","alt_text":null}],"quoted_tweet":{},"retweet_count":9,"like_count":73,"expanded_url":{},"video_url":null,"belowTheFold":true}">Pocket Network | Is Hiring 👀🚀 @POKTnetworkHola! Wondering where the @POKTnetwork fam was last week?🧵

We were busy planning our next big moves at our yearly offsite👀

This year it was in a gorgeous hacienda in Malinalco, then spent a few days at a hotel in the heart of Mexico City - just in time for día de los muertos! [5:23 PM ∙ Nov 10, 2021
---
73Likes9Retweets](https://twitter.com/POKTnetwork/status/1458485493226741768)

**Going on this trip was one of the best decisions I ever made.**

The Pocket team takes the mantra of "*work hard, play hard"* very seriously. The days were spent with content-dense presentations and stimulating discussions. The breaks were a mix of thought-provoking conversations, sports and other fun activities. I'll leave the nights up to the imagination of the reader.

The overall atmosphere of the event is difficult to put into words. Every day was new, challenging, interesting, exciting, fun and refreshing. Time-over-time, I was impressed by the quality and pedigree of all the presentations. The level of innovation and expertise that every member brought to the table contests some of the most impressive workshops and presentations I experienced throughout most of my academic and professional career. More importantly, they led to very conducive, sometimes heated, but invigorating discussions.

There were presentations about everything one could ask for, including: growth channels, user experience, protocol development, best engineering practices, token economics, decentralized governance, etc. I would re-attend each and everyone again.

I got to see the speed and intensity at which the team operates and how passionate and driven everyone is to achieve the same goal. It is incredible to see how quickly the community is growing, how much traction they're gaining, and how much they have achieved with the resources they had. Everyone on the team is equally passionate and excited about the mission. Everyone is fueled and driven by the same goal. In a way, you could say they're all part of the same Pocket. *I know this last analogy doesn't really make sense, but I couldn't resist.*

With every additional day I spent in Mexico, I kept thinking that I didn't want it to end. Finally, a few days after returning, I spoke to my manager about wrapping up my work and leaving Waymo. I wasn't sure what I would do, but I knew I needed to be in the crypto space full-time. I found the 🔥🔥🔥 I was looking for, and it's all I could think about. I didn't know if I'd be joining Pocket, doing my own startup in the crypto space, sitting at home and reading white papers, running nodes, or sifting through various discord servers. All I knew was that this was how I needed and wanted to spend my time.

*Quick side note: We also ran into Robert Downey Jr. on the street, which I documented in this [Twitter thread](https://twitter.com/olshansky/status/1455053861547175940).*

#### Why Crypto? Why Pocket?
I won't do these questions justice in a couple of paragraphs, so I'll discuss them in another post that expands on this thesis:

**Crypto is the most effective path forward to achieve democratic capitalism, and Pocket is the foundational layer of decentralized infrastructure that'll enable all of it it.**

If you're curious to learn more, this [recent blog post](https://medium.com/wall-street-ninja/pocket-network-decentralized-relays-989826efdc1) and [primer](https://invest.robotcache.com/blog/crypto/pocket-network-primer) are good starting points to learn more about what the Pocket network does. In short, it is a decentralized relay network that creates financial incentivize for full node runners, eliminating the need for centralized node infrastructure, which most DApp developers today use to bootstrap their application development.

According to [POKTscan](https://poktscan.com/public/dashboard), they're averaging around 100MM relays per day, supporting a growing list of more than a dozen public blockchains, and dozens of new Pocket node runners are coming online every day. The best part is that this is just the beginning!

There are still a lot of crypto skeptics out there, and it's hard to argue that there's no bubble at the moment, but there is no question in my mind that that this is going to be part of everyone's every day, like internet protocols, smartphones, databases, etc.… So whether you're into DeFi, economics, games, art, collectibles, governance, law, engineering, there is something in the space for everyone.

#### Finality
With Thanksgiving weekend having just come to an end, I am very thankful that Pocket extended me the opportunity to join their team full-time and build out the future of Web3!

If you haven't heard of them yet, I promise you that you will in the next couple of years. I cannot recall the last time I was this excited about the next step in my career.

Lastly, if you made it this far, you should join Pocket's [Discord channel](https://discord.com/invite/uCZZkHTQjV) and be part of the community. You won't regret it!