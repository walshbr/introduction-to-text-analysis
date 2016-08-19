# Topic Modeling Case Studies

In the previous section, we described how a single text could be broken up into a list of word frequencies, and we also suggested a single text might be composed of any number of discourses or topics. The different words in a text draw from these topics, so, given lists of word frequencies, we can infer the underlying topics. This process is called **topic modeling**, a machine learning technique that allows you to discover the topics that construct a text. Topic modeling does so by exercising a variety of statistical protocols over and over again. Executing topic modeling projects yourself takes more hands-on programming than we want to introduce in this coursebook. So instead of exercising the techniques themselves or offering a tool for doing so, we are going to attempt to describe what topic modeling is and how to interpret results from it using a case study. Come talk to either of us in person if you want to go further and explore topic modeling on your own.

We began by walking through a paragraph and suggesting that by skimming it you can infer the types of topics that a paragraph deals with. Topic modeling works in a similar way: the software looks for words that tend to occur next to each in statistically significant ways. As humans, though, we have an upper limit to how much we can hold in our head to compare to each other: a few topics, a few texts. A computer doesn't have that same problem. Topic modeling software can process hundreds of thousands of texts. Over and over again. refining its sense of how all the pieces fit together. 

So when you run topic modeling software, it looks for words that occur near each other in texts in meaningful ways over the course of the corpus. In most cases, it looks for words the occur in documents together. But you might occassionally **chunk** larger documents into a series of paragraphs so that the software thinks about them each as separate documents for finer granularity.

After running over the whole corpus, the results of topic modeling will look something like this:


The program spits out a series of topics, each of which consists of a series of words that tend to occur in documents together with statistical significance. You can think of these as the latent topics or discourses that contribute vocabulary to a document. Notice that the computer does not know anything about these topics at all. The real work of topic modeling involves interpreting these topics in ways to make them meaningful to readers. Take

We will do a lot of statistical handwaving in what follows, but have some extra resources at the bottom of the page if you are interested in learning more about the mechanics of how topic modeling works.



as Andrew Goldstone and Ted Underwood put it in their article on topic modeling *[PMLA](https://andrewgoldstone.com/blog/2012/12/13/pmla/)*, "a 'topic' is neither more nor less than a pattern of co-occurring words"



not dependent on location - just looking at all the different words that show up in a document.



The topic modeling algorithm looks for statistically significant clusters of words. For each document in your corpus, it will look


talk about topic weighting. link to 

http://www.scottbot.net/HIAL/index.html@p=221.html



We call this an **unsupervised classifier** because we are asking the computer to analyze and mark a text without giving it any clear directions. We just say, "here is some text. Do your thing and tell me what you find." A **supervised classifier** would take information from us to help it make decisions. We might say, "read this text. If it has more than fifty uses of the word 'crime' mark it as 'detective fiction.' If it has fifty uses of the word 'sex,' mark it as 'romance' (more on supervised classifieres in the next chapter). Unsupervised classifiers like topic modeling instead no very little about the underlying texts that they are examining. Instead, they process them based on an underlying model.

In the last lesson we called the **bag of words** model an epistimelogy of texts, a way of understanding texts that might be different from what you were familiar with. In the case of the kind of topic modeling we have been discussing, that model could further be called **Latent Dirichlet Allocation (LDA)**. We won't go into too much detail about the specifics of LDA, but it is important to know that this is the model you are working with. LDA is a model that assumes that there are a text is constructed from a small number of topics.

# How to interpret

Until now, we have stressed approaching text analysis with a clear sense of your interests and the research questions that drive them. Topic modeling works a little differently: it is more useful for exploratory work.






So you've topic modeled! The results are…confusing. Let's take a look at them.




