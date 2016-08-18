# Adapting This Book

We encourage others to use this book for their own courses and to change it to meet the needs of their own contexts. The publishing platform here helps to facilitate this process. We especially imagine people reworking the exercises in each chapter to reflect their own content. With a little effort you can rework the book for your own purposes and publish it to GitBooks for your students to use.

**Notes:**

* **copying the book will only get you a particular version of the book at a particular point in time. By default, any changes we make to the book after you copy it will not be reflected in your version of the book. [Syncing your version](https://help.github.com/articles/syncing-a-fork/) of the book with ours will likely conflict with any changes you have made, so I would only try that with great care.** 
* **The GitBook editor and system are changing rapidly, and I make no guarantees that these steps are updated. As of this writing, they were, but let me know by filing an issue on our [GitHub repository](https://github.com/bmw9t/introduction-to-text-analysis/issues) if you find a problem.**

## Getting Your Own Copy

The contents of this book are hosted in [a repository on GitHub](https://github.com/bmw9t/introduction-to-text-analysis) and rendered to the internet via [GitBooks](gitbook.com). When we make changes to this file structure, the changes populate out to our GitBooks account, which renders the various files into a book. To make your own remixable copy of the book, you will need to make a copy our GitHub repository and sync your copy with a GitBook of your own. Things you'll need to begin:

- GitBooks Account
- GitHub Account
- GitBooks Editor

First you will need to make a copy of our GitHub repository for your own account. When logged in and looking at our repository page, you should see these three buttons in the top-left corner of the window:

![fork button on github](/assets/conclusion/fork-button.jpg)

**Forking** is Github's term for creating a copy of a repository for yourself - imagine a road forking and diverging into two paths. If you click fork, GitHub should start the copying process. When finished, you will be redirected to your fresh copy of the repository.

![copy of github repository after forking](/assets/conclusion/github-forking.jpg)

Note the "forked from bmw9t/introduction-to-text-analysis" window at the top of the window, which lets you know where the book originated from. Above that you will see your own book's location.

#### Publishing

You have a copy of the files that make up the book, but you will need to sync them with GitBooks if you want to publish them online in the same way that we have done here. To do so, after logging into GitBooks you will click on the green 'Import Button.' ![gitbook add book button](/assets/conclusion/gitbook-add-book.jpg)

Selecting the "GITHUB" option, you will need to link your GitHub account and verify your account by an email.

![import github repository to gitbook](/assets/conclusion/gitbooks-import-github.jpg)

After linking your GitHub account, if you have more than one respository under your name you will have to select the one that you want to import to GitBooks. In this case, we will import the *Introduction to Text Analysis* repository.

![select your repo in GitBooks](/assets/conclusion/gitbook-repo-selection.jpg)

Give your repository a name and a description, and you're all set. A complete form should look something like this:

![Complete form for importing a github repository into GitBooks](/assets/conclusion/gitbooks-github-complete-import-template.jpg)

You now have a working copy of the book hosted on GitHub and rendered in GitBooks (GitBooks should automatically redirect you to your copy). You can do anything you want with these files, and they won't affect our own base copy of the resources. 

## Editing

#### Markdown

From here you just need to know a few more things to edit your new and ready-to-remix textbook. The book is written as a series of files in **markdown**, a form of markup that can easily be converted into HTML. GitBooks provides a [great tutorial on markdown](https://gitbookio.gitbooks.io/markdown/content/) that help get you started. 

#### Editing with GitBooks Editor

If markdown feels too complicated, GitBooks also provides a handy [desktop editor](https://www.gitbook.com/editor/osx) that can make the process just about as intuitive as writing in Microsoft Word. You can type in markdown, but the editor will also convert certain commands to markdown for you:

\*\*bolded text\*\* will render as **bolded text**.

But I can also highlight text and press command + b as I would in Microsoft Word to produce the same effect.

![gitbooks editor interface](/assets/conclusion/gitbooks-editor-interface.jpg)

The interface provides a preview of what your text will look like to the right of the window, which can be very helpful if you are new to markdown. If you do decide to work in the GitBooks Editor, you will need to log in the first you do so. Then select the "GitBooks.com" option for importing. 

![gitbooks cloning locally](/assets/conclusion/gitbooks-clone.jpg)

The computer will **clone**, or copy, the book to your computer. From there, you can follow the instructions in the [editor's documentation](https://help.gitbook.com/). The only significant difference from MS Word is that, after saving your work, you will need to click the sync button to upload your content to GitHub.

![gitbooks sync](/assets/conclusion/gitbooks-sync.jpg)

After doing so, any changes you have made from the GitBooks editor will also change the GitHub repository's files, which will then automatically get rendered in the GitBooks version of the site. You are all set!

#### Editing with Terminal

If you are planning to use terminal, the process is fairly similar. Once you have forked and have your own copy of the book on github, you will just clone it to your computer using the clone url found at the top of your repository's page on GitHub. Here is the one for the original book:  

![github clone url](/assets/conclusion/clone-url.jpg)

Find your own clone url, copy it to your clipboard, and use it like so (without curly braces):

```$ git clone {your_clone_url here}```

This will copy the repository to your machine. From there, you will just edit using a plain text editor as normal and make changes to the repository using [git](https://git-scm.com/). 

At this point you should have everything you need to edit your copy of the book as you see fit for your own needs. If we haven't covered something here or you run into problems, drop us a line in our [discussions forum](https://www.gitbook.com/book/bmw9t/introduction-to-text-analysis/discussions).
