standards, metadata

# OCR

Take this image taken from a newspaper ad for the [American film *Sherlock Holmes* in 1922](https://commons.wikimedia.org/wiki/File:Sherlock_Holmes_(1922)_-_6.jpg):

![sherlock holmes article clipping](/assets/holmes.png)

By default, the computer has no idea that there is text inside of this image. For a computer, an image is just an image, and you can only do image-y things to it. The computer could rotate it, crop it, zoom in, or paint over parts of it, but your machine cannot read the text there - unless you tell it how to do so. The computer requires a little extra help to pull out the text information from the image.

The process of using software to extract the text from an image of a text is called **optical character recognition** or OCR. There are many tools that can do this, and some are proprietary. All of these tools are only so good at the process. Running this image through tesseract, a common tool for OCR'ing text, I get something like this:

![ocr'd sherlock holmes text](/assets/holmes_ocr_text.png)
The material here is still recognizable as being part of the same text, though there are obvious problems with the reproduction. At first blush, you might think, "This should be easy! Why does the computer have such a hard time with this?" OCR'ing text is actually a pretty complicated problem for computers. [WhatFontis.com](https://www.whatfontis.com) lists over 342,000 fonts, and this count only appears to include Western fonts. A single word will look slightly different in each font and at each size. And that doesn't even begin to account for hand-written text or text that has been partially damaged: even a slight imperfection in a letter can complicate the scanning process. The process is complicated and takes a lot of work: even the most expensive OCR software is prone to errors. If you see clean text transcriptions of an image online, odds are high that a human cleaned up the OCR to make it readable. You can find a more detailed explanation of how OCR workings [here](http://www.explainthatstuff.com/how-ocr-works.html). 

# Standards

Let me say it again, computers cannot infer. Imagine this scenario:

I'm going to count to ten!

1,2,3,4,5,6,7,8,10

You probably meant to have a 9 in there, but the computer will have no idea that you probably mistyped and left out a number. You would have to specifically tell it to account for such errors. This simple fact about computational logic becomes a big problem in the humanities, because humanities data is *messy*. To see what I mean, go check out the Wikipedia section on Sir Arthur Conan Doyle's [name](https://en.wikipedia.org/wiki/Arthur_Conan_Doyle#Name). I will wait. Here is a picture of a cat in the meantime. Imagine it's a cat high fiving you when you clean up some data.

![high fiving cat](/assets/data_cat_high_five.png)

Did you read it? Don't lie to me.

Doyle has a complicated naming history, to say the least. Now iImagine you are putting together a database of authors. You get to Doyle. How will you save his name? I can think of a number of possibilities:

Doyle
Arthur Doyle
A.C. Doyle
Doyle, A.C.
Doyle, Sir Arthur
Doyle, Sir Arthur Conan
Sir Arthur Conan Doyle

You can probably imagine others. All of these are technically correct, and they might serve your purposes just fine. But you need to be consistent. Remember how computers cannot infer anything? Imagine this as part of your database of authors:

```
Author Name
---
Austen, Jane
James Joyce
Arthur Conan Doyle
```

You are working with a number of formats:

```
Austen, Jane: last_name, first_name
James Joyce: first_name last_name
Arthur Conan Doyle: first_name last_name or first_name middle_name last_name (depending on your reading of the biography)
```
A computer program would need a way to understand what you are giving it, something like: 

1. Look at this 'Author Name' database.
2. Each Author has a line of its own.
3. For each 

So this data would cause all sorts of problems. Reorganizing

dirty data
different formats
**dirty data**
**data cleaning**
changing standards

sustainability