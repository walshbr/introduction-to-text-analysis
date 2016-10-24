# How Computers Read Texts

If you have been dutifuly following along until now, it should be clear that computers and humans don't think the same way.  With respect to text analysis, we can say that computers and humans have complementary skills. Computers are good at doing things that would take us a long time to do or that would be incredibly tedious. Computers can easily count and compare and will do so for pretty much as long as you tell them to do so. In contrast, humans are very good at understanding nuance and context. Thus, you wouldn't want a computer to do any close reading, or unpack the claims of a primary or secondary text; this is something you are far better at. By the same token, it's probably easier to have a computer list all the numbers between one and 45678987 than to do it yourself.

If such a disparity in skills exists between you and computers, you may be wondering why we're teaching a class on digital text analysis. Why bring technology into the equation when it is a poor approximation for a lot of the things that we do when we read? The answer is that there are a lot of instances where you can combine the nuance of human thinking with the quantitative power of computers to look at texts in new and creative ways. In particular, you can make computers do a lot of the repetitive work that you might find tedious.

To do so, though, you need to know a bit about how computers process texts. In many ways, they have a hard time understanding data. They can interact with and use information, but they make very few assumptions and even fewer interpretations about what they're working with. Any interpretative abilities that they do have been specifically programmed into the computer's software. So what follows, then, is a lesson in not taking anything for granted.

In the context of text analysis, all of this means that computers do not read with the same ease that we do. Consider the following sentence:

"We saw 8<sup>1/2</sup>."

Taken alone, the sentence doesn't tell us much. Its meaning depends a lot on the question to which we might be responding, and we can think of two possible questions with very different contexts:

> "How many movies did you see?

> "What movie did you see?"

