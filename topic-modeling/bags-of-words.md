# Bags of Words

When we read, our eyes move in sequence across the page and take in phrase after phrase in the order in which they were intended. This sense of chronology integral to how we, as human readers, understand texts. But it is possible to imagine other ways of reading. Have you ever skimmed over a page backwards looking at every other word? You probably still got the gist of the text even though you didn't read in order, even though you missed many of the words.

Take this passage:

> I will, for the sake of argument, assume that the information given to the coroner by the officer of one of the medical schools is correct, and that Dr. Phillips is right in considering that the character of the mutilation in question justifies the assumption that the perpetrator was probably one who possessed some knowledge of anatomy. But that the inference which has been deduced is warranted, any one who is the least acquainted with medical science and practice will unhesitatingly deny and indignantly repudiate. That a lunatic may have desired to obtain possession of certain organs for some insane purpose is very possible, and the theory of the murdering fiend being a madman only derives confirmation from the information obtained by the coroner. But that the parts of the body carried off were wanted for any quasi scientific publication, or any other more or less legitimate purpose, no one having any knowledge of medical science will for a moment believe. 

The excerpt is from a letter about the Jack the Ripper murders from the *Pall Mall Gazette* published on September 28, 1888. Even without knowing anything about the context, you can probably infer rough senses of the topic of the text: murder. We might further say that there are a number of overlapping in the text: evidence, medicine, murder, and many more. But how did you know this? Besides reading the whole text, you could probably skim and get a sense from certain words that strongly indicate these topics to you. Here is the same passage with one representation of how reading might have taken place for you using *[Prism](https://prism.scholarslab.org)*. We have highlighted various words associated with particular categories as such:

```
Highlight Color: Topic
---
red: evidence
green: medicine
blue: murder
```

![topic modeling highlights](/assets/topic-modeling/topic-modeling-highlights.jpg)

When you read at a glance, you probably intuit the presence of such words as indicative of the topic in a text. We might further abstract this outwards to say that each of these topics represents a different kind of discourse at work in the text. In any given conversation about medicine, certain words are more likely to occur than others. The word 'lunatic' might appear in such a conversation, but it is far more likely that a word like 'anatomy' would suggest you are in a conversation about medicine. So each text is made up of some mix of discourses like these; each text is the result of some number of topics, of some number of discourses. Here we started with a few topics and then located words that supported our sense that they appeared in the text. But wouldn't it be interesting if we could somehow see the whole web of topics that occur in a text?

We are beginning to float a different kind of reading. Let's take one more step back. 

If we take the words in a text as being indicative of its underlying topics, we actually don't need to worry about word order so much. We just care about whether the words are there or not, not the order they come in. Our previous examples have preserved the sense of narrative time in a text - when we counted words with *Voyant*, we then graphed them over time. But we can find out interesting things about texts if we are a little more flexible if we think about them not as things that unfold over time but rather as pure token counts, as **bags of words**. In a bag of words model, word order becomes irrelevant. All we care about is what words occur and how often they do so. Pretty straight forward, right?

Take the following two sentences:

"Fine. How are you doing?"
"How are you doing? Fine?"

If we normalize them and remove stopwords, we lowercase them and get rid of punctuation. A bag of words model of each text would be the same:

```
[
    "fine", 
    "how", 
    "are", 
    "you", 
    "doing"
]
```

A bag of words model generates a list of words that occur in the corpus as a whole, and then how often. So a bag of words model for the following two sentences might produce something like the following:

Sentence 1: "Barbara is doing fine, thank you."
Sentence 2: "Thank you, Dave. I am doing fine."

```
Words
[
    "Barbara",
    "is",
    "doing",
    "fine",
    "thank",
    "you",
    "Dave,
    "I",
    "am"
]

Sentence 1
[1, 1, 1, 1, 1, 1, 0, 0, 0]
Sentence 2
[0, 0, 1, 1, 1, 1, 1, 1, 1]
```
In addition to the list of the total words in all our documents, we also have two lists, one for each sentence, of the number of times each of those terms occur. 
You might feel like this goes against everything that you've ever known about reading. This might feel like destroying a text. You're not wrong. This concept is pretty far removed from how we tend to read, since we tend to read in sequence across the page. This approach, instead, wants you to think about reading in a different way, to develop a new epistemology for the process. We lose something in the process, the sense of a text as it unfolds over time. 

But we also gain the ability to think about a text in new ways. If we can 