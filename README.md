leo-blog
========

Blog source code

To read the blog head over to http://leo-editor.github.io/


How to publish on the Leo blog
------------------------------

### Initial Setup ###

First, you need to be added to the leo-editor organization here on github.  Ask in the leo-editor google group and one of us will add you.

Second, you need to clone two repos: this one, and leo-editor/leo-editor.github.io.

    git clone git@github.com:leo-editor/leo-blog.git
    git clone git@github.com:leo-editor/leo-editor.github.io.git

After this, be sure to install Pelican:

    pip install pelican


### Daily Use ###

    1. Sync local working copies
    2. Write your article
    3. Preview
    4. Commit source files
    5. Publish


#### Sync local working copies ####   
Before you do any work, be sure that you have the newest copies of both repositories:

    cd leo-blog
    git pull
    cd ../leo-editor.github.io
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

    mkdir output
    /path/to/pelican content -o output -s pelicanconf.py
    cd output
    python -m SimpleHTTPServer


#### Commit source files ####
Add your source document to github's copy of this repo:

    cd ../leo-blog
    git add .
    git commit -am "Added article on blahblahblah."
    git push


#### Publish to World ####
After you're satisfied with the results, it's time to publish to github.io:

    cp -r output/* ../leo-editor.github.io/
    cd ../leo-editor.github.io
    git add .
    git commit -am "Added article on blahblahblah."
    git push


That's it.  If you have any questions, ask away on the leo-editor google group.  We're pretty friendly :) 
