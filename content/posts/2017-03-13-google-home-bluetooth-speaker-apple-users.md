---
title: "Google Home As A Bluetooth Speaker for Apple Users"
date: 2017-03-13T05:11:44.831Z
draft: false
description: "One of the biggest disappoints I experienced after purchasing my Google Home is discovering that it cannot function as a Bluetooth speaker…"
medium_url: "https://medium.com/@olshansky/google-home-as-a-bluetooth-speaker-for-apple-users-e7f9b9881daf"
tags: ["google-home", "apple", "bluetooth", "technology", "airplay"]
---

One of the biggest disappoints I experienced after purchasing my Google Home is discovering that it cannot function as a Bluetooth speaker. As a Mac & iPhone user, most of my use cases were pretty well supported. I could talk to Google Home to play the news, podcasts or music. I could also manually cast a Chrome tab or use an application such as Spotify that has native Google Cast support. There were a couple use cases though where the Google Home and iPhone didn't play so well.

My preferred apps for consuming audio content while I'm driving is [Bookmobile](https://itunes.apple.com/us/app/bookmobile-audiobook-and-podcast-player/id416457527?mt=8) for audiobooks and Apple's [Podcast](https://itunes.apple.com/us/app/podcasts/id525463029?mt=8) app for podcasts. Both of these applications have direct support for AirPlay and implicit support for Bluetooth since it's natively supported by iOS. However, neither of these applications supports Google Cast. I contacted the creator of Bookmobile who said there are no plans to add it in the near future, and don't think it's on Apple's roadmap either. I tried using TuneIn for podcasting since it has Google Cast support (shoutout to my good friend [Davy Li](https://twitter.com/davyli) who implemented this feature), but have grown too accustomed to the default Podcast app and didn't really want to switch.

I discovered that there is a straightforward workaround to this problem that involves the use of two Mac applications: [AirServer](https://www.airserver.com/Download) and [mkchromecast](http://mkchromecast.com/). AirServer turns my Mac into an AirPlay ready receiver, and mkchromecast turns it into a Google Cast transmitter. When I use either Bookmobile or Podcast, the audio stream is transferred from my iPhone to my Mac over AirPlay, and from my Mac to my Google Home over Google Cast. Given that I use both of these apps very heavily in my car over Bluetooth, I can pick up exactly where I left of when I leave my car and enter my home.

Though I hope that Google will make the Google Home have Bluetooth support at some point in the future, I realize that it's unlikely. If Bluetooth is an important feature for you, this might be one reason to go with the Echo instead of the Home.