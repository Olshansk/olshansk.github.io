---
title: "Bitcoin's price isn't a bubble, it's an adoption curve"
date: 2017-12-27T19:35:51.920Z
draft: false
description: "It's difficult to objectively quantify Bitcoin's adoption rate since there are too many factors to consider. Should it be the number of…"
medium_url: "https://medium.com/@olshansky/bitcoins-price-isn-t-a-bubble-it-s-an-adoption-curve-f52695df2b01"
tags: ["bitcoin", "cryptocurrency", "adoption", "bubble", "analysis", "data"]
---

It's difficult to objectively quantify Bitcoin's adoption rate since there are too many factors to consider. Should it be the number of people holding Bitcoin? Bitcoin's market cap? The number of brokerages with support for Bitcoin futures? The number of businesses accepting it as form of payment? A very different story can be told depending on the angle from which you look at it.

## Bitcoin's market cap

As a potential store of value, Bitcoin's market cap needs to be sufficiently high for institutions and central banks to take it seriously. Governments must add some regulation around it so it has legitimacy, and a large enough portion of the general population must agree that it has inherent value. To agree that it has value, Bitcoin is very dependent on network effects such as those described by [Metcalfe's Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law).

A typical social networking service must simultaneously grow it's user base and provide utility. Once there is a sufficiently large user base and and the utility provided is high enough, it can start deriving value for its shareholders. However, unlike a social network, Bitcoin must grow it's user base and derive value at the same time. Once the user base is sufficiently large and it has enough value, Bitcoin can start providing utility as a store of value.

It's unlikely that a central bank will spend effort looking into a currency with a $1B market cap and several hundred users. No government would spend effort regulating a market that small either. Similarly, very few individuals would consider putting their life savings into a something that is only valued by a couple hundred people. As we've seen, a market cap needs to be in the tens or hundreds of billions for the general public to take notice, and possibly in the trillions to achieve mainstream adoption.

Bitcoin's growing market cap and increasingly diverse set of holders is a self reinforcing cycle that further promotes it's utility. As it's price grows and more people invest, there is an increasing incentive for the general population to accept it as means to store value.

## Adoption rate

With all of that said, it doesn't mean that Bitcoin's market cap should be at $10T tomorrow. It's price and adoption rate should grow at a similar pace, but the recent hype by the media brought on a ton of speculation that pushed its price to ridiculous heights.

I decided to see how Bitcoin's recent price action relates to its adoption rate. Like I mentioned earlier, there is no right way to determine what the adoption rate is, so I chose to use the _number of unique transactions_ and the _number of unique addresses used_ because it was easily accessible via [blockchain.info](https://blockchain.info/).

Below is a graph of the percent change in Bitcoin's price, number of transactions and the number of unique addresses used between any two consecutive days over the past three years. A 25 day moving average was arbitrarily chosen to smooth out the data.

![Bitcoin price and adoption correlation chart](/images/posts/2017-12-27-bitcoin-adoption-curve-not-bubble-image-01.png)

There are few interesting observations from the above chart.

1. While the day-to-day price % change is definitely above the mean, it is relatively reasonable by Bitcoin standards.
2. There have been several points in time in the past when the day-to-day price % change was higher than it is today.
3. In the recent past, the number of unique addresses used and the number of transactions have had a similar growth rate as the price.

Below is another way of looking at the same dataset.

![Complete dataset for the ratios over the past three years.](/images/posts/2017-12-27-bitcoin-adoption-curve-not-bubble-image-02.png)
_Complete dataset for the ratios over the past three years._

![Same data as the graph above, but stretched horizontally and excludes 7 outliers where | % Δ price | is more than 300 and | % Δ trans | is near zero.](/images/posts/2017-12-27-bitcoin-adoption-curve-not-bubble-image-03.png)
_Same data as the graph above, but stretched horizontally and excludes 7 outliers where | % Δ price | is more than 300 and | % Δ trans | is near zero._

Overall, it does look the recent price movement is historically high, but still reasonable relative to it's adoption rate. [1]

## Intrinsic value

Bitcoin's market cap is currently fluctuating around the $250B ± $50B mark. As a speculative asset, the shear numbers involved cause a lot of skepticism, and rightfully so. Bitcoin's fair value could range anywhere from $0 to $1MM USD per coin depending on how you look at it. Justifying any sort of intrinsic value comes down to opinion regarding what the future holds. However, as the market cap grows and more people "jump on the bandwagon", it is increasingly more likely to be adopted by more and more people.

[@olshansky](http://twitter.com/olshansky)

[1] It's reasonable to say that these transactions don't provide real utility because they're the result of short term trading, but I would argue that it's a form of adoption in itself.

[2] _The script used to generated the charts can be found [here](https://gist.github.com/Olshansk/9b0c8e15fdb05ee735b6b547c4add8a6)._
