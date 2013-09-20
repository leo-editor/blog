Custom Printing with printing.py
################################

:date: 2013-09-20
:tags: plugins
:category: plugins
:slug: custom_printing
:author: Jacob Peck
:summary: Print custom documents with Leo's printing plugin

Printing with the printing.py plugin is fairly simple, and decently flexible.  However, sometimes you want more fine-grained control over the output of your print job.  For these situations, you can use a script.

Step 0: Get your imports right
------------------------------
We'll be using stuff from PyQt for this, specifically QtGui.  Be sure to import them at the top of your script::

    from PyQt4 import QtGui


Step 1: Creating your Document
------------------------------
Printing in Leo is handled by PyQt, which provides nice tools for printing QTextDocuments, which are in turn just HTML documents wrapped in a special object.

To that effect, we create our document (what follows is just a minimal example)::

    mydoc = '''
    <html>
    <h1>Hello!</h1>
    <p>Documents to be printed in Leo are just HTML documents, wrapped up in a QTextDocument object.</p>
    </html>
    '''

Note that the above string can be *any* valid HTML.

And then we wrap it in a QTextDocument::

    qtextdoc = QtGui.QTextDocument()
    qtextdoc.setHtml(mydoc)

Step 2: Print it!
-----------------
Finally, we use the printing.py plugin to preview the document to be printed::

    c.thePrintingController.print_preview_doc(qtextdoc)

You can see how the document would look when printed, and if you're satisfied, you can click on the print button from here.  If not, close the dialog, and nothing will be printed.  Easy as pie!

The full script
---------------
Here's the full script::

   @language python
    from PyQt4 import QtGui
    
    mydoc = '''
    <html>
    <h1>Hello!</h1>
    <p>Documents to be printed in Leo are just HTML documents, wrapped up in a QTextDocument object.</p>
    </html>
    '''
    
    qtextdoc = QtGui.QTextDocument()
    qtextdoc.setHtml(mydoc)
    
    c.thePrintingController.print_preview_doc(qtextdoc) 

Optional: Stylesheets
---------------------
QTextDocuments can be styled by CSS stylesheets, if you desire.  You can incorporate those with a call to qtextdoc.setDefaultStyleSheet, which takes in a string.  For example::

    css = '''
    h1 {color: #f00}
    p {color: #0f0}
    '''
    qtextdoc.setDefaultStyleSheet(css)



