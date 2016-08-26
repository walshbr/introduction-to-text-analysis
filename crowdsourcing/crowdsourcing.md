# Crowdsourcing

Think of a common scenario: you are buying something online and, before the system will allow you to check out, you have to enter some text, transcribe some audio, or otherwise prove that you are not a robot. Doing so only takes a few seconds of your time, but such transactions happen millions of times everyday on the internet. The combined energy wasted on such simple interactions is astounding.

Now imagine that you could take all those hours of human labor and put them to something useful. [reCAPTCHA](https://www.google.com/recaptcha/intro/index.html) aims to do just that, and you've probably unwittingly used it. Those human-validation tasks we described in the last paragraph? The chances are pretty high that, when you carried one out, you may have unwittingly corrected an image transcription, helped provide a test set for artificial intelligence, or helped to make Google Maps more precise. The next time you fill out a text box to prove that you are a human, you might take a closer look at what you are doing and ask, "what is my work being used for?"

**Crowdsourcing**, broadly defined, can be thought of as the application of many different people to a single problem by having them each work on a piece of the project. The most common type of crowdsourcing is used to correct text transcriptions. When you scan an image with text in it, sophisticated computer programs run over the image to make their own best guess as to what that text might be based on vast quantities of information. This process is known as **optical character recognition (OCR)**, and these guesses are often incorrect: given many variations in font, ink type, contrast, and more, the task is actually very complicated and difficult. These mistakes are often called **dirty OCR**, and an example might look something like this:

"Qi-jtb"

That might not mean a lot out of context, but alongside an image you could probably piece together the word it was meant to represent from the original print artifact. [Ryan Cordell](http://ryancordell.org/research/qijtb-the-raven/) fixes on this particular poor scanning of the first word in the famous phrase "Quoth the Raven" from Edgar Allen Poe's "The Raven" as an example of the problems that scanning can present for studying historical documents. Such errors complicate a lot of digital text analysis: a search through the document for "Quoth" would not return this instance unless someone (or something) cleaned it. 

You will learn more about this and other problems with digital data in our chapter on [data cleaning](/data-cleaning/problems-with-data.md). For now, suffice it to say that correcting such errors is long, tedious work. They don't require much intellectual energy for a human, but they do take a lot of time. On the other hand, these correcting tasks would be very difficult for a computer to do accurately, but computers can manage the large scale of the work with little trouble. Projects like these use a technique called **microtasking**, meaning they direct the human energy of many many people to finite tasks. Microtasking projects find solutions to big problems by making them into small tasks solvable by individuals. OCR Correction is a common scenario for such projects: [Transcribe Bentham](http://blogs.ucl.ac.uk/transcribe-bentham/) asks users to prepare corrected versions of the papers of Jeremy Bentham's unpublished manuscripts, and [18thConnect](http://www.18thconnect.org/) has developed [Typewright](http://www.18thconnect.org/typewright/documents) to correct a vast number of early modern materials. Each of these projects relies on individual people correcting texts one piece at a time.

Whereas microtasking projects ask users to work on a problem already laid out for them, **macrotasking** projects are lead by the interests and aims of the group itself. *Wikipedia* is probably the most famous example of crowdsourcing, and it would fall under this category. Its many users apply their energy to common problems: the production of knowledge regarding particular topics. But *Wikipedia* is different from other forms of crowdsourcing in that it has no clear goal in sight. They will never solve knowledge: instead, *Wikipedia*'s devoted users will be continually working to develop a better understanding until the website goes offline. The user community creates their own goals, priorities, and tasks, all of which can lead to systemic problems: the articles online necessarily reflect the inherent interest of the material but, instead, the interests of the community of editors. Whereas microtasking projects are about really small, repeatable problems, macrotasking problems are fundamentally different in kind.

It is worth pausing over all of these examples to consider the labor going into them. We are talking about an incredible amount of energy and work that is essentially volunteer. If I go onto *Typewright* and help transcribe an eighteenth-century text, that is time that I could have spent doing something else, something that could have compensated me in more explicit ways.

> Is it enough that the users are contributing to the public good for these projects?

> At what point does volunteer labor become exploitation?

In many cases, these digital projects cost vast sums of money, and, so the critique goes, these funds could have provided for actual paid employees instead of volunteers. Some of these crowdsourcing participants may not even have realized they were working. In the case of *Recaptcha*, you might have taken part in a crowdsourcing project without even realizing it. 

> What are ethical practices for conducting volunteer projects on such a scale?

> What would it take for you to feel adequately compensated for your time?

These are open questions with no clear answers, but they are worth keeping in mind. I think this awareness and self-reflection must be the foundation of ethical ways of engaging with projects like these. After all, *Typewright*, *Recaptcha*, and *Transcribe Bentham* produce great results, but they do so by employing human energy to fairly menial tasks. *Wikipedia* raises other important questions about crowdsourcing: 

> Can the crowd do more?
> What happens when we give control of the project over to the crowd?
