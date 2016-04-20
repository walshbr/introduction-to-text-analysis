# Voyant Part Two


Look back at the word cloud that Voyant gave us for *The String of Pearls*:

![voyant default wordcloud of string of pearls](/assets/voyant_word_cloud_default.png)

Using the standard stopword filter in Voyant, the most common word by far is 'said.' Taken alone, that might not mean an awful lot to you. But it implies a range of conversations: people speaking to each other, about different things. One of the limitations of a concordance is that it only shows you a very high-level view of the text. Once you find an interesting observation, such as 'said' being the most frequent word in the text, you might want to drill down more deeply to see particular instances of the usage. Voyant can help you just do that by providing a number of context-driven tools.

In the bottom-right pane Voyant provides with a series of options for examining the contexts around a particular word. You can change the word being examined by selecting a new word from the 'Reader' pane. By adjusting the context slider, you can modify exactly how much context you see around each word. Tools like these can be helpful for interpreting the more quantitative results that the tool provides you. 670 instances of 'said' might not mean an awful lot, and the contexts pane can help you to search for different use cases. In this case, it can be useful for seeing different conversations: frequently, said followed by a name indicates dialogue from a particular character.

![voyant contexts](/assets/voyant_contexts.png)

In this list of the first ten uses of 'said', two of them are closely joined with a name: 'Sweeney Todd.' If we look back at the word cloud for the text, we can see that these two words occur with high frequency in the text itself. Given this information, we might become interested in a series of related questions? How often is he talking? What is he talking about? 

When we start to move beyond particular words towards an interest in clusters of phrases, we introduce a number of new concepts: **ngrams** and **collocates**. 

You may have heard of **ngrams** from [the Google Ngram Viewer](https://books.google.com/ngrams), which allows users to search large corpora for specified words or phrases. An ngram is a sequence of words that occurs next to each other of a particular length: the 'n' becomes a stand-in for the specified length of phrase. So take the following sentence:

"This is a sentence to illustrate ngrams."

"To illustrate" is an ngram of length two, while "is a sentence" is an ngram of length three. We use a convenient shorthand for referring to ngrams of this length: **bigrams** and **trigrams**.

**Collocations** are words that tend to occur together in meaningful patterns: so 'good night' is a collocation because it is part of a recognized combination of words whose meaning change when put together. 'A night,' on the other hand, is not a collocation because the words do not form a unit of meaning in the same way. We can think of collocations as bigrams that occur with such frequency that the combination itself is meaningful in some way.

![voyant collocates](/assets/voyant_collocates.png)

In this case, it helps to know that the 'context' slider allows you to find sentences where two words occur near each other. So setting a context of three for 'sweeney' and 'todd' will give you all the three word phrases in which those two words occur: they do not need to be contiguous. So in this case "Sweeney Todd said" would match as would "Sweeney said Todd." Each row tells you how often those words appear within a certain distance from each other. 

Click on the row that lists 'said sweeney 52'. Many of the windows in Voyant are interactive, and selecting something will modify the visualizations and options available to you elsewhere in the tool. Selecting a row here will modify line graph that shares a space with the collocates table. You'll need to select 'Trends' at the top of the pane in order to switch back to the line graph. 

When you do, you will see 

![graph of sweeney said](/assets/sweeney_said.png)

Th