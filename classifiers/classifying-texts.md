# Classifying Texts

"Supervised classification is all well and good, but how does this relate to text analysis? I'm going to go back to googling for animal photos."

Stop right there! We've got one for you:

![non-diegetic owl photo](/assets/classifiers/owl.jpg)

Now that you're book and not going anywhere, your point is a good one. We wanted to stay relatively simple so that you could get a handle on the basics of supervised classification, but let's think about the ways you could apply this method to texts. The [NLTK book](http://www.nltk.org/book/ch06.html)
 lists some common text classification tasks:

> * Deciding whether an email is spam or not.
> * Deciding what the topic of a news article is, from a fixed list of topic areas such as "sports," "technology," and "politics."
> * Deciding whether a given occurrence of the word bank is used to refer to a river bank, a financial institution, the act of tilting to the side, or the act of depositing something in a financial institution.

Remember, a supervised classifier relies on labeled data for a training set. You have to give it lots of example data. Let's break each of these tasks down. You could work backwards, and figure out what kind of training data you would need from the question you are interested in:

* To decide whether an email is spam, you will need lots of examples of junk email.
* To tag a news article as belonging to a particular category, you will need examples of articles from each of those categories.
* To determine the use of the word 'bank', you will need examples of it used in all possible contexts. 

In each case, it's not enough to just dump data at the classifier. You would also have to decide what feature sets you want to use for each task. Take the task of building a spam filter. To determine whether or not a text is spam, you would need to decide what features you find to be indicative of junk mail. And you have many options! Here are just a few:

* You might decide that word choice is indicative of spam: "Buy now! Click this link to see an urgent message!". So you'd need to break up your representative spam texts into tokenized lists of vocabulary and work from there to give the classifier a sense of those words likely to result in unwanted messages.
* You might notice that all your spam notifications come from similar emails. You could train the classifier to identify certain email addresses, pull out those which have known spam addresses, and tag them as spam.

You could certainly come up with others. In any case, you would need to take a large question and break it down into smaller steps. 

For now, let's consider a supervised approach to a common problem in text analysis: authorship attribution.

[http:\/\/aicbt.com\/authorship-attribution\/online-software\/](http://aicbt.com/authorship-attribution/online-software/)

More technical version here - [http:\/\/www.aicbt.com\/authorship-attribution\/](http://www.aicbt.com/authorship-attribution/)

