# How Computers Read Texts

When preparing for text analysis, this becomes im 
Consider the following sentence:

"I saw 8<sup>1/2</sup>."

Taken alone, the sentence doesn't tell us much. Its meaning depends a lot on the question to which I might be responding, and I can think of two possible questions with very different contexts:

"How many movies did you see?
"What movie did you see?"

In the first case, I might be responding with a number of movies that I had seen. In the second, I'm responding with the title of a specific film, [*8<sup>1/2</sup>* by Italian director Frederico Fellini](https://en.wikipedia.org/wiki/8%C2%BD). One is a number, and one is a name. For humans, the difference is mostly trivial, and we would be able to distinguish between the two by context.

Computers cannot make inferences like these. Since numbers and words have significant differences - you can divide the former, but not the latter - programmers have developed conventions for telling computers to distinguish between these **data types**.

**String**: characters, the stuff of words

**Integer**: a whole number

So to a computer, the following are entirely unrelated:

8 ≠ "8" ≠ "Eight" ≠ "Eighth"

It goes even further: computers think of lowercase and capital letters as different:

"H" ≠ "h"

Programmers over the years have built a variety of functions and tools into different languages to get around some of these difficulties, but they still remain. When processing text by a computer, we have to account for such problems.

They only do what you (or decades of programmers) have taught them to do. In fact, by default, they do not know how to do much of anything. In almost all cases, the computer can only read for the things you tell it to read for. 

tokens and types