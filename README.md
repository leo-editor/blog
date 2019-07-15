leo-blog
========

Source code for publishing to the [Leo Editor Blog](http://leo-editor.github.io/blog "Leo Editor Blog").
The Leo Editor itself is at http://leoeditor.com



### Initial Setup ###

First, you need to be added to the leo-editor organization here on github.  Ask in the [leo-editor google group](https://groups.google.com/forum/#!forum/leo-editor) and one of us will add you.

Second, clone this repo:

    git clone git@github.com:leo-editor/leo-blog.git
    
After this, be sure to install Pelican:

    pip install pelican


### Daily Use ###

    1. Sync local working copy
    2. Write your article
    3. Preview
    4. Commit source files
    5. Check public url


#### Sync local working copies ####   
Before you do any work, be sure that you have the newest copy of the repository:

    cd leo-blog
    git pull

#### Write your article ####
This is a simple RST file in the content/ directory:

    cd content/
    cd your-category/
    vi your_article.rst

You can use Leo to edit the article, but I'd recommend using @auto-rst.  Not sure how well Pelican handles sentinels.

At the top of your article, you need a title, and then a few bits of info for Pelican to process your article correctly.  Here's an example from the custom_printing.rst article:

    Custom Printing with printing.py
    ################################
    
    :date: 2013-09-20
    :tags: plugins
    :category: plugins
    :slug: custom_printing
    :author: Jacob Peck
    :summary: Print custom documents with Leo's printing plugin

The rest of your article is a standard RST doc.


#### Preview ####
To preview your doc, you can use `make devserv` to start a local instance of SimpleHTTPServer.  To publish your doc, use `make html`.

Some machines might not have make, so the following command will work to build the docs and view your article instead:

linux:

    rm -r -f doc
    mkdir doc
    /path/to/pelican content -o doc -s pelicanconf.py
    cd doc
    python -m http.server

Windows:

    rmdir /s/q doc
    pelican content -o doc -s pelicanconf.py
    cd doc
    python -m http.server    

#### Commit source files ####
Add your source document to github's copy of this repo:

    git add .
    git commit -am "Added article on blahblahblah."
    git push


#### Check public view ####

Point a browser at http://leo-editor.github.io/blog

That's it.  If you have any questions, ask away on the leo-editor google group.  We're pretty friendly :) 
