OCR, Dirty OCR, standards, metadata

Take this image taken from a newspaper ad for the [American film *Sherlock Holmes* in 1922](https://commons.wikimedia.org/wiki/File:Sherlock_Holmes_(1922)_-_6.jpg):

![sherlock holmes article clipping](/assets/holmes.png)

By default, the computer has no idea that there is text inside of this image. For a computer, an image is just an image, and you can only do image-y things to it. The computer could rotate it, crop it, zoom in, or paint over parts of it, but your machine cannot read the text there - unless you tell it how to do so. The computer requires a little extra help to pull out the text information from the image.

The process of using software to extract the text from an image of a text is called **optical character recognition** or OCR. There are many tools that can do this, and some are proprietary. All of these tools are only so good at the process. Running this image through tesseract, a common tool for OCR'ing text, I get something like this:

![ocr'd sherlock holmes text](/assets/holmes_ocr_text.png)
Still recognizable as being part of the same text, though there are obvious problems with the reproduction. At first blush, you might think, "This should be easy! Why does the computer have such a hard time with this?" OCR'ing text is actually a pretty complicated problem for computers. Consider

You can find a more detailed explanation of how OCR workings [here](https://www.explainthatstuff.com/how-ocr-works.html)

here are some example edits

dirty data
different formats

changing standards

sustainability