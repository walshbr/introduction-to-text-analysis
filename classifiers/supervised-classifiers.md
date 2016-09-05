# Supervised Classifiers

In the lesson on our [Topic Modeling Case Study](/topic-modeling/topic-modeling-case-study.md), we talked about unsupervised classifiers. That is to say that when topic modeling explores texts to find the underlying discourses at work within them, our texts were not really labeled in any way. We did not say, "topic modeler, go out and search for a topic called, 'medicine.' A medicine topic will consist primarily of the words 'anatomy,' 'science,' 'hospital,' etc. Let me know what else you find!" Instead, the topic modeling software came up with groups of words that it thought were related with relatively little input from us. This has the advantage of showing us patterns that we might not even know are there. Topic modeling is useful for exploring a corpus and discovering new things about it.

You could maybe think of unsupervised classifiers as a kind of roomba. You hit a button, and the tiny little robot dutifully goes out and starts cleaning your floor. It knows when it reaches walls and corners that it should try to scoot around them. And its cleaning brushes are spinning furiously the whole time. You haven't told the machine how to clean, or how to navigate your floor. You just push the button and trust that it has inherent assumptions and protocols that it will follow. That covers the unsupervised part, but an unsupervised _classifier_ is obviously more sophisticated and different. Instead of cleaning your floor, topic modeling uses statistics to sort the words in your texts in such a way that you can get a sense of underlying patterns in word usage.

Let's try another example, whose spiritual origin is in Lisa Rhody's [farmers' market game](https://github.com/lmrhody/topicmodelgame) that teaches topic modeling. Imagine you have a bag with apples, oranges, and bananas in it. Imagine you also don't have any idea what an apple, an orange, or a banana is. Now we tell you to sort the things in the bag. You can still sort them, and you would do so by creating three piles. You take the first item, and place it into a pile on its own. Pull out a second item. Does it look similar to the first? No? Gets a new pile. Third item? Looks like the first one, so it goes next to that one. Each time you pull a new item, you compare it to all the others and revise your piles accordingly. At the end, you'll have three different piles, organized by fruit. But you didn't know anything about those fruits ahead of time.

Now imagine, instead, that we give you a slightly different exercise. We give you a bag filled with dragon fruit, star fruit, and durian. Imagine that you don't know anything about these fruits. We say, "find me all the durian." If you don't know anything about durian, you won't be able to do so. So first we bring in ten examples of durian for you to study. We say, "Look at them. Study them. Pay attention to these characteristics: they have spikes, they are big, and they are yellow-ish." We might also give you several examples of non-durian fruit so that you can get a sense of what durian don't look like. This set of fruit, where we tell you the correct labels for the fruit, is called our **training set**. Now, you pull a fruit. No spikes. So you start a pile called not durian. The next one has spikes. Durian! You keep going until you have two piles, ones that you think are durian and ones that are not.

This kind of classification is called **supervised classification**. You had to be taught what the durian looked like before you could really do anything. We would call these a feature set, and it might look something like this:

```
feature_set = {
'has_spikes': True,
'size': 'big',
'color': 'yellow-ish'
}
```

Don't worry too much about the brackets, equals sign, etc. These are just a common way of organizing the information so that the computer can read them. Here, we're just saying that to belong the feature set, the fruit has to have spikes, be large and yellow-ish. This allows us to make a reasonable guess as to whether or not any one piece of fruit we pulled out of the bag was a durian. Notice how you can only work in binaries: the fruit is either a durian or not. Your not-durian pile had star fruit and dragon fruit in it, since you weren't really able to distinguish between the two in this thought experiment. We could only answer something like the following if we looked at star fruit:

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

So we have been developing a series of tests for fruit types, but they might not be perfectly correct: after all, there are other fruits that are large, spikey and yellow-ish. A kiwano melon could have gotten thrown into the mix, and you might have incorrectly identified it as a durian. Or you might have gotten an unripe \(green\) durian, which you incorrectly tossed in the wrong pile. So we could better characterize our two piles as "probably not durian" and "probably durian."

Likewise, maybe you want to figure out a classification system to sort bagels. So you ask: is it round? Yes. Then it's a bagel. Does it have black dots? Then it's a poppy-seed bagel. Does it have white dots? Then it's a sesame-seed bagel. Neither one? Mainly one color? Then it's a plain bagel.

![bagel dog](/assets/bagel2.jpg)

Only this dog fits all the criteria for a plain bagel, but is definitely not a bagel. Our classifier can say, at best, "probably bagel" or "probably not bagel." But sometimes it's wrong. Sometimes life gives you a dog, and all you can see is a bagel. \(You go [here](http://www.boredpanda.com/dog-food-comparison-bagel-muffin-lookalike-teenybiscuit-karen-zack/) for more on this classification problem.\)

The use of the word "probably" should be a clue here - we have drifted into probability and statistics. What we have developed above are very basic **naive Bayes classifiers**. Thomas Bayes was an eighteenth-century statistician, and this classifier relies on his underlying [theory of statistics](https://en.wikipedia.org/wiki/Bayesian_statistics). There are other types of classifiers, but this kind assumes that each feature \(size, color, spikiness in the fruit example; shape and dotted-ness in the bagel example\) in our feature set will have some say in determining how to classify something that is unknown.

In the fruit example, the classifier combines these likelihoods with the total number of times that durian actually occurred in our example set of fruit to determine the probability of each label. In this case, our labels are durian or not-durian, true or false, though you could have more than just two labels. The classifier then picks the label with the highest likelihood. We have trained ourselves to classify fruit, and we could replicate that same process on durian at a later date. If a master fruit vendor comes along, he could probably tell us how accurate we were. We could then compare our accuracy to another person trained to classify fruit, and we could figure out who is the better classifier.

This might all seem a bit removed from the kinds of work that we have been doing elsewhere in the book, but we wanted you to get a firm foundation in what classification is before we modeled an example relative to text analysis.

## Further Resources

* The NLTK book has [a good section](http://www.nltk.org/book/ch06.html#naive-bayes-classifiers) on naive Bayes classifiers. The book is a Python tutorial, though, so it will quickly get technical.

* [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)


