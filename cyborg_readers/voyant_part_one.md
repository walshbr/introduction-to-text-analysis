#Voyant Part One

We will be using a tool called [Voyant](http://voyant-tools.org/) to introduce some basic topics in text analysis using distant reading tools. 

Upon arriving at Voyant you will encounter a space where you can upload texts. For the following graphs, we have uploaded the full text of *The String of Pearls*, the 1846-7 penny dreadful that featured Sweeney Todd, the demon barber of Fleet Street. Feel free to [download that dataset](/assets/the_string_of_pearls_full.txt) and use it to produce the same results for following along, or upload your own texts using the window provided. ![Voyant splash page and text uploader](/assets/voyant_splash_page.png)
After Voyant processes your text you'll get a series of window panes with lots of information. Voyant packages several features into one tight digital package: each pane offers you different means of interacting with the text.

![default view of string of pearls in voyant](/assets/voyant_overview.png)

Voyant gives you lots of options, so do not be overwhelmed. Voyant provides great documentation for working through their interface, and we will not rehearse them all again [here](http://docs.voyant-tools.org/start/). Instead, we will just focus on a few features. The top left pane may be the most familiar to you:

![voyant default wordcloud of string of pearls](/assets/voyant_word_cloud_default.png)
Word clouds like these have been made popular in recent years by [Wordle](http://www.wordle.net/). They do nothing more than count the different words in a text: the more frequent a particular word appears, the larger its presence in the word cloud. In fact, Voyant allows you to see the underlying frequencies that it is using to generate the cloud if you click the "Corpus Terms" button above the word cloud. 

![underlying corpus term frequency](/assets/voyant_term_frequencies.png)

The most frequent words, by far, are 'said' and 'Todd," which makes a certain amount of sense. Many characters might speak and, when they do, they are probably talking about the central character. But notice the words that you don't see: words like 'a' or 'the.' Words like these are *so* common that they are frequently excluded from analyses entirely, the reasoning being that they become something like linguistic noise, overshadowing words that might be more meaningful to the document. To see the words that Voyant excludes by default, click the following: 
![stopwords list]()



Return to the word cloud. Using the slider below the word cloud, you can reduce or expand the number of terms visible in the visualization. Slide it all the way to the left to include the maximum number of words. 

![voyant word clouse dense](/assets/voyant_word_cloud_dense.png)