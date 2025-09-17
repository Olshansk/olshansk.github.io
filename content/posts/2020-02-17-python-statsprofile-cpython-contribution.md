---
title: "Python 3.9 StatsProfile — My first OSS Contribution to cPython"
date: 2020-02-17T19:31:48.783Z
draft: false
description: "You can try out all of the code in this article yourself using this Google Colaboratory notebook."
medium_url: "https://medium.com/@olshansky/python-3-9-statsprofile-my-first-oss-contribution-to-cpython-9dd6847eb802"
tags:
  ["python", "cpython", "opensource", "profiling", "performance", "programming"]
---

_You can try out all of the code in this article yourself using [this Google Colaboratory notebook](https://colab.research.google.com/drive/1GBxS6UnJOLyztivEheHBEDOHFFqpRG2y#scrollTo=Vmky1qQQzvVt)._

If you've ever tried to debug and optimize your python application, it's likely that you stumbled upon [Python Profiles](https://docs.python.org/3/library/profile.html#) to understand where most of the execution time is being spent. You enable the profiler at the beginning of a code segment you're interested in profiling with `pr.enable()`, and call `pr.create_stats()` at the end.

[View code on GitHub Gist](https://gist.github.com/olshansky/9e693eaaca3153a8ff9a2584629388f9)

Afterwards, you can create a [Stats](https://docs.python.org/3/library/profile.html#the-stats-class) object, and print the results in a human readable format with `ps.print_stats()`.

![Python profile stats output](/images/posts/2020-02-17-python-statsprofile-cpython-contribution-image-01.png)

The output above is quite useful and can take you a long way. However, what if you don't know what kind of data inputs cause a bottleneck in your application? What if you're interested in aggregating and evaluating profiling data over some period of time? What if you want to profile your application while your team is dogfooding it? I found that there isn't an easy way to use this data in an ETL pipeline where you'd be able to do further offline analysis over a larger dataset.

I recently made my first [open source cPython contribution](https://github.com/python/cpython/pull/15495) which adds a [dataclass](https://docs.python.org/3/library/dataclasses.html) called `StatsProfile` to address this. After you created your stats object, you can retrieve all the information in the above screenshot by calling `ps.get_stats_profile()` and analyze it in a programmatic way.

If you're not on Python3.9 yet, the following code snippet is a slightly modified version of the code in the pull request that you can start using today by importing it directly into your project.

[View code on GitHub Gist](https://gist.github.com/olshansky/31266d61542bbcddb3f57ae684ca0917)

Now, rather than inspecting the profile of a single execution of our code snippet, we can aggregate and analyze the profiles over several different iterations. In a real production service, depending on which logging tool you use, you would likely need to format and stringify the `StatsProfile` dataclass before logging it, but for the purposes of this example, everything is stored in memory.

To simulate timestamped logging, `(timestamp, stats_profile)` tuples are appended to a `timestamped_stats_profile` list with every execution of the loop.

[View code on GitHub Gist](https://gist.github.com/olshansky/867a1ec17e3cc470d051c41d62c94896)

After the data is logged, it needs to be aggregated over a certain timeslice. Most logging/visualization platforms have their functions to process timeseries data, so this would be platform specific. Sumologic has the [timeslice](https://help.sumologic.com/05Search/Search-Query-Language/Search-Operators/timeslice) function, Elasticsearch has examples of how to do [date histogram aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-datehistogram-aggregation.html), Datadog has an [aggregate across time dropdown](https://www.datadoghq.com/blog/summary-graphs-metric-graphs-101/#distributions), etc...

For the purposes of this example, I'm doing the aggregation manually in python. I bucket all the logged (i.e. saved) `StatsProfile` objects over 10 second intervals, aggregate the cumulative execution time, `cumtime`, per function call and store the resultant counters in `time_slices_counters`. If you're interested in inspecting the number of calls to certain functions rather than the cumulative execution time spent in it, you would simply modify the parameter being access on `line 21` in the code snippet below.

[View code on GitHub Gist](https://gist.github.com/olshansky/f34671bf3cb569796acff30bfb4ea178)

In my opinion, a stacked bar graph is a great way to visualize and easily interpret this data. Using the following code snippet:

[View code on GitHub Gist](https://gist.github.com/olshansky/39d51402401ce69262acafd0b824279e)

We can generate a graph that looks like this:

![Stacked bar chart showing Python profile data over time](/images/posts/2020-02-17-python-statsprofile-cpython-contribution-image-02.png)

The results aren't very interesting or surprising given the simplicity of a script calling `sleep` a bunch of times, but hopefully it'll be more useful in more complex applications.

It's important to note that you probably should not be doing this in production. It could be useful on your local or development environments, and might be worth enabling in a single canary, but could have adverse effects in prod. You would be polluting your logs with large `StatsProfile` structures, and I have not investigated if running `cProfile` in prod could potentially downgrade your service's performance.

As a side note, though there is some overhead and a small learning curve, I was very pleased with how easy it is to contribute to cPython. Aside from publishing the [actual PR](https://github.com/python/cpython/pull/15495), you have to sign the [PSF Contributor Agreement](https://www.python.org/psf/contrib/contrib-form/), open a on [bugs.python.org](https://bugs.python.org/issue37958), and nudge a few people to make get your code looked at. There is a great [developer guide](https://devguide.python.org/) on how to run things locally and execute tests. I recently also came by [this doc](https://paper.dropbox.com/doc/JlgnduI6kw9MJIaGPpN9G), which is a good starting point if you've never contributed to cPython before.

Huge thanks Gregory P. Smith for reviewing and approving my cPython PR! Also, thank you to Сергей Яркин for proofreading my article, and a special shoutout to Manuel Dell'Elce who built a really nice [chrome extension](https://chrome.google.com/webstore/detail/code-medium/dganoageikmadjocbmklfgaejpkdigbe/related) that made [embedding code snippets](https://medium.com/@Maluen0/how-to-add-code-highlighting-in-medium-articles-without-leaving-the-editor-8f24f5a88d28) in this medium article a breeze.
