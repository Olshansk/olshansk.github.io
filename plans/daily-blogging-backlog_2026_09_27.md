# Daily Blogging: Workflow and Writing Backlog <!-- omit in toc -->

Date captured: 2026-09-27
Source: Notes supplied by Olshansky from another thread.
Status: Captured ideas and proposed workflow; unpublished.

- [Working agreement](#working-agreement)
- [Publishing system proposal](#publishing-system-proposal)
  - [Recommended architecture](#recommended-architecture)
  - [Voice commands](#voice-commands)
- [Current writing backlog](#current-writing-backlog)
  - [1. Personal publishing system](#1-personal-publishing-system)
  - [2. Work-related posts](#2-work-related-posts)
  - [3. The unexpected Uber-driver conversation](#3-the-unexpected-uber-driver-conversation)
  - [4. Tolerance for pain](#4-tolerance-for-pain)
  - [5. Fashion after two weeks in New York](#5-fashion-after-two-weeks-in-new-york)
  - [6. The person at the mall](#6-the-person-at-the-mall)
- [Suggested starting point](#suggested-starting-point)

_Capture ideas now, develop drafts through dictation, and publish only when explicitly requested._

## Working agreement

- Use this thread for daily blog ideas and dictation.
- Create new drafts or add to existing drafts as thoughts arrive.
- Preserve Olshansky's voice while cleaning up grammar and structure.
- Keep drafts unpublished until Olshansky explicitly asks to publish.
- Preserve “PB screenshot” and “EOS” exactly; their meanings have not been supplied.

The proposal and backlog below preserve the supplied notes.
Product capabilities mentioned in the proposal have not been verified as part of this capture.
The proposed automation has not been implemented.

## Publishing system proposal

The cleanest setup is to treat capture, writing, and publishing as separate stages.
Codex should be the writing/publishing agent, not the thing responsible for recording you.

### Recommended architecture

iPhone → audio/transcript inbox → Codex → mobile review → publish

Apple already gives you most of the capture layer.
Vocal Shortcuts can listen for a custom phrase and execute an action, while Siri can run any normal Shortcut by name.
The Action Button can also invoke a Shortcut or Voice Memo if you want a physical trigger instead.
Apple Notes can already record audio and generate transcripts, although I’d probably build our own Shortcut workflow rather than use Notes as the permanent storage layer.

On the other side, Codex now has an SDK specifically for embedding the agent in workflows, plus GitHub Actions support, so the actual writing/publishing pipeline can be fully automated.

### Voice commands

I’d build two voice commands:

- “Blog note”: immediately starts recording.
  When finished, saves the audio, transcribes it, timestamps it, and drops it into something like `inbox/2026-09-26-uber-driver.md`.
  No editing, no friction.
- “Write blog”: takes one or more inbox notes, gives them to Codex with your `STYLE.md`, turns them into a finished post, creates a PR, and sends you the rendered preview on your phone.
  You review it there and either say/tap publish, revise, or leave as draft.
  Merging the PR automatically deploys the site.

That gives you the workflow you actually want: you never need to sit down at your laptop just because you had something worth writing about.

## Current writing backlog

I’m preserving “PB screenshot” and “EOS” exactly rather than guessing what you mean by them.

### 1. Personal publishing system

- Streamline daily personal blogging.
- Connect the blog repository/site to Codex.
- Audio → transcript → review/edit → publish.
- Entire workflow needs to work from the phone.
- Set up a voice activation phrase / Vocal Shortcut for instant voice-note capture.
- Recordings should be persisted somewhere, transcribed, and available for later retrieval and synthesis.

### 2. Work-related posts

- PB screenshot at work.
- Your skill + agent setup at work.
- Windows sandboxing at work.
- EOS at work.

### 3. The unexpected Uber-driver conversation

- You normally don’t talk much with Uber drivers, but occasionally you do and the conversation is unexpectedly compelling.
- Driver was involved in import/export.
- Has dealt with/worked with Flexport.
- Worked at one of Paul Allen’s companies.
- Knows a lot about cars.
- Goes hiking constantly.
- Very laid-back, apparently high, but clearly someone who works hard and plays hard.
- Interesting reminder that people you encounter randomly can have unusually rich lives and can be successful entirely on their own terms.

### 4. Tolerance for pain

- Respond to/reference the other posts you’ve read about the importance of a high tolerance for pain.
- Counterpoint: a genuinely high pain tolerance can become dangerous when combined with fear of failure.
- You can keep pushing long after the point when another person would recognize that something needs to change.
- Eventually that is how you break.
- Your recurring personal metric: “Did I create more output on this earth today than I consumed as input?”
- Output can mean work, family, friendship, or broader contribution.
- This is unfortunately a major motivating mechanism for you.
- Some people genuinely seem able to optimize for simply being happy.
  You envy that, but don’t identify with it.
- Potential tension of the essay: pain tolerance is an advantage until your inability to stop becomes the failure mode.

### 5. Fashion after two weeks in New York

- Spending two weeks in NYC changed your appreciation for dressing well.
- Comfort isn’t the entire objective.
- Clothing appropriate to the occasion actually changes something about the experience.
- There is value in looking intentionally well-dressed rather than purely optimizing for utility/comfort.

### 6. The person at the mall

- Write about meeting someone who was unusually willing to actually help you dress well.
- It stood out because people rarely invest that much effort in helping another person find their look.
- Could potentially connect this to the New York fashion essay rather than necessarily being its own post.

## Suggested starting point

The system itself should probably be the first project, because once it exists, everything underneath it becomes much easier to turn into published writing.
