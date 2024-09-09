# Move Fast & Document Things <!-- omit in toc -->

**I'm going to share a small secret: a perfect solution to software documentation does not exist.**

The documentation at any stage of a project is heavily reliant on everything ranging
from the customer's needs, the team's culture,the seniority of the individuals
on the team, the type of project, its maturity, as well as the company's runway
or the velocity at which the product is changing.

I feel like I can write an individual blog post about each of the points in the paragraph above, but alas, I won't.

Anyone who has worked with me knows what a 🥙 PITA (Pain In The Ass) when it comes to documentation.
Though I do occasionally catch myself asking for too much, I put a lot of effort
into staying reflecting on my asks, staying cognizant and being pragmatic.

**No one loves putting a lot of effort into documentation that becomes deprecated the week
after. At the same time, everyone complains that there's nothing worse than having a
codebase, tool or product without any documentation. In fact, there is, it's
documentation without a codebase, tool or product to support it.**

## Why - What's the motivation for documenting things? <!-- omit in toc -->

Whenever I ask for someone to document something, I have a few key motivations:

1. I like to be self-sufficient
2. I don't like to be confused
3. I don't like to waste time
4. I don't like context switching
5. I always operate under the assumption that I might get hit by a bus tomorrow

The points above are pretty selfish, but what I want for myself, I also want for
everyone I work with, either day-to-day or indirectly.

Over the last few years, I've picked up a few tips & tricks that I believe help
find a balance between moving fast and documenting things, and I'm hoping they
can help others too.

_Note: I'm going to be using some platform specific terminology (e.g. GitHub, Notion, Discord)
related to the tools our team uses on a daily basis, but replace it with whatever
tools your organization uses instead. Everyone has their equivalent of source control
manager, documentation tooling, knowledge base, issue tracker, etc..._

