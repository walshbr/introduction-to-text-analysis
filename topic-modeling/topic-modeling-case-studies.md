Topic modeling looks for words that tend

as Andrew Goldstone and Ted Underwood put it in their article on topic modeling *[PMLA](https://andrewgoldstone.com/blog/2012/12/13/pmla/)*, "a 'topic' is neither more nor less than a pattern of co-occurring words"



**Latent Dirichlet Allocation (LDA)**



not dependent on location - just looking at all the different words that show up in a document.



The topic modeling algorithm looks for statistically significant clusters of words. For each document in your corpus, it will look



Until now, we have stressed approaching text analysis with a clear sense of your interests and the research questions that drive them. Topic modeling works a little differently: it is more useful for exploratory work.


We call this an **unsupervised classifier** because we are asking the computer to analyze and mark a text without giving it any clear directions. We just say, "here is some text. Do your thing and tell me what you find." A **supervised classifier** would take information from us to help it make decisions. We might say, "read this text. If it has more than fifty uses of the word 'crime' mark it as 'detective fiction.' If it has fifty uses of the word 'sex,' mark it as 'romance' (more on supervised classifieres in the next chapter). Unsupervised classifiers like topic modeling instead no very little about the underlying texts that they are examining. Instead, they process them based on an **algorithm**. An algorithm as [described by Bethany Nowviskie](http://nowviskie.org/2015/a-game-nonetheless/) is

> any effective procedure that pursues the solution of a problem by means of a predetermined sequence of actions, or steps.

In the last lesson we called the **bag of words** model an epistimelogy of texts, a way of understanding texts that might be different from what you were familiar with. You might think about an algorithm like an applied epistemology. We take this way of understanding texts and use it to produce some readings or results. We write a program that interacts with texts








So you've topic modeled! The results are…confusing. Let's take a look at them.




