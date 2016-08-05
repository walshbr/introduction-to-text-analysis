# How Computers Read Texts

If you have been dutifuly following along until now, it should become clear that computers have a hard time understanding data. They can interact with and use data, but they make very few assumptions and even fewer interpretations about data. Those that they do have been specifically programmed into the computer's software. In the context of text analysis, this means that computers have a hard time reading. Consider the following sentence:

"I saw 8<sup>1/2</sup>."

Taken alone, the sentence doesn't tell us much. Its meaning depends a lot on the question to which I might be responding, and I can think of two possible questions with very different contexts:

> "How many movies did you see?

> "What movie did you see?"

In the first case, I might be responding with a number of movies that I had seen. In the second, I'm responding with the title of a specific film, [*8<sup>1/2</sup>* by Italian director Frederico Fellini](https://en.wikipedia.org/wiki/8%C2%BD). One is a number, and one is a name. For humans, the difference is mostly trivial, and we would be able to distinguish between the two by context. 

Computers cannot make inferences like these, and this fact has serious implications: numbers and words have significantly different uses. Here are two further followups.

> If you add four to how many movies you saw, what is the result?
> 

you can divide the former, but not the latter - programmers have developed conventions for telling computers to distinguish between these **data types**.

**String**: characters, the stuff of words

**Integer**: a whole number

So to a computer, the following are entirely unrelated:

8 ≠ "8" ≠ "Eight" ≠ "Eighth"

It goes even further: computers think of lowercase and capital letters as different. 

"H" ≠ "h"

Programmers over the years have built a variety of functions and tools into different languages to get around some of these difficulties, but they still remain. When processing text by a computer, we have to account for such problems. We generally do this by following very strict guidelines for inputting information. This **syntax** works in much the same way as grammar does for humans - helping the computer to keep track of what we mean and what we want it to do.

They only do what you (or decades of programmers) have taught them to do. In fact, by default, they do not know how to do much of anything. In almost all cases, the computer can only read for the things you tell it to read for. 

tokens and types

**Tokens**
**type**
