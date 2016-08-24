# Classifying Texts

At this point, you might be saying, "Supervised classification is all well and good, but how does this relate to text analysis? I'm going to go back to googling for animal photos."

Stop right there! We've got not one, but two for you:

![non-diegetic owl photo](/assets/classifiers/owl.jpg)

\(What do you think this owl thinks about supervised classifiers?\)

![sarah's sleeping dog](/assets/classifiers/sleepingstarbuck.jpg)

\(Or perhaps you feel like crawling under the covers and sleeping like this dog here.\)

Now that you're back and not going anywhere, your point is a good one. We wanted to stay relatively simple so that you could get a handle on the basics of supervised classification, but let's think about the ways you could apply this method to texts. The [NLTK book](http://www.nltk.org/book/ch06.html) \(which is a great one to check out if you want to go into more depth into text analysis\) lists some common text classification tasks:

> * Deciding whether an email is spam or not.
> * Deciding what the topic of a news article is, from a fixed list of topic areas such as "sports," "technology," and "politics."
> * Deciding whether a given occurrence of the word bank is used to refer to a river bank, a financial institution, the act of tilting to the side, or the act of depositing something in a financial institution.

Remember, a supervised classifier relies on labeled data for a training set. You have to give it lots of example data. Let's break each of these tasks down. You could work backwards, and figure out what kind of training data you would need from the question you are interested in:

* To decide whether an email is spam, you will need lots of examples of junk email.
* To tag a news article as belonging to a particular category, you will need examples of articles from each of those categories.
* To determine the use of the word 'bank', you will need examples of it used in all possible contexts. 

In each case, it's not enough to just dump data at the classifier. You would also have to decide what feature sets you want to examine for the training sets for each task. Take the task of building a spam filter. To determine whether or not a text is spam, you would need to decide what features you find to be indicative of junk mail. And you have many options! Here are just a few:

* You might decide that word choice is indicative of spam: "Buy now! Click this link to see an urgent message!". So you'd need to break up your representative spam texts into tokenized lists of vocabulary and work from there to give the classifier a sense of those words likely to result in unwanted messages.
* You might notice that all your spam notifications come from similar emails. You could train the classifier to identify certain email addresses, pull out those which have known spam addresses, and tag them as spam.

You could certainly come up with others. In any case, you would need to step through a series of questions common to all text analysis projects: 

* What is my research question?
* How can my large question be broken down into smaller pieces?
* Which of those can be measured by the computer?
* What kind of example data do I have that I can for this problem?

Going through these questions can be difficult at first, but, with practice, you will yourself able to separate feasible digital humanities questions from those that are impossible to answer. You will start to gain a sense of what could be measured and analyzed as well as whether or not you might want to do so at all.


Now, let's practice on a supervised approach to a common problem in text analysis: authorship attribution. Sometimes texts come down to us with no authors at all attributed to them. You could approach this in a variety of unsupervised ways, graphing the similarity or difference of particular authors based on a number of algorithms. But if you have a pretty good guess as to whom the author of a particular text might be, you can take a supervised approach to the problem. At other times, a single text might be written under a pseudonym, but you might have a good guess as to whom might be the author. To step through our same list of steps:

* What is my research question?
    * I want to be able to identify the unknown author of a text.

* How can my large question be broken down into smaller pieces?
    * I have a reasonable guess as to some possible authors, so I can use those as objects of study. I also am assuming that authorship can be associated with style.

* Which of those can be measured by the computer?
    * Well, style is the sum total of vocabulary, punctuation, and rhetorical patterns, among other things. Those can all be counted!

* What kind of example data do I have that I can for this problem?
    * I have the unknown text. And I also have several texts by my potential authors that I can compare against it.

To illustrate this experiment, I took two authors from our syllabus: Danielle Bowler and Pia Glenn. Using their author pages on [Eyewitness News](http://ewn.co.za/Contributors/Danielle-Bowler) and [xoJane](http://www.xojane.com/author/pia-glenn), I gathered articles that belonged to each. Bowler tends to write shorter pieces than Glenn, so my training set included about double the number of pieces by Bowler as by Glenn. With this body of training data for each author, I uploaded the texts to this great online [authorship attribution tool](http://aicbt.com/authorship-attribution/online-software/)
by AICBT. The tool allows you to upload sample data for two authors. With this set, you can then upload a text by an unknown author, and the software will try to guess who wrote it. In this case, the mystery text was [Freedom, Justice, and John Legend](http://ewn.co.za/2015/02/23/OPINION-Danielle-Bowler-Freedom-justice-and-John-Legend) by Bowler. Author 1 is Glenn, and Author 2 is Bowler. The tool attempted to identify the author of the mystery text as follows. You can also find AICBT's helpful explanation of the different metrics that they are using to analyze the unknown text.

![authorship function](/assets/classifiers/authorship-function.jpg)
![authorship lexical](/assets/classifiers/authorship-lexical.jpg)
![authorship diversity](/assets/classifiers/authorship-punctuation.jpg)

So looking at these measures, for a successful classifier we would want the arrow to point towards the right (this text is actually by author 2). You'll immediately see that we have some success, but also some failure! Function word analysis is a slight indicator of the correct author, lexical analysis is virtually useless, and punctuation analysis is way *wrong*. In a real classification project, we would want use the success or failure of our classifier to revise our sense of which features are useful for our particular project. In this case, punctuation is not a good measure at all, so we would throw that out. We might focus, instead, on function words as an indicator of authorship. We can tweak our approach accordingly.

Note how these measures of authorship overlap with other things we have studied in this book. Remember stopwords, those words that are so common in a text that they are frequently removed before text analysis? In cases, like this one, we might actually care a lot about those simple stopwords. Two of the three measures for authorship here deal with just those words that we might otherwise throw away: punctuation, articles, etc. These words might not tell you much about what a text talks about, but they can tell you an awful lot about *how* a text discusses them. 

You can carry this research process out by means of a variety of programming languages, so you might take a look at our concluding chapter on [Where to Go Next](/conclusion/where-to-go.md) if you are interested in learning how to implement these sorts of experiments yourself.