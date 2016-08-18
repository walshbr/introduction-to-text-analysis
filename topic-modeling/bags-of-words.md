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

We might further abstract this outwards to say that 

> How does this work?

Our previous examples have preserved the sense of narrative time in a text - when we counted words with *Voyant*, we then graphed them over time. But we can find out interesting things about texts if we are a little more flexible if we think about them not as things that unfold over time but rather as **bags of words**. In a bag of words model, word order becomes irrelevant. Take the following two sentences:

"Fine. How are you doing?"
"How are you doing? Fine?"

If we remove normalize them and remove stopwords, we lowercase them and get rid of punctuation. A bag of words model of each text would be the same:

```
[
    "fine", 
    "how", 
    "are", 
    "you", 
    "doing"
]
```

A bag of words model generates a list of words that occur in the corpus as a whole, and then often.

This concept is pretty far removed from how we tend to read, since we tend read in sequence across the page. Topic modeling, instead, wants you to think about reading in a different way. It wants you to think through a different epistemology of reading. 

Topic modeling 

**Latent Dirichlet Allocation (LDA)**

not dependent on location - just looking at all the different words that show up in a document.

The topic modeling algorithm looks for statistically significant clusters of words. For each document in your corpus, it will look 

We call this an **unsupervised classifier** because we are asking the computer to analyze and mark a text without giving it any clear directions. We just say, "here is some text. Do your thing and tell me what you find." A **supervised classifier** would take information from us to help it make decisions. We might say, "read this text. If it has more than fifty uses of the word 'crime' mark it as 'detective fiction.' If it has fifty uses of the word 'sex,' mark it as 'romance.'

Until now, we have stressed approaching text analysis with a clear sense of your interests and the research questions that drive them. Topic modeling works a little differently: it is more useful for exploratory work.

So you've topic modeled! The results are…confusing. Let's take a look at them.