In the first case, we might be responding with the number of movies that we had seen. It was a slow weekend, and we spent it at the local movie theatre hopping from film to film. It was a great time! In the second situation, we might be responding with the title of a specific film, [*8<sup>1/2</sup>* by Italian director Frederico Fellini](https://en.wikipedia.org/wiki/8%C2%BD). So one answer is a number, and one answer is a name. Since humans are good at grasping context, we would easily be able to distinguish between the two. In most situations, we would just adjust our understanding internally before moving on with the conversation. 

Computers cannot make inferences like these, and this fact has serious implications: numbers and words have significantly different uses. Here are two further extensions of the conversation:

> If you add four to how many movies you saw, what is the result?

If we were talking about a number of movies, my response would clearly be, "Oh that's 12.5. Why are you giving me a math quiz?" If we were talking about the Fellini film, we might respond, "What? Oh, we were talking about a title, not a number. We can't add things to a title." Again, humans have the ability to respond to context, infer, and adapt. Computers aren't nearly as flexible: they need to know ahead of time, in most cases, what kind of information they are dealing with. That way they can act as you anticipated.

Programmers have developed conventions for telling computers to distinguish between these different kinds of information, or **data types**. The distinction we outline above contains the two most important ones for our purposes here:

* **Strings**: characters, the stuff of words

* **Integers**: a whole numbers

The misunderstanding about films depends on a confusion around data types like these. If you go on to learn how to program, you might find slightly different names depending on the programming language, and you will be introduced to other data types as well. But the distinction between strings and integers is important for text analysis. You can perform arithmetic operations on integers while strings respond less well to such things. You can capitalize words, but not numbers. And computers generally want you to deal with similar objects: you can combine strings (words can become sentences) or add numbers, but trying to combine a string and an integer will break things. 

But notice that our beginning scenario hinged on the ambiguity between strings and integers. How does a computer know whether we are talking about strings or about integers in cases where they could refer to either? How does it know that we want 8 to function as a word and not as a number in this context?

Programmers over the years have built a variety of functions and tools into different languages to get around some of these difficulties, but they still remain. When processing text by a computer, we have to account for such problems. We generally do this by following very strict guidelines for inputting information. This **syntax** works in much the same way as grammar does for humans - helping the computer to keep track of what we mean and what we want it to do. 

In this case, we can tell the computer that something is a string or not by the presence or absence of quotation marks:

* 8 vs "8"

The computer looks at those quotation marks and can intuit the difference in datatypes: 

* A number without quotation marks? That's an integer. 
* Ah quotation marks. That means I'm looking at a string.

Programming and text analysis more generally are built on such subtle distinctions. A computer needs to have its hand held in order to recognize difference and similarity. To a computer, the following are entirely unrelated:

* 8 ≠ "8" ≠ "Eight" ≠ "Eighth"

The computer would not recognize the relationships among those four clearly related words. It goes even further: computers think of lowercase and capital letters as different characters entirely. 

"H" ≠ "h"

These differences can be extremely frustrating when you are beginning to practice text analysis, but don't worry: you don't have to reinvent the wheel. You benefit from years of programmers developing ways to account for these things. In any programming context, you probably have access to a range of utilities to capitalize things, lowercase them, convert integers to strings, convert date timestamps into words, etc. What this means is that sometime, years ago, someone first invented that wheel for you. A diligent programmer came along and told the computer that "h" and "H" have a special relationship along with how to navigate that link. You can benefit from their work.

But there are advantages to these rigid restrictions. By following them, we can get very detailed information about texts that we might otherwise gloss over. The first part of any text analysis project involves converting complex language into organized data that the computer can understand. This first step involves smoothing out problematic bits and filling in any gaps, all with an eye to the issues outlined above and in the chapter on "[Data Cleaning](/data-cleaning.md)."

"This is a sentence" ≠ "This" "is" "a" "sentence"

A computer would not recognize the two sides of the equals sign as being equivalent. The left side, after all, contains spaces, and the right side contains a series of smaller strings, since each word is in quotation marks. Annoying? Maybe. But also useful! After all, we are rarely interested in whole sentences. We commonly refer to individual words as **tokens**, and the process of breaking sentences into words then becomes called **tokenization**. This allows us to structure our text into a collection of pieces that we can manipulate more easily. Tokenization almost always breaks apart punctuation from words. So "I heard him!" would become "I", "heard", "him", "!". Punctuation tokens may or not be thrown away, depending on whether they are tokens that you care about.

We can break things down even further once we've divided a text into individual words. While we often care about how many times each particular token or word occurs, we might also care about the different kinds of words. We might want to keep track, on the one hand, of all the different words in a text regardless of how often they occur. But we might also want a different kind of vocabulary list. Rather than counting all the words, we might just want to grab a single example of each token **type**. If we have the following document:

> Test test test sentence sentence

We have five tokens and two types ('test' and 'sentence'). A list of types might be good for getting a sense of the kinds of language used in a text, while a raw list of tokens could be useful for figuring out what kinds of words occur in which proportions. Depending on our research questions and interests, statistics like these can help us figure out what the document discusses as well as how it is being discussed.

If sentences are broken up into words, we might care also about breaking documents into sentences first. We have a name for that too: **segmentation**.

> "But wait," you say, "computers care about capitalization. So if we tokenize a text and try to compare 'word' and 'Word' they will think they are entirely different things!" 

Good catch! You're right, those differences in capitalization often aren't meaningful. It is a fairly common practice to lowercase all the words after you tokenize them. This process is often called **normalizing** the data, since we are smoothing out inconsistencies that might get in the way of our research questions. This whole collection of processes of segmentation, tokenization, and normalization has a name of its own as well: **preprocessing**, all those things you do to data before you work with it. Depending on your interests, you might include other steps, such as tagging tokens for parts of speech or filtering out particular types of words. Note that preprocessing can change your list of types. A computer would not recognize "Said" and "said" as being of the same type, but, if you normalize capitalization so that every token is lowercased, a computer would see them as the same word. So you often need to decide what pieces you care about at the beginning of the process.

Textual data is messy, and it requires a lot of work to convert it into usable material. Very often, the process involves even more steps than those that we outline here. But once you get a handle on the fixed set of methods for doing so, a whole world of possibility opens up. After all, the internet is *filled* with unstructured textual data, and we could learn a lot about our world by analyzing it. This field of study is referred to as **natural language processing** ("natural language" refers to human languages like English, French, Arabic or Chinese, as opposed to computer languages, which were invented). A wide range of careers are built upon these foundations in fields in the sciences, medicine, government, and many more. The world needs people who can make sense of our textual world. You could be one of them.
