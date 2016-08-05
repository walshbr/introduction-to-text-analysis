# How Computers Read Texts

If you have been dutifuly following along until now, it should become clear that computers and humans don't think the same way.  With respect to text analysis, we can say that computers and humans have complementary skills. Computers are good at doing the things that it would take a long time for a human to do (or that we would find incredibly tedious to do). Computers can easily count and compare and will do so for pretty much as long as you tell them to do so. In contrast, humans are very good at understanding nuance and context. Thus, you wouldn't want a computer to do any close reading, or unpack the claims of a primary or secondary text; this is something you are far better at. 

If that's the case, you may be wondering why we're teaching a class on text analysis. The answer is that there are a lot of instances where you can combine what humans are good at with what computers are good at to look at texts in new and creative ways. In particular, you can make computers do a lot of the repetitive work that you might find tedious.

To do so, though, you need to know a bit about how computers process texts. It should be clear from what we've said so far that they have a hard time understanding data. They can interact with and use data, but they make very few assumptions and even fewer interpretations about data. Those that they do have been specifically programmed into the computer's software. In the context of text analysis, this means that computers have a hard time reading. Consider the following sentence:

"I saw 8<sup>1/2</sup>."

Taken alone, the sentence doesn't tell us much. Its meaning depends a lot on the question to which I might be responding, and I can think of two possible questions with very different contexts:

> "How many movies did you see?

> "What movie did you see?"

In the first case, I might be responding with a number of movies that I had seen. In the second, I'm responding with the title of a specific film, [*8<sup>1/2</sup>* by Italian director Frederico Fellini](https://en.wikipedia.org/wiki/8%C2%BD). One is a number, and one is a name. For humans, the difference is mostly trivial, and since we're good at understanding context, we would easily be able to distinguish between the two. 

Computers cannot make inferences like these, and this fact has serious implications: numbers and words have significantly different uses. Here are two further extensions of the conversation:

> If you add four to how many movies you saw, what is the result?

If I was talking about a number of movies, my response would clearly be, "Oh that's 12.5. Why are you giving me a math quiz?" If I was talking about the Fellini film, I might respond, "What? Oh, I was talking about a title, not a number. I can't add things to a title."

Programmers have developed conventions for telling computers to distinguish between these **data types**.  There are two important ones for our purposes here:

**String**: characters, the stuff of words

**Integer**: a whole number

If you go on to learn how to program, you might find slightly different names depending on the programming language, and you will be introduced to other data types as well. But distinction between strings and integers is important for text analysis. You can perform arithmetic operations on the one while the other responds less well to such things. You can capitalize words, but not numbers. And computers generally want you to deal with similar objects: you can combine strings (words can become sentences) or add numbers, but you trying to combine a string and an integer will break things.

But notice that my beginning answer hinged on the ambiguity between strings and integers. How does a computer know whether we are talking about strings or about integers in cases where they could refer to either? How does it now that I want 8 to function as a word and not as a number in this context?

Programmers over the years have built a variety of functions and tools into different languages to get around some of these difficulties, but they still remain. When processing text by a computer, we have to account for such problems. We generally do this by following very strict guidelines for inputting information. This **syntax** works in much the same way as grammar does for humans - helping the computer to keep track of what we mean and what we want it to do. 

In this case, we can tell something is a string or not by the presence or absence of quotation marks:

8 vs "8"

The computer looks at those quotation marks and can intuit the difference in datatypes: 

integer vs string

Programming and text analysis more generally are built on such subtle distinctions. A computer needs to have its hand held in order to recognize difference and similarity. To a computer, the following are entirely unrelated:

8 ≠ "8" ≠ "Eight" ≠ "Eighth"
The computer would not recognize the relationships among those four clearly related words. It goes even further: computers think of lowercase and capital letters as different characters entirely. 

"H" ≠ "h"

These differences can be extremely frustrating when just beginning to practice text analysis, but don't worry: you don't have to reinvent the wheel. You benefit from years of programmers developing ways to account for these things. In any programming context, you probably have access to a range of utilities to capitalize things, lowercase them, convert integers to strings, convert date timestamps into words, etc. 

But there are advantages to these rigid restrictions. By following them, we can get very detailed information about texts that we might otherwise gloss over. The first part of any text analysis project involves converting complex language into organized data that the computer can understand. 

"This is a sentence" ≠ "This" "is" "a" "sentence"

A computer would not recognize these two terms as being equal. The left side, after all, contains spaces, and the right side contains a series of smaller strings. Annoying? Maybe. But also useful! After all, we are rarely interested in whole sentences. We commonly refer to individual words as **tokens**, and the process of breaking sentences into words then becomes called **tokenization**. While we often care about how many times each particular token occurs, we might care about not so much about the numbers of each different word so much as the different kinds of words themselves. So rather than counting all words, we just want to grab an example of each token **type**. If we have the following document:

> Test test test sentence sentence

We have five tokens and two types. Depending on our research questions and interests, statistics like these can help tell us about what the document discusses as well as how it is being discussed.

If sentences are broken up into words, we might care also about breaking documents into sentences first. We have a name for that too: **segmentation**.

> "But wait," you say, "computers care about capitalization. So if I tokenize a text and try to compare 'word' and 'Word' it will think they are entirely different things!" 

Good catch! You're right, those differences in capitalization often aren't meaningful. It is a fairly common practice to lowercase all the words after you tokenize them. This process is often called **normalizing** the data, since we are smoothing out inconsistencies that might get in the way of our research questions. This whole collection of processes of segmentation, tokenization, and normalization has name as well: **preprocessing**, all those things you do to data before you work with it. Depending on your interests, you might include other steps, such as tagging things for parts of speech or filtering out particular types of words.

Textual data is messy, and it requires a lot of work to convert it into usable material. But once you get a handle on the fixed set of methods for doing so, a whole world of possibility opens up. After all, the internet is *filled* with unstructured textual data, and we could learn a lot about our world by analyzing it to better understand things. This field of study is referred to as **natural language processing**, and a wide range of careers are built upon these foundations. From the sciences, medicine, government, and many more, the world needs people able to make sense of our textual world. You could be one of them.
