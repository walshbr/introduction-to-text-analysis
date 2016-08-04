standards, metadata

# OCR

Take this image taken from a newspaper ad for the [American film *Sherlock Holmes* in 1922](https://commons.wikimedia.org/wiki/File:Sherlock_Holmes_(1922)_-_6.jpg):

![sherlock holmes article clipping](/assets/holmes.png)

By default, the computer has no idea that there is text inside of this image. For a computer, an image is just an image, and you can only do image-y things to it. The computer could rotate it, crop it, zoom in, or paint over parts of it, but your machine cannot read the text there - unless you tell it how to do so. The computer requires a little extra help to pull out the text information from the image.

The process of using software to extract the text from an image of a text is called **optical character recognition** or OCR. There are many tools that can do this, and some are proprietary. All of these tools are only so good at the process. Running this image through tesseract, a common tool for OCR'ing text, I get something like this:

![ocr'd sherlock holmes text](/assets/holmes_ocr_text.png)
The material here is still recognizable as being part of the same text, though there are obvious problems with the reproduction. At first blush, you might think, "This should be easy! Why does the computer have such a hard time with this?" OCR'ing text is actually a pretty complicated problem for computers. [WhatFontis.com](https://www.whatfontis.com) lists over 342,000 fonts, and this count only appears to include Western fonts. A single word will look slightly different in each font and at each size. And that doesn't even begin to account for hand-written text or text that has been partially damaged: even a slight imperfection in a letter can complicate the scanning process. The process is complicated and takes a lot of work: even the most expensive OCR software is prone to errors. If you see clean text transcriptions of an image online, odds are high that a human cleaned up the OCR to make it readable. You can find a more detailed explanation of how OCR workings [here](http://www.explainthatstuff.com/how-ocr-works.html). 

# Standards

Let me say it again, computers cannot infer. If you write:

I'm going to count to ten!

1,2,3,4,5,6,7,8,10

The computer will have no idea that you probably mistyped and left out a number. You would have to specifically tell it to account for such errors. This simple fact about computational logic becomes a big problem in the humanities, because humanities data is *messy*

dirty data
different formats

changing standards

sustainability