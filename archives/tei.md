# Text Encoding Initiative


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


This book studies texts and the things that computers can do with them. But, as you read along, you may notice that they cannot do all that much. Many of the methods that you will learn are simply different ways are simply sophisticated ways of counting words, but it should be immediately clear that reading entails far more complicated processes of interpretation and analysis. When we read, we tend to skip straight on to much more complicated understandings of a text:

> What does it mean?

> How does it mean?

Computers have a hard with abstract concepts like this. They tend to work in hierarchies and clear-cut structures, and, even then, only know about those structures that someone has told it about. For example, if I were to say to a computer, "Hey! Find me the poem in this lesson!" It would have no idea what I was talking about: I have to let find some way of telling it where it can find the poem. Right now it just thinks the text up there is no different from the other lines of text on this page.

A computer program looking at the above passage from Oscar Wilde's *The Ballad of Reading Gaol* would, most likely, not even recognize those six lines as related in any way. Nor it would understand anything about how the internal components of those lines relate to each other. There are a number of ways to do this, and we can get towards one that works for a computer by working through a few that you might use on your own. 

Think about all the annotations that you put on your own pages as you read them. If you are anything like me, your markings tend to be all over the place. But imagine if you were to systematically note certain structural features of the text. We can think of the passage, after all, as a series of nested concepts:

* There is a stanza.
* This stanza contains some lines.
* Each line has text.
* Some of that text contains a rhyme.

And we can represent it graphically, like so, where black denotes the stanza boundaries, horizontal blue the lines, and the rotating colors under the final words describe a rhyme scheme:

![marking up poem by hand graphically](/assets/archives/tei-graphic.jpg)

But you probably would need a moment to realize what was going on if you came to this having not highlighted things yourself. We can perform a similar function with text annotations, which gets closer to a meaning that we could understand without having any prompting:

![tei with text annotations](/assets/archives/tei.jpg)

But for a computer to understand this, we need an even more delineated way of describing the passage. We have to pay careful attention to **syntax**, the ways in which we mark particular things to provide information to the computer. Computers require very specific systematic guidelines to be able to process information, as you will learn in our chapter on Cyborg readers. Scholars have been working for years to develop such a system for describing texts in a way that can be processed by software. The *Text Encoding Initiative* (TEI), the result of this work, is an attempt to make abstract humanities concepts legible to machines. TEI applied to the passage, might begin to look something like this:

```
<lg>
  <l>Yet each man kills the thing he loves</l>
  <l>By each let this be heard.</l>
  <l>Some do it with a bitter look,</l>
  <l>Some with a flattering word.</l>
  <l>The coward does it with a kiss,</l>
  <l>The brave man with a sword!</l>
</lg>```

Notice how our concepts like 'stanza' and 'line' have here translated into particular **tags** like <lg> and <l>. Each set of tags has both an opening (<lg>) and a closing (</lg>) tag, the latter of which is almost identical except for a forward slash - /. These framing elements help the computer understand the boundaries of the concepts we are describing, and they help to provide structure to the text. They also have intuitive relationships to the concepts that they represent: <l> corresponds to line, and <lg> corresponds to line group. Think of TEI as a new layer that exists on top of the text. Words offer one layer of meaning, but we add **markup** to give the computer (or future readers) more nuanced ways of understanding how the parts in a text relate to one another.

We can give further details to the poem. For example:

```
<lg type="poem">
  <lg type="stanza">
    <l>Yet each man kills the thing he loves</l>
    <l>By each let this be heard.</l>
    <l>Some do it with a bitter look,</l>
    <l>Some with a flattering word.</l>
    <l>The coward does it with a kiss,</l>
    <l>The brave man with a sword!</l>
  </lg>
  <lg type="stanza">
    <l> A short second stanza that I've made up.</l>
  </lg>
</lg>```

Here I've added an exta stanza group as well as an outer tag to denote this is, in fact, a poem. We also give **attributes** to certain tags to give more information about them - type="stanza" tells the computer that the contents of this tag refer to a poem. Remember the nested hierarchy we talked about earlier? Notice how we are representing it graphically by indentation. The outer poem element contains two stanzas, which contain some lines, and those have some text. You can run your eye down the text and see the structure. Some programming languages will actually error if you do not pay attention to such things. But, either way, it just helps us keep things clean and easy to read. 

One last one. Remember our rhyme scheme and line numbers? We can encode those too:

``` 
<lg type="stanza">
    <l n="1" rhyme="a">Yet each man kills the thing he <rhyme>loves</rhyme></l>
    <l n="2" rhyme="b">By each let this be <rhyme>heard</rhyme>.</l>
    <l n="3" rhyme="c">Some do it with a bitter <rhyme>look</rhyme>,</l>
    <l n="4" rhyme="b">Some with a flattering <rhyme>word</rhyme>.</l>
    <l n="5" rhyme="d">The coward does it with a <rhyme>kiss</rhyme>,</l>
    <l n="6" rhyme="b">The brave man with a <rhyme>sword</rhyme>!</l>
  </lg>
 ```

I have added attributes to denote the line numbers for each line as well as the rhyme scheme, and then a new <rhyme> tag for each line denotes what word the rhyme is associated with. All of the tags used here can be found in the tutorial on poetry of the [TEI by Example](http://teibyexample.org/modules/TBED04v00.htm) page.

Once a text has been **encoded** in this way, it can be represented more easily in a digital form. This work may not necessarily actually make it *look* any different. But it does allow you to do new and exciting things to your work. TEI encoding can make it possible to provide nuanced digital editions of a work. We could actually say to a program, pull out all the rhyming words in a poem. Make them appear differently on a webpage. Change them all to "TEI is the best."

Encoding is meant to convey abstract humanities concepts to the machine so that we can make better use of them in our digital work. Some of these concepts, like line breaks, might be pretty clear cut. Others might require a lot of interpretation. You might decide certain tags are important, and even given the same set of tags and texts, two people could encode things different. You can make a whole career off working with TEI, and we have just scratched the surface here. But encoding documents in TEI is an important step in preparing them for life as digital artifacts. Not all texts need to be encoded in TEI in order for them to be archived, but the vast majority of documents you will find in digital humanities archives have been encoded in this way. The process helps ensure that complex humanities data makes its way comfortably, ethically, and responsibly into the digital world.