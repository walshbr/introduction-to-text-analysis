# TEI


This book studies texts and the things that computers can do with them. But, as you read along, you may notice that they cannot do all that much. Many of the methods that you will learn are simply different ways are simply sophisticated ways of counting words, but it should be immediately clear that reading entails far more complicated processes of interpretation and analysis. When we read, we tend to skip straight on to much more complicated understandings of a text:

> What does it mean?

> How does it mean?

Computers have a hard with abstract concepts like this. They tend to work in hierarchies and clear-cut structures. 

>Yet each man kills the thing he loves
>
>By each let this be heard.
>
>Some do it with a bitter look,
>
>Some with a flattering word.
>
>The coward does it with a kiss,
>
>The brave man with a sword!

The computer does not really know much at all about this poem. A computer program looking at this passage would, most likely, not even recognize it as related. But we might be interested in making the computer better able to represent the kinds of things that a human might find interesting in the passage. 

We can think of the passage, after all, as a series of nested concepts:

* There is a stanza.
* This stanza contains some lines.
* Each line has text.
* Some of that text contains a rhyme.

And we can represent it graphically, like so, where black denotes the stanza boundaries, horizontal blue the lines, and the rotating colors under the final words describe a rhyme scheme:

![marking up poem by hand graphically](/assets/tei_graphic.png)

But you probably would need a moment to realize what was going on if you came to this having not highlighted things yourself. We can perform a similar function with text annotations, which gets closer to a meaning that we could understand without having any prompting:

![tei with text annotations](/assets/tei.png)

The *Text Encoding Initiative* (TEI) is an attempt to join abstract humanities concepts with the kinds of systematic 

Think of TEI as a new layer that exists on top of the text. Words offer one layer of meaning, but we add **markup** to give the computer (or future readers) more nuanced ways of understanding how the parts in a text relate to one another.
Once a text has been **encoded** in this way, it can be represented more easily in a digital form. This may not necessarily actually make it *look* any different. But it does allow you to do new and exciting things to your work. For example, TEI encoding can make it possible to provide nuanced digital editions of a work.