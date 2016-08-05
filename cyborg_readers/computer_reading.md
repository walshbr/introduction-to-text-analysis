# How Computers Read Texts

If you have been dutifuly following along until now, it should become clear that computers have a hard time understanding data. They can interact with and use data, but they make very few assumptions and even fewer interpretations about data. Those that they do have been specifically programmed into the computer's software. In the context of text analysis, this means that computers have a hard time reading. Consider the following sentence:

"I saw 8<sup>1/2</sup>."

Taken alone, the sentence doesn't tell us much. Its meaning depends a lot on the question to which I might be responding, and I can think of two possible questions with very different contexts:

> "How many movies did you see?

> "What movie did you see?"

In the first case, I might be responding with a number of movies that I had seen. In the second, I'm responding with the title of a specific film, [*8<sup>1/2</sup>* by Italian director Frederico Fellini](https://en.wikipedia.org/wiki/8%C2%BD). One is a number, and one is a name. For humans, the difference is mostly trivial, and we would be able to distinguish between the two by context. 

Computers cannot make inferences like these, and this fact has serious implications: numbers and words have significantly different uses. Here are two further extensions of the conversation:

> If you add four to how many movies you saw, what is the result?

If I was talking about a number of movies, my response would clearly be, "Oh that's 12.5. Why are you giving me a math quiz?" If I was talking about the Fellini film, I might respond, "What? Oh, I was talking about a title, not a number. I can't add things to a title."

Programmers have developed conventions for telling computers to distinguish between these **data types**.  There are two important ones for our purposes here:

**String**: characters, the stuff of words

**Integer**: a whole number

If you go on to learn how to program, you might find slightly different names depending on the programming language, and you will be introduced to other data types as well. But distinction between strings and integers is important for text analysis. You can perform arithmetic operations on the one while the other responds less well to such things. You can capitalize words, but not numbers. And computers generally want you to deal with similar objects: you can combine strings (words can become sentences) or add numbers, but you trying to combine a string and an integer will break things.

But notice that my beginning answer hinged on the ambiguity between strings and integers. How does a computer know whether we are talking about strings or about integers in cases where they could refer to either? How does it now that I want 8 to function as a word and not as a number in this context?

Programmers over the years have built a variety of functions and tools into different languages to get around some of these difficulties, but they still remain. When processing text by a computer, we have to account for such problems. We generally do this by following very strict guidelines for inputting information. This **syntax** works in much the same way as grammar does for humans - helping the computer to keep track of what we mean and what we want it to do. 

In


So to a computer, the following are entirely unrelated:

8 ≠ "8" ≠ "Eight" ≠ "Eighth"

It goes even further: computers think of lowercase and capital letters as different. 

"H" ≠ "h"

They only do what you (or decades of programmers) have taught them to do. In fact, by default, they do not know how to do much of anything. In almost all cases, the computer can only read for the things you tell it to read for. 

tokens and types

**Tokens**
**type**
