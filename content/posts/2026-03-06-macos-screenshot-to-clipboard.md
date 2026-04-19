---
title: "macOS Screenshot To Clipboard"
date: 2026-03-06T22:12:39-0800
draft: false
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

# Automatically copy macOS screenshots to the clipboard (while still saving the file)

I don't like pressing `ctrl` in addition to `cmd + shift + 4`.

My normal screenshot flow is:

```
cmd + shift + 4 → space → click
```

This saves a screenshot to disk.

But if I want the screenshot **in the clipboard**, macOS requires:

```
cmd + shift + ctrl + 4
```

That extra key press annoys me.

The main reason: I frequently paste screenshots directly into **agentic CLI tools**, chat terminals, or editors where images can be pasted inline. I want screenshots to **save automatically** _and_ be **instantly pasteable**.

macOS does not support this natively. It only supports **file OR clipboard**, not both.

So I built a small automation.

---

# Goal

Every time a screenshot is taken:

1. macOS saves it to disk
2. the screenshot is **automatically copied to the clipboard**

So the workflow becomes:

```
cmd + shift + 4 → space → click
cmd + v
```

No extra modifier keys.

---

# Approach

The solution uses **Folder Actions** and a small **AppleScript**.

The idea:

1. macOS saves screenshots to a dedicated folder
2. a script watches that folder
3. whenever a new screenshot appears, it copies the image to the clipboard

---

# Step 1: Create a screenshots folder

Create a folder:

```
~/Pictures/Screenshots
```

This keeps automation clean and avoids watching the Desktop.

---

# Step 2: Tell macOS to save screenshots there

Press:

```
cmd + shift + 5
```

Then:

1. Click **Options**
2. Under **Save to**, choose **Other Location…**
3. Select your `Screenshots` folder

---

# Step 3: Create the AppleScript

Open **Script Editor** and paste this:

```applescript
use AppleScript version "2.4"
use framework "Foundation"
use framework "AppKit"
use scripting additions

on adding folder items to this_folder after receiving added_items
	repeat with anItem in added_items
		set itemPath to POSIX path of anItem
		my copyImageFileToClipboard(itemPath)
	end repeat
end adding folder items to

on copyImageFileToClipboard(itemPath)
	set imageRep to current application's NSImage's alloc()'s initWithContentsOfFile:itemPath
	if imageRep is missing value then return

	set pasteboard to current application's NSPasteboard's generalPasteboard()
	pasteboard's clearContents()
	pasteboard's writeObjects:{imageRep}
end copyImageFileToClipboard
```

Save the script as:

```
ScreenshotToClipboard.scpt
```

---

# Step 4: Put the script in the correct folder

Folder Actions only detect scripts located here:

```
~/Library/Scripts/Folder Action Scripts/
```

Create the directory if needed.

Move the script there.

---

# Step 5: Attach the script

Open **Folder Actions Setup**.

The fastest way:

```
cmd + space
```

Search for:

```
Folder Actions Setup
```

Then:

1. enable **Folder Actions**
2. click **+** under folders
3. choose your `Screenshots` folder
4. click **+** under scripts
5. attach `ScreenshotToClipboard.scpt`

---

# Step 6: Test

Take a screenshot:

```
cmd + shift + 4
```

Then immediately paste somewhere:

```
cmd + v
```

You should see the screenshot paste instantly.

The file also remains saved in the folder.

---

# Result

Your workflow becomes:

```
cmd + shift + 4 → space → click
cmd + v
```

No `ctrl` required.

---

# Screenshot setup

_(Insert screenshot of macOS screenshot options here)_

---

# Folder actions setup

_(Insert screenshot of Folder Actions Setup UI here)_

---

# Screenshot folder structure

_(Insert screenshot of the screenshots directory here)_

---

# Notes

Folder Actions are somewhat old macOS infrastructure and can occasionally stop firing. If that happens, restarting them usually fixes it:

```
killall Folder\ Actions\ Dispatcher
killall System\ Events
```

Then take another screenshot.

---

# Why this helps with CLI workflows

Many modern developer tools support **image paste directly from the clipboard**:

- terminal-based AI agents
- chat-based dev tools
- Markdown editors
- Slack / Discord
- browser inputs

This automation removes friction from the common workflow:

```
capture → paste → continue working
```

Without adding additional key combinations.

Small improvement, but it compounds quickly if you take screenshots often.
