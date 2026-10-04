---
title: "Use Git LFS on Github Carefully"
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

* * *

### Use Git LFS on Github Carefully

< Insert Screenshot of Git LFS>

[Git Large File System](https://git-lfs.github.com/) is a great solution when you need to store large files (audio files, PDFs, test fixtures, binaries, etc…) as part of your repo. You should probably be using some sort of object storage system when the number of size of the files exceeds some threshold, but it’s a very quick and easy way to get going and can take you far.

I create a new repo called [git-lfs-test](https://github.com/Olshansk/git-lfs-test) and confirmed that my Git LFS usage is currently empty using the instructions provided by [Github](https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage) and visiting the [billing](https://github.com/settings/billing) page.

![](https://cdn-images-1.medium.com/max/800/1*T6o-9DLcv_gz4cCvIGFdWA.png)

I then created a 50Mb file, commit it and pushed it. My usage remained at 0.0GB, so I assumed it was likely because GitHub round 0.05GB down.

Since every account only comes with 1GB of alloted Git LFS storage, you need to be very careful because of how the data is versioned.From the [docs](https://docs.github.com/en/github/managing-large-files/versioning-large-files/about-storage-and-bandwidth-usage):

> If you push a 500 MB file to Git LFS, you’ll use 500 MB of your allotted storage and none of your bandwidth. If you make a 1 byte change and push the file again, you’ll use another 500 MB of storage and no bandwidth, bringing your total usage for these two pushes to 1 GB of storage and zero bandwidth.

Commit and push

  


No changes on the billing page…

git lfs ls-files

Using git lfs for some fixtures I use for testing

[**Viewing your Git Large File Storage usage**  
 _Bandwidth and storage usage only count against the repository owner 's quotas. In forks, bandwidth and storage usage…_docs.github.com](https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage "https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage")[](https://docs.github.com/en/billing/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage)

  


I rm — cached all the files, untracked them with git lfs, and then unisntalled git lfs in my repo before pushing. Unfortunately, didn’t work..

![](https://cdn-images-1.medium.com/max/800/1*M0ZlELzuuRj4f6MpUMEBkw.png)

I do want to say that GitHub was extremeley proactive, very helpful and responded fast, and gave me a refund for data I didn’t need.

  


Currently, this is not on our public roadmap(<https://github.com/github/roadmap/projects/1>) but I think this a feedback worth sharing with the GitHub LFS team.
