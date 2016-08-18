# Topic Modeling Case Studies

In the last lesson we discussed topics, discourses, and the bag of words model for reading texts. These are all backgrounds and framing contexts for **topic modeling**, a machine learning technique that allows you to discover the topics that construct a text. Executing topic modeling projects yourself takes more hands-on programming than we want to introduce in this coursebook. So instead of exercising the techniques themselves or offering a tool for doing so, we are going to attempt to describe what topic modeling is and how to interpret results from it using a case study. Come talk to either of us in person if you want to go further and explore topic modeling on your own.

Topic modeling looks for words that tend



as Andrew Goldstone and Ted Underwood put it in their article on topic modeling *[PMLA](https://andrewgoldstone.com/blog/2012/12/13/pmla/)*, "a 'topic' is neither more nor less than a pattern of co-occurring words"



not dependent on location - just looking at all the different words that show up in a document.



The topic modeling algorithm looks for statistically significant clusters of words. For each document in your corpus, it will look



We call this an **unsupervised classifier** because we are asking the computer to analyze and mark a text without giving it any clear directions. We just say, "here is some text. Do your thing and tell me what you find." A **supervised classifier** would take information from us to help it make decisions. We might say, "read this text. If it has more than fifty uses of the word 'crime' mark it as 'detective fiction.' If it has fifty uses of the word 'sex,' mark it as 'romance' (more on supervised classifieres in the next chapter). Unsupervised classifiers like topic modeling instead no very little about the underlying texts that they are examining. Instead, they process them based on an underlying model.

In the last lesson we called the **bag of words** model an epistimelogy of texts, a way of understanding texts that might be different from what you were familiar with. In the case of the kind of topic modeling we have been discussing, that model could further be called **Latent Dirichlet Allocation (LDA)**. We won't go into too much detail about the specifics of LDA, but it is important to know that this is the model you are working with. LDA is a model that assumes that there are a text is constructed from a small number of topics.

# How to interpret

Until now, we have stressed approaching text analysis with a clear sense of your interests and the research questions that drive them. Topic modeling works a little differently: it is more useful for exploratory work.






So you've topic modeled! The results are…confusing. Let's take a look at them.




