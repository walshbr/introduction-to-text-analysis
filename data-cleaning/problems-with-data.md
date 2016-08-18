# Problems with Data

So you have a text. You want to do something with it. It might be tempting to dive in and start running it through one of the tools in this book, but you should take a moment to examine the materials you are working with. Not all text is created equal, and your results can have real problems if you don't take care to examine the quality of the materials before you work with them.

The basic principle to remember is "GIGO," or "garbage in, garbage out:" you are not going to get good results unless you have good data to begin with.

## OCR

Take this image taken from a newspaper ad for the American film version of Sherlock Holmes:

![sherlock holmes article clipping](/assets/data-cleaning/holmes.jpg)

By default, the computer has no idea that there is text inside of this image. For a computer, an image is just an image, and you can only do image-y things to it. The computer could rotate it, crop it, zoom in, or paint over parts of it, but your machine cannot read the text there - unless you tell it how to do so. The computer requires a little extra help to pull out the text information from the image.

The process of using software to extract the text from an image of a text is called **optical character recognition** or OCR. There are many tools that can do this, and some are proprietary. All of these tools are only so good at the process. Running this image through tesseract, a common tool for OCR'ing text, I get something like this:

![ocr'd sherlock holmes text](/assets/data-cleaning/holmes-ocr-text.jpg)The material here is still recognizable as being part of the same text, though there are obvious problems with the reproduction. At first blush, you might think, "This should be easy! I learned to read in first grade \[or whenever you learned to read\]. I can even read things written in cursive! Why does the computer have such a hard time with this?" This is one of those instances where what is really easy for you is really hard for a computer. Humans are great at pattern recognition, which is essentially what OCR is. Computers, not so much.

OCR'ing text is actually a pretty complicated problem for computers. [WhatFontis.com](https://www.whatfontis.com) lists over 342,000 fonts, and this count only appears to include Western fonts. A single word will look slightly different in each font and at each size. And that doesn't even begin to account for hand-written text or text that has been partially damaged: even a slight imperfection in a letter can complicate the scanning process. The process is complicated and takes a lot of work: even the most expensive OCR software is prone to errors. If you see clean text transcriptions of an image online, odds are high that a human cleaned up the OCR to make it readable. You can find a more detailed explanation of how OCR workings [here](http://www.explainthatstuff.com/how-ocr-works.html).

## Data Cleaning

Let me say it again, computers cannot infer. Imagine this scenario:

I'm going to count to ten!

1,2,3,4,5,6,7,8,10

You probably meant to have a 9 in there, but the computer will have no idea that you probably mistyped and left out a number. You would have to specifically tell it to account for such errors. This simple fact about computational logic becomes a big problem in the humanities, because humanities data is _messy_. To see what I mean, go check out the Wikipedia section on Sir Arthur Conan Doyle's [name](https://en.wikipedia.org/wiki/Arthur_Conan_Doyle#Name). I will wait. Here is a picture of a cat in the meantime. Imagine it's a cat high fiving you when you clean up some data.

![high fiving cat](/assets/data-cleaning/data-cat-high-five.jpg)

Did you read it? Don't lie to me.

Doyle has a complicated naming history, to say the least. Now iImagine you are putting together a database of authors. You get to Doyle. How will you save his name? I can think of a number of possibilities:

DoyleArthur DoyleA.C. DoyleDoyle, A.C.Doyle, Sir ArthurDoyle, Sir Arthur ConanSir Arthur Conan Doyle

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
Author Name
---
Austen, Jane: last_name, first_name
Arthur Doyle: first_name last_name
```

A computer program would need a way to understand what you are giving it, something like:

1. Look at this 'Author Name' database.2. Each Author has a line of its own.3. Get the Author's name.

This data would cause all sorts of problems with the third step. To begin, how does the computer get the names? There are two options here:

* Look at the line for a comma. Before the comma, you will find the first name. After, the last name.* Look at the line for a space. Before the space, you will find the first name. After, the last name.

The former is the more common way of representing data like this. Using commas to denote the different pieces of data is so popular that the format has its own name: **comma seperated value** or **csv**. It has an advantage over the second format that breaks apart data based on spaces:

```
Author Names
---
Austen Jane
Arthur Doyle
Arthur Conan Doyle
```

If we used spaces to denote breaks between first name and last name, Arthur Conan Doyle would cause our program to error. It would likely interpret 'Arthur' as the first name and 'Conan' as the last name. 'Doyle' would be an unkown. Reformatting this as a csv allows us to handle Conan Doyle's full name:

```
Author Names
---
Austen, Jane
Arthur, Doyle
Arthur Conan, Doyle
```

The next problem should be obvious: Jane Austen is in a last\_name, first\_name format, while the others are in the reverse. So our final version of this dataset would look like this:

```Author Names---Austen, JaneDoyle, ArthurDoyle, Arthur Conan```

We might go further to associate Arthur Doyle and Arthur Conan Doyle as being representations of the same person, a process known as **authority control**. A common way of referring to data that contains inconsistencies and\/or errors is as **dirty data**. To keep the metaphor, then, the process of revising data to remove such problems and prepare it for use is called **data cleaning**.

## Metadata

If you have ever searched for a book using a library search interface, you have interacted with metadata categories. **Metadata**, in its most basic sense, is data about data. A text, after all, is more than just the words on the page. We have a whole range of other information that we use to describe the document. The author, its date of publication, its publisher, its copyright status, etc.: we might care deeply about these pieces of information, and we might want you to use them for particular analyses. These categories allow for more nuance, for us to be able to search for books with particular titles from particular time periods. In our previous example, we were actually working with metadata without realizing.

```
Author Names
---
last_name, first_name
Austen, Jane
Doyle, Arthur
Doyle, Arthur Conan
```

We have two metadata categories here: last\_name, and first\_name. Each are separated by a comma. We might even think of author\_name as being its own metadata category for someone else's list of books! Databases are really these sorts of things at their heart: data and metadata, organized in systematic ways to make them easily usable.

Imagine: now that you have started to put together your own table of author names, you notice that your neighbor is putting together one of her own. You want to be able to compare notes and, even more, you want to combine lists. It should be obvious that you will have real problems if you organize things in "first\_name last\_name" and she organizes things in "last\_name, first\_name". You would need to do a lot of extra work to reorganize things. It would have been easier if you were working with an accepted standard for how author names should be listed.

Such metadata standards exist, and a lot of work goes into maintaining them \(check out [Dublin Core](dublincore.org/specifications) if you are interested in learning more\). These standards ensure that anyone producing a new dataset creates work that could easily translate and communicate with other systems. They ensure that your local library's data could eventually be drawn into the [Digial Public Library of America](https://dp.la) and made available on a large scale. The process might seem easy with this basic author name example, but imagine trying to coordinate such metadata standards for all people working on all types of cultural objects, all over the world. The work never ends.

You can fall down a deep pit looking at all the different metadata standards and their uses. For now, I just want you to be familiar with the concepts.