- [#PUC (Please Update Comment) - A quick and easy request while reviewing code and asking questions](#puc-please-update-comment---a-quick-and-easy-request-while-reviewing-code-and-asking-questions)
- [TODO_XXX - Customize XXX to provide a signal on the type of TODO it really easy](#todo_xxx---customize-xxx-to-provide-a-signal-on-the-type-of-todo-it-really-easy)
- [TODO All The Things - Satisfy that Engineer OCD craving by being very liberal with TODOs](#todo-all-the-things---satisfy-that-engineer-ocd-craving-by-being-very-liberal-with-todos)
- [Leave Links Everywhere - Leave a trail of links to both internal or external resources that provide necessary context](#leave-links-everywhere---leave-a-trail-of-links-to-both-internal-or-external-resources-that-provide-necessary-context)
- [Diagrams - Only focus on one sub-system or flow at a time](#diagrams---only-focus-on-one-sub-system-or-flow-at-a-time)
- [Diagrams - Leverage AI tools to bypass the blank page problem](#diagrams---leverage-ai-tools-to-bypass-the-blank-page-problem)
- [GitHub Issues - Use screenshots as the context for an issue you want to track for the future](#github-issues---use-screenshots-as-the-context-for-an-issue-you-want-to-track-for-the-future)
- [GitHub Conversations - Once it's resolved, #PUC](#github-conversations---once-its-resolved-puc)
- [Naming Things - 15 seconds can save you 15 minutes or more](#naming-things---15-seconds-can-save-you-15-minutes-or-more)
- [Documenting Code Blocks - If you've a nice code block, add a comment!](#documenting-code-blocks---if-youve-a-nice-code-block-add-a-comment)
- [Self Explanatory Code - If done well, you can remove the comments altogether](#self-explanatory-code---if-done-well-you-can-remove-the-comments-altogether)
- [Prgamatic Function Comments - Break the rules by being pragmatic about what's actually necessary](#prgamatic-function-comments---break-the-rules-by-being-pragmatic-about-whats-actually-necessary)
- [Wishlist](#wishlist)
- [Bonus - How NOT TO document things](#bonus---how-not-to-document-things)
- [Bonus - How TO document things](#bonus---how-to-document-things)

## #PUC (Please Update Comment) - A quick and easy request while reviewing code and asking questions

If you're ever reviewing code and have a question at a particular spot, leave a comment with a #PUC tag at the end.

There are so many interesting, discussions and explanations that take place in GitHub threads that simply get lost. The correspondence
is between two people, who may forget the details in the future, and it gets lost in the GitHub verse.

If you ask a question with a #PUC at the end, it informs the reader that a certain part of the code

it informs the author that once the discussion is finishedI've found that simply asking a question with a #PUC at the end asking a question withleaving a comment

I've found that there are golden

_TODO: Add a screenshot and linking with an example of this._

## TODO_XXX - Customize XXX to provide a signal on the type of TODO it really easy

SHow our Makefile helpers

Talk about how it accounts for the OCD every engineer has

You get to show you know what needs to be done without getting distracted

Bonus: TODO_XXX(#123, @olshansk): To show who should own it and a link to the ticket if a related one is available.

_TODO: Add a link and embed the code for our Makefile._

## TODO All The Things - Satisfy that Engineer OCD craving by being very liberal with TODOs

How many times have you wanted to fix a bug, add another feature or refactor something while working on a complete unrelated feature?

We all know it's the right thing to do, but the urge to resist it is not easy. TODOs give us an easy way out to satisfy
that craving by writing it down, ensuring it never gets lost, disseminating it with the rest of the team, and the satisfaction
of knowing that something needs to be done even though we know it's not a priority.

Additionally, whenever TECHDEBT week comes around, all you need to do is `grep -r "TODO" .` and you've got a starting point.
If the scope of a particular TODO is large enough to warrant it's on GitHub Issue, you can just take a screenshot of the TODO
with the surrounding context as the origin document and fill in the rest of the details.

_TODO: Show an example grep command (plus awk) that makes tracking work really easy during techdebt week._

_TODO: Show the makefile helpers we have explaining how many todos we already have._

## Leave Links Everywhere - Leave a trail of links to both internal or external resources that provide necessary context

Whether it's a link to another pull request, a thread on github you'll need to refer to later, a discord channel, a slack thread,
a notion page, or anything else, just embed it!

Usually, if you read a comment where you need more context, you'll reach out to your team and ask for it. Put yourself
in the reader's shoes and just get ahead of the question by inserting the link ahead of time. I've found this as a great
way for past olshansky to talk to future Olshansky

## Diagrams - Only focus on one sub-system or flow at a time

As a personal rule of thumb, try to limit the number of arrows or components to 10 or less.

I've both seen and created sequence diagrams that can span more than a whole page. I've also
both seen and created the "mega diagrams" that show all the major sub systems involved.
They look impressive, and we think it's what we want, but realistically all they do is just
highlight the complexity of a certain system.

_TODO: Show the sequence diagram from the relay mining paper and find another one that's much smaler_

_TODO: Show the sequence diagram from the relay mining paper and find another one that's much smaler_

## Diagrams - Leverage AI tools to bypass the blank page problem

_TODO: Show a gif of using Excalidraw's AI to mermaid/diagram tooling._

## GitHub Issues - Use screenshots as the context for an issue you want to track for the future

Everyone hates creating issues, but you help everyone:

- A backlog for yourself
- A backlog for the team
- A backlog for the company
- If you're ever unsure of what to work on, you can just go to the backlog and pick something
- Show examples of this from work.
- This is overhead, I agree. If you feel like you’re wasting your time, don’t do it.
- Also, I’ve seen so many engineers spending time trying to understand what the goal of an issue is. If this is the case, just close it. You’ll reopen it if you need it
- Don't be afraid to

## GitHub Conversations - Once it's resolved, #PUC

We put 10X more effort in replying to comments in reviews than the comments in the docs.

Realistically

- No one looks through slack / discord history
- No one look through PR comment history
- People rarely go into the docs
- People spend their time looking in the code
- Even if you had a conversation in Discord/Slack or over a call, capture it in a comment
- No one reads documents
- No one goes through old messages

## Naming Things - 15 seconds can save you 15 minutes or more

This doesn't apply to just

skip over the content of this text block and I bet most readers Can you see how I made the title header

Insert joke about naming things (3 hard things)

Add screenshot of being Chief Naming Officer

Show a snippet from our codebase where it’s really easy to follow

_TODO: Add screenshot of me being the Chief Naming Officer_

TODO:

## Documenting Code Blocks - If you've a nice code block, add a comment!

_TODO: Add an example of a test where we can easily follow the comments to understand what's going on._

TODO: Show example of:

- Unit test
- inline functioni

## Self Explanatory Code - If done well, you can remove the comments altogether

Most readers will likely read the header for this section and skip over the actual content. We can do the same thing with function headers too.

_TODO: Find something where we use overly verbose language but it helps!_

## Prgamatic Function Comments - Break the rules by being pragmatic about what's actually necessary

I don’t need a description of each input & output variable

Don’t do “the right thing” - do the “useful and pragmatic thing”

In school, what I hate most is when they gave a minimum word count. I understand why (it’s direction), but it’s something I had to unlearn.

Show gif of GitHub Copilot doing this.

## Wishlist

1. An AI documentation solution that actually works
2. Better search of notion
3. Documentation generate from slack/discord threads

## Bonus - How NOT TO document things

1. Do not use long sentences
2. Do not write long paragraphs
3. Do not tell a story
4. Do not create "the one document to rule them all"
5. Do not create cognitive overload
6. Assume the reader is lazy
7. Assume the reader just wants to get back building

## Bonus - How TO document things

1. Put yourself in the reader's shoes
2. Use bullet points wherever possible
3. Add visuals/diagrams whenever possible
4. Keep diagrams focused on a single flow
