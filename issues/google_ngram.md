# Google NGram Viewer
The [Google NGram Viewer](https://books.google.com/ngrams) is often the first thing brought out when people discuss large-scale textual analysis, and it serves well as a basic introduction into the possibilities of computer-assisted reading. 

![google ngram splash page](/assets/google_ngram_viewer.png)

The Google NGram Viewer provides a quick and easy way to explore changes in language over the course of many years in many texts. Provide a word or comma-seperated phrase, and the NGram viewer will graph how often those search terms occur over a given corpus for a given number of years. You can specify a number of years as well as a particular google books corpus. 

The tool allows you to quickly search thousands of texts and, by tracking a few words or phrases, draw inferences about cultural and historical shifts. For example, with a quick search on 'science' and 'religion,' for example, we could draw conclusions about their relative importance at various points in last few centuries.

<iframe name="ngram_chart" src="https://books.google.com/ngrams/interactive_chart?content=science%2Creligion&year_start=1600&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Cscience%3B%2Cc0%3B.t1%3B%2Creligion%3B%2Cc0" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

Looking at the graph, one could see evidence for a variety of commonly held arguments about the increasing secularization of society in the last two centuries. The steady increase of usage of the word science over the last 200 years accompanied by the precipitous decline of the word religion might provide concrete evidence for what might otherwise be anecdotal. But not so fast: what is actually being measured here? We can ask questions of a number of pieces of this argument:

* Corpus
* Methodology
* Interpretation


### Corpus

With any large-scale text analysis like this, the underlying data is everything. Imagine running the same word search for 'science' and 'religion' over 1000 texts used in religious schools, services. It would probably look quite different! The same would hold true if we targeted only biology, botany, and physics textbooks over the same time period. While these are fairly stark examples, the same principle holds true: the input affects the output. The texts we choose for a study can skew our concolusions, and it is important for us to think carefully about their selection as a part of the process. 

> What is the corpus, or set of texts, being used to generate this data? 

> Where is this data coming from? 

The Google NGram Viewer offers a dropdown menu where you can select a corpus for study. Our results would look a lot different depending on which corpus we selected. The corpora for these options are pulled from the Google Books scanning project (to see similar visualizations of your corpus you could try working with [Bookworm](http://bookworm.culturomics.org/), a related tool). This raises a number of difficulties. For one, the corpus only has one copy of each book in its dataset. So things do not get scaled for circulation or popularity. An book that only sells one copy becomes weighted the same as a book that sells a thousand copies: they both become a single copy according to their methods. 

The Google Books corpus has also, at times, been criticized for its heavy reliance on poor quality scans of texts to generate their data (more on this in later chapters). The computer can't infer, for example, that the mispelling 'scyience' should be lumped in with the results for 'science.' Any underlying problems in scanning or uploading texts will skew the results. For now, just remember that graphs can appear to express fact when, in fact, the data is murky, subject for debate, or skewed. 

## Methodology

Even with a perfect corpus, our choices can make a big difference in the results we produce. The above search only accounts for single words, but there are more nuanced ways of using the NGram Viewer. An NGram is another name for a sequence of words of length *n*. Take this sentence: 'a test sentence.' We have three grams of length 1, two grams of length 2, and 1 gram of length 3. Or, we could use shorthand: we have 3 unigrams or tokens, 2 bigrams, and 1 trigram. These are just fancy ways to describe different ways of chunking up a piece of text so that we can work with it. And we can do the same thing in the NGram Viewer. Take this NGram for the token 'scandal' in an English corpus:

<iframe name="ngram_chart" src="https://books.google.com/ngrams/interactive_chart?content=scandal&year_start=1600&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Cscandal%3B%2Cc0" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe> 

iframe of scandal, scandals, scandalous <iframe name="ngram_chart" src="https://books.google.com/ngrams/interactive_chart?content=scandal%2Cscandals%2Cscandalous&year_start=1600&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Cscandal%3B%2Cc0%3B.t1%3B%2Cscandals%3B%2Cc0%3B.t1%3B%2Cscandalous%3B%2Cc0" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

iframe of crime in english
<iframe name="ngram_chart" src="https://books.google.com/ngrams/interactive_chart?content=crime&year_start=1600&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Ccrime%3B%2Cc0" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

Language changes over time. 

iframe of crime in french

<iframe name="ngram_chart" src="https://books.google.com/ngrams/interactive_chart?content=crime&year_start=1600&year_end=2000&corpus=19&smoothing=3&share=&direct_url=t1%3B%2Ccrime%3B%2Cc0" width=900 height=500 marginwidth=0 marginheight=0 hspace=0 vspace=0 frameborder=0 scrolling=no></iframe>

## Interpretation

Of course, these graphs mean nothing on their own. It is our job to look at the results and describe them in meaningful ways. But be critical of what you see. You might find something interesting, but you might be looking at nonsense. It is your job to tell the difference. Beware of **apophenia**, the all to human urge to look at random data and find meaningful patterns in it. You can find wild patterns in relationships in anything if [you look hard enough](http://tylervigen.com/spurious-correlations). After all, visualizations can confuse as much as clarify. Numbers and graphs do not carry object meaning.![apophenia illustrated - noise illustration](/assets/visual_clarity.png)

Always think. Never let a graph think for you.