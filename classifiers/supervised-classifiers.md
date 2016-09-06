# Supervised Classifiers

In the lesson on our [Topic Modeling Case Study](/topic-modeling/topic-modeling-case-study.md), we talked about unsupervised classifiers. When topic modeling explores texts to find the underlying discourses at work within them, our texts were not really labeled in any way. We did not say, "topic modeler, go out and search for a topic called, 'medicine.' A medicine topic will consist primarily of the words 'anatomy,' 'science,' 'hospital,' etc. Let me know what else you find!" Instead, the topic modeling software came up with groups of words that it thought were related with relatively little input from us. This has the advantage of showing us patterns that we might not even know are there. Topic modeling is useful for exploring a corpus and discovering new things about it.

You could think of unsupervised classifiers as similar to a [roomba](https://www.youtube.com/watch?v=A0Z79ycisDU). You hit a button, and the tiny little robot dutifully goes out and starts cleaning your floor. It knows when it reaches walls and corners that it should try to scoot around them. And its cleaning brushes are spinning furiously the whole time. You haven't told the machine how to clean, or how to navigate your floor. You just push the button and trust that it has inherent assumptions and protocols that it will follow. That covers the unsupervised part, but an unsupervised _classifier_ is obviously more sophisticated and different in kind. Instead of cleaning your floor, topic modeling uses statistics to sort the words in your texts in such a way that you can get a sense of underlying patterns in word usage.

Let's try another example, adapted from Lisa Rhody's [farmers' market game](https://github.com/lmrhody/topicmodelgame) that teaches topic modeling. Imagine you have a bag with apples, oranges, and bananas in it. Imagine you also don't have any idea what an apple, an orange, or a banana is. Now we tell you to sort the things in the bag. You can probably still sort the fruit even without knowing anything about them, and you would do so by creating three piles. You take the first item, and place it into a pile on its own. Pull out a second item. Does it look similar to the first? No? Gets a new pile. Third item? Looks like the first one, so it goes next to that one. Each time you pull a new item, you compare it to all the others and revise your piles accordingly. At the end, you'll have three different piles, organized by fruit. But you didn't know anything about those fruits ahead of time. Topic modeling employs a few other variables in the process, so check out Rhody's lesson to learn more. For now, we will move on. 

Now imagine, instead, that we give you a slightly different exercise. We give you a bag filled with dragon fruit, star fruit, and durian. Imagine that you don't know anything about these fruits. We say, "find me all the durian." You could sort the fruit into piles all day long, but, if you don't know anything about durian, you won't be able to pick out the fruit you need. So we give you a little **training** by first bringing in ten examples of durian for you to study. We say, "Look at them. Study them. Pay attention to these characteristics: durian have spikes, they are big, and they are yellow-ish." We might also give you several examples of non-durian fruit so that you can get a sense of what durian doesn't look like. This set of fruit, where we tell you the correct labels for the fruit, is called our **training set**. Now, you have something to work with! You pull a fruit. No spikes. So you start a pile called not durian. The next one has spikes. Durian! You keep going until you have two piles, one that contains fruit that you think is a durian and one that contains fruit that you think are not.

This kind of classification is called **supervised classification**. You had to be taught what the characteristics of a durian were before you could really do anything. We would call this collection of traits a **feature set**, and it might look something like this:

```
feature_set = {
'has_spikes': True,
'size': 'big',
'color': 'yellow-ish'
}
```

Don't worry too much about the brackets, equals sign, etc. These are just a common way of organizing the information so that the computer can read them. Here, we're just saying that this feature set defines what a durian looks like: the fruit has to have spikes, be large, and yellow-ish. This allows us to make a reasonable guess as to whether or not any one piece of fruit we pull out of the bag was a durian. Notice how you can only work in binaries: the fruit is either a durian or not. Your not-durian pile had star fruit and dragon fruit in it, since you weren't really able to distinguish between the two in this thought experiment. If we pulled out a star fruit, we could only answer something like the following:

```
fruit.is_durian?
>>> False
```

Or this if we were looking at a durian:

```
fruit.is_durian?
>>> True
```

The test is actually pretty simple in its results, even if the feature set that leads to them is more nuanced. True and False are referred to as **boolean data types** in programming, and these boolean values are used to test or represent whether something is just that - true or false.

We have been developing a series of tests for fruit types, but they might not be perfectly correct: after all, there are other fruits that are large, spikey and yellow-ish. A kiwano melon could have gotten thrown into the mix, and you might have incorrectly identified it as a durian. Or you might have gotten an unripe durian, which you incorrectly tossed in the wrong pile because it was green. So we could better characterize our two piles as "probably not durian" and "probably durian."

Likewise, maybe you want to figure out a classification system to sort bagels. So you ask: is it round? Yes. Then it's a bagel. Does it have black dots? Then it's a poppy-seed bagel. Does it have white dots? Then it's a sesame-seed bagel. Neither one? Mainly light brown in color? Then it's a plain bagel.

![bagel dog](/assets/bagel2.jpg)

But wait: this dog fits all the criteria for a plain bagel, and it is definitely not a bagel. Our classifier can say, at best, "probably bagel" or "probably not bagel." And sometimes it's wrong. Sometimes life gives you a dog, and all you can see is a bagel. \(Go [here](http://www.boredpanda.com/dog-food-comparison-bagel-muffin-lookalike-teenybiscuit-karen-zack/) for more on this classification problem.\)

The use of the word "probably" should be a clue here - we have drifted into probability and statistics. What we have developed above are very basic **naive Bayes classifiers**. Thomas Bayes was an eighteenth-century statistician, and this classifier relies on his underlying [theory of statistics](https://en.wikipedia.org/wiki/Bayesian_statistics). There are other types of classifiers, but this kind assumes that each feature \(size, color, spikiness in the fruit example; shape and dotted-ness in the bagel example\) in our feature set will have some say in determining how to classify something that is unknown.

In a real-world situation, we probably would have given you negative examples as well, examples of fruit that are not durian so that you had a more nuanced sense of what you were studying. In the case of a naive Bayes classifier and our fruit example, the classifier takes the number of times that durian actually occurred in our training set as the **prior probability**. The classifier then combines this number with the actual features that we provided to give a weighted probability as to whether or not what it is looking at is a durian. 

In this case, our labels are durian or not-durian, true or false, though you could have more than just two labels. The classifier then picks the label with the highest likelihood. We have trained ourselves to classify fruit, and we could replicate that same process on durian at a later date. If a master fruit vendor comes along, she could probably tell us how accurate we were. We could then compare our accuracy to that of another person trained to classify fruit, and we could figure out who is the better classifier. We could even figure out the percentage of the time that each of our classification systems is likely to be correct!

This might all seem a bit removed from the kinds of work that we have been doing elsewhere in the book, but we wanted you to give a firm foundation in what classification is before we modeled an example relative to text analysis.

## Further Resources

* The NLTK book has [a good section](http://www.nltk.org/book/ch06.html#naive-bayes-classifiers) on naive Bayes classifiers. The book is a Python tutorial, though, so it will quickly get technical.

* [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) provides a very handy introduction to other types of classifiers.


