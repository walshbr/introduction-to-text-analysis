# Voyant Part One

We will be using a tool called [Voyant](http://voyant-tools.org/) to introduce some basic topics in text analysis using distant reading tools.

Upon arriving at Voyant you will encounter a space where you can upload texts. For the following graphs, we have uploaded the full text of _The String of Pearls_, the 1846-7 penny dreadful that featured Sweeney Todd, the demon barber of Fleet Street. Feel free to [download that dataset](/assets/the_string_of_pearls_full.txt) and use it to produce the same results for following along, or upload your own texts using the window provided.

![Voyant splash page and text uploader](/assets/voyant_splash_page.png)
After Voyant processes your text you'll get a series of window panes with lots of information. Voyant packages several features into one tight digital package: each pane offers you different means of interacting with the text.

![default view of string of pearls in voyant](/assets/voyant_overview.png)

Voyant gives you lots of options, so do not be overwhelmed. Voyant provides great documentation for working through their interface, and we will not rehearse them all again [here](http://docs.voyant-tools.org/start/). Instead, we will just focus on a few features. The top left pane may be the most familiar to you:

![voyant default wordcloud of string of pearls](/assets/voyant_word_cloud_default.png)
Word clouds like these have been made popular in recent years by [Wordle](http://www.wordle.net/). They do nothing more than count the different words in a text: the more frequent a particular word appears, the larger its presence in the word cloud. In fact, Voyant allows you to see the underlying frequencies that it is using to generate the cloud if you click the "Corpus Terms" button above the word cloud.

![underlying corpus term frequency](/assets/voyant_term_frequencies.png)

Concordances like these are some of the oldest forms of text analysis that we have, and computers are especially good at producing them. In fact, a project of this kind frequently cited as one of the origin stories of digital humanities: [Father Roberto Busa's massive concordance of the works of St. Thomas Aquinas](http://www.historyofinformation.com/expanded.php?id=2321) begun on punch cards in the 1940's and 50's was one of the first works of its kind and was instrumental in expanding the kinds of things that we could use computers to do.

Busa's work took years. We can now carry out similar searches in seconds, and we can learn a lot simply by counting words. The most frequent words, by far, are 'said' and 'Todd," which makes a certain amount of sense. Many characters might speak and, when they do, they are probably talking about the central character.

Notice the words that you do not see on this list: words like 'a' or 'the.' Words like these, **stopwords** are _so_ common that they are frequently excluded from analyses entirely, the reasoning being that they become something like linguistic noise, overshadowing words that might be more meaningful to the document. To see the words that Voyant excludes by default, hover next to the question mark at the top of the pane and click the second option from the right:

![voyant settings](/assets/voyant_settings.png)

Use the dropdown list to switch from 'auto-detect' to none. Now the concordance will show you the actual word frequencies in the text. Notice that 'said', the number one result in the original graph, does not even come close to the frequent usage of articles, prepositions, and pronouns.

![concordance with no stopwords](/assets/stopword_free_concordance.png)

Words like these occur with such frequency that we often need to remove them entirely in order to get meaningful results. But the list of words that we might want to remove might change depending on the context. For example, language does not remain stable over time. Different decades and centuries have different linguistic patterns for which you might need to account. Shakespearean scholars might want to use an [early modern stopword list](file.path/assets/early_modern_stopwords.txt) provided by Stephen Wittek. You can use this same area of _Voyant_ to edit the stoplist used by your analyis.

There are some instances in which we might care a lot about just these words. They can tell us _how_ an author writes: those very words that might seem not to convey much meeting are the building blocks of style. Tamper with someone's use of prepositions or pronouns and you will quickly change the nature of their voice. You can use this same feature to edit the list of stopwords. Doing so will give you greater control over the tool and allow you to fine-tune it to your particular research questions.

Return to the word cloud. Using the slider below the word cloud, you can reduce or expand the number of terms visible in the visualization. Slide it all the way to the left to include the maximum number of words.

![voyant word clouse dense](/assets/voyant_word_cloud_dense.png)

Just like the stopword list can be used to adjust the filters that help to give you meaningful results, this slider adjusts the visualization that you get. It should become clear as you play with both options that different filters and different visualizations can give you radically different readings. The results are far from objective: your own reading, the tool itself and how you use it all shape the data as it comes to be known.

This is a good reminder that you should not think of digital tools as gateways to fixed and clear truths, either about historical periods or individual texts. Voyant may seem somehow objective in that it produces mathematical calculations and data visualizations, but now you've seen that you can easily alter the results. These techniques of "distant reading" are same as the models of "close reading" we talked about earlier in that both only lead to asking more questions and positing more interpretations.

That is a good thing.

## Interpreting Word Clouds

Given that what's important about word clouds is not producing visualizations so much as the interpreting Voyant helps you come up with, you might ask: what does this help us learn about _The String of Pearls_?

For one, looking at these word clouds suggests that much of the vocabulary of this novel either refers to or exists in the context of speech.  One of the most prominent words is "said," but you also see "say" and "speak" and words like "yes," "I'll," and "oh" which probably -- although not necessarily -- come from written dialog.

Additionally, most of the words are relatively short and most are only one or two syllables long.  Penny dreadfuls like _The String of Pearls_ were aimed at working class audiences: could the prevalence of these relatively 'simple' words reflect the audience of the text? In order to substantiate such a claim, we would probably want to look at other publications of the period to see whether or not such a list of frequently used words was typical or not.

If we load Arthur Conan Doyle's "A Scandal in Bohemia" into Voyant, you can see that we get quite different results. \(Again, feel free to follow along!\)

![](/assets/Screen Shot 2016-08-09 at 11.47.16 AM.png)

A quick glance shows that the most common words tend to be longer in length than those in _A String of Pearls_, with the three syllable "photograph" being one of the most frequently used terms in this short story, one written for a middle-class as opposed to lower-class audience. So maybe the simple vocabulary of the penny dreadful is related to the nature of its readership.



give it three more instances of analysis for sweeney \(the concordance is only half fleshed out right now\).
patterns \(say more about this\), noise in visualizations \(say more\)

