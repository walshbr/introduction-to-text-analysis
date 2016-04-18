# Voyant Part One

We will be using a tool called [Voyant](http://voyant-tools.org/) to introduce some basic topics in text analysis using distant reading tools. 

Upon arriving at Voyant you will encounter a space where you can upload texts. For the following graphs, we have uploaded the full text of *The String of Pearls*, the 1846-7 penny dreadful that featured Sweeney Todd, the demon barber of Fleet Street. Feel free to [download that dataset](/assets/the_string_of_pearls_full.txt) and use it to produce the same results for following along, or upload your own texts using the window provided.

![Voyant splash page and text uploader](/assets/voyant_splash_page.png)
After Voyant processes your text you'll get a series of window panes with lots of information. Voyant packages several features into one tight digital package: each pane offers you different means of interacting with the text.

![default view of string of pearls in voyant](/assets/voyant_overview.png)

Voyant gives you lots of options, so do not be overwhelmed. Voyant provides great documentation for working through their interface, and we will not rehearse them all again [here](http://docs.voyant-tools.org/start/). Instead, we will just focus on a few features. The top left pane may be the most familiar to you:

![voyant default wordcloud of string of pearls](/assets/voyant_word_cloud_default.png)
Word clouds like these have been made popular in recent years by [Wordle](http://www.wordle.net/). They do nothing more than count the different words in a text: the more frequent a particular word appears, the larger its presence in the word cloud. In fact, Voyant allows you to see the underlying frequencies that it is using to generate the cloud if you click the "Corpus Terms" button above the word cloud. 

![underlying corpus term frequency](/assets/voyant_term_frequencies.png)

Concordances like these are some of the oldest forms of text analysis that we have, and computers are especially good at producing them. In fact, a project of this kind frequently cited as one of the origin stories of digital humanities: [Father Roberto Busa's massive concordance of the works of St. Thomas Aquinas](http://www.historyofinformation.com/expanded.php?id=2321) begun on punch cards in the 1940's and 50's was one of the first works of its kind and was instrumental in expanding the kinds of things that we could use computers to do. 

Busa's work took years. We can now carry out similar searches in seconds, and we can learn a lot simply by counting words. The most frequent words, by far, are 'said' and 'Todd," which makes a certain amount of sense. Many characters might speak and, when they do, they are probably talking about the central character. Looking at these counts, you could argue that these relatively 'simple' words might reflect the audience of the text: penny dreadfuls like *The String of Pearls* were aimed at working class audiences. In order to substantiate such a claim, we would probably want to look at other publications of the period to see whether or not such a list of frequently used words was typical or not. 

Notice the words that you don't see: words like 'a' or 'the.' Words like these, **stopwords** are *so* common that they are frequently excluded from analyses entirely, the reasoning being that they become something like linguistic noise, overshadowing words that might be more meaningful to the document. To see the words that Voyant excludes by default, hover next to the question mark at the top of the pane and click the second option from the right: 

![voyant settings](/assets/voyant_settings.png)


There are some instances in which we might care a lot about just these words. They can tell us *how* an author writes: those very words that might seem to convey much meeting are the building blocks of style. Tamper with someone's use of prepositions or pronouns and you will quickly change the nature of their voice. You can use this same feature to edit the list of stopwords. Doing so will give you greater control over the tool and allow you to fine-tune it to your particular research questions. 

Return to the word cloud. Using the slider below the word cloud, you can reduce or expand the number of terms visible in the visualization. Slide it all the way to the left to include the maximum number of words. 

![voyant word clouse dense](/assets/voyant_word_cloud_dense.png)

Just like the stopword list can be used to adjust the filters that help to give you meaningful results, this slider adjusts the visualization that you get. It should become clear as you play with both options that different filters and different visualizations can give you radically different readings. The results are far from objective: your own reading and the tool itself both shape the data as it comes to be known. Be wary of thinking of digital tools as gateways to objective truths: they only lead to more questions and more interpretations. 

That is a good thing.

update with some more analysis and language. 

give it three more instances of analysis for sweeney (the concordance is only half fleshed out right now).
patterns (say more about this), noise in visualizations (say more)