# Bags of Words

When we read, our eyes move in sequence across the page and take in phrase after phrase in the order in which they were intended. This sense of chronology integral to how we, as human readers, understand texts. But it is possible to imagine other ways of reading. Have you ever skimmed over a page backwards looking at every other word? You probably still got the gist of the text even though you didn't read in order, even though you missed many of the words.

Take this letter from the *Pall Mall Gazette* published on September 28, 1888:



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