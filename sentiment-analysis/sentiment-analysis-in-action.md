# Sentiment Analysis in Action

To illustrate how sentiment analysis works, let's walk through a couple different projects. We will do a fair amount of handwaving at technical details, but hopefully you will get a sense of the kind of work that goes into sentiment analysis projects.

## Jockers and Syuzhet

Matt Jockers uses a sophisticated software package that he constructed in the [R programming language](/conclusion/where-to-go.md). We won't get into the details of the code itself, but we can cover the general approach. To find a more technical explanation you can look at Jockers's "[Introduction to the Syuzhet Package](https://cran.r-project.org/web/packages/syuzhet/vignettes/syuzhet-vignette.html)".

Jockers's project combines supervised classifiers and unsupervised classifiers. Remember: supervised classifiers rely on training data that tells the software how to interpret and classify data. Unsupervised classifiers are not based on any prior training data. Instead, they rely on underlying assumptions and algorithms to categorize texts \(in the case of topic modeling, this means that the unsupervised classifiers make assumptions about the relation between texts and statistics\).

So, first, Jockers needed training data. In order to for his software to read sentiment in sentences, it needed example sentences that had already been marked for emotions. By providing the software with example sentences, the software will be able to categorize related sentences in the future. So imagine that we train our computer with these sentences:

1. "I am happy!", positive
2. "I am sad!", negative

Marking a given text for sentiment, then, imagine that the computer encounters sentence 1 again. The computer could look in its bank of knowledge and remember that it knows how it should be marked: positive. But this classifier would not work very well: it only knows the sentiment for two specific sentences. When it encounters new sentences that we haven't pre-marked, it would not know what to do! In practice, we want to train it on as much as data as possible to maximize its ability to handle new information. And we probably won't train it on full sentences. After all, computers distinguish between sentences and individual words in quite profound ways. Depending on how thorough we want to be, we might give the computer vocabulary and phrases marked for sentiment instead. And rather then a binary positive\/negative, we might mark for a continuum. After all, 'good' is less positive than 'exuberant'.

You can find information on the training sets used by Jockers [here](https://github.com/mjockers/syuzhet#references). He uses a training lexicon of his own but gives the option to categorize sentiment using other training sets. The software reads a text, looks at its memory of the training corpus to determine how positive or negative a sentence or word is, then converts the text into a series of values like this:

```
2.50 0.60 0.00 -0.25 0.00 0.00
```

Now the text is converted into a series of values that represent the sentiment of the text. As the numbers of the text becomes negative or positive, we get a sense of how the classifier reads the emotions of the text. From there, it is just a matter of plotting numbers to get a better representation of the sentiment trends over time, to get something like this, taken from Jockers's explanation of the software \(this is graph for James Joyce's _A Portrait of the Artist as a Young Man_\):

![plot trajectory in portrait](/assets/sentiment-analysis/jockers-portrait.jpg)

Measuring sentiment computationally in this way, at its core, relies on solid training data. The computer needs to learn how to map emotion-laden words and phrases onto some sort of numerical system. The robustness of your training set can strengthen or complicate your results. Getting a good training set can be difficult, however, since assembling them takes a great deal of time and labor. It takes a long time to manually label single words with positive or negative valence.

## EmojiSentiment

Another interesting use of sentiment analysis is [EmojiSentiment](http://www.emojisentiment.com/#About). The project approaches the problem from a different angle: rather than trying to analyze textual content for sentiment, the site postulates that emojis embedded in tweets might be a good predictor of their sentiment. There are only around 2000 emoji and only a small subset have emotional valences to them; tagging these emojis is a lot easier than tagging all the words that convey emotion. The authors of this project use emojis to determine the overall sentiment for particular hashtag, as opposed to any one tweet. So EmojiSentiment reads \#friday as being relatively positive:

![friday sentiment](/assets/sentiment-analysis/emoji-sentiment-friday.jpg)

The three most dominant emoji are fire, police sirens, and flowers, which might seem a bit unusual. Note that we're only getting 32 emoji in the last 1000 tweets - these might just be artifacts of whatever happens to be going right now, and the project can't handle more volume than that \(it's a student project. Yay students!\). If \#friday got a relatively happy average sentiment, \#angry is much more negative:

![angry sentiment](/assets/sentiment-analysis/emoji-sentiment-angry.jpg)

Note how even \#angry just barely dips below 50 to be predominantly negative. I actually had to search around for a while to find a hashtag that read as predominantly negative. Could this be a function of language - are people just happier than they are sad? Certainly not. This might have to do with how we represent our emotions on social media; maybe we just don't use emojis to represent negative emotions that often. Or maybe sentiment analysis by way of computation is imprecise at best.

> What might you imagine using sentiment analysis for?
> 
> What kinds of texts lend themselves especially well to reading for emotion?

