Valuespace, the spreadsheet in your outliner
############################################

:date: 2013-04-05 22:34
:tags: plugins
:category: plugins
:slug: valuespace-intro
:author: Ville Vainio
:summary: Introducing the valuespace plugin

Introduction
------------

Do you mostly use Leo as an outliner, "thought organizer" or data analysis tool? If so, this post can be useful to you. Valuespace won't help you much if you use Leo mostly as an IDE or code editor.

I could easily wax philosophical about the valuespace plugin, but I can do it in a later blog post. Here, I'll just go ahead and tell what it does.

Valuespace makes .leo document *executable*, turning the whole leo document to one big python "script" that assigns values to variables, uses those values to execute computations, and renders values of computations in the document itself.

The way to tell leo to execute the current document is to run alt-x vs-update.


Embed scripts in body text
==========================

Clearly, it makes no sense to execute everything in a .leo document that mostly consists of human readable text. To mark a part of body text as executable, use @x in the beginning of line.

There are two variants of this. Single line statements look like this:


.. code-block:: python

	This is some text
	that does not get executed
	@x foo = 1 + 2
	more text follows

Observant reader will not be surprised by what it does.

Running large swatches of text is a natural extension of this notation:

.. code-block:: python

	Some text that doesn't get executed

	@x {

	foo = 1 + 2
	bar = foo + 1

	@x }

	more text that doesn't get executed

Note that leo "tangling" (parsing of  `<< section >>` blocks and `@others` directives) is run on the executed script, so if you want to split your python code to a deeper Leo tree, you can do something like this:

.. code-block:: python

	@x {
		import os, sys

		@others
	@x }

This will interpret (and run) the subtree after doing the imports. For data analysis, you could e.g. have a first node called "prelude", looking much like the snippet above, and in the subtree you could declare all the functions and classes used in the rest of the document.

Sometimes, you don't really want to run a block, but rather assign it
to a python variable for further processing. This extension of `@x` notation helps here:

.. code-block:: python

	@x =somevar {
	text
	that
	gets assigned to 'somevar'
	as string
	@x }

In consecutive script blocks, you would now be free to reference the python variable 'somevar'.

Now, sometimes the variable should be a list, and you want to accumulate blocks of text to that list. Further extension of the notation looks like this:

.. code-block:: python

	@x =mylist+ {
	some text
	@x }

	Ignored text

	@x =mylist+ {
	more text
	@x }

Now, assuming `mylist` was instantiated as a list earlier, this would produce the final value of mylist as

.. code-block:: python

 	['some text', 'more text']

Slurping data from external files
=================================

If you processing data, you often want it to reside outside .leo document in external files (and follow the history separately version control, etc.). Valuespace currently has built in support for JSON and
yaml files.

Let's say you have JSON formatted data in foobar.json. To slurp in that data and store it in variable "foobar", create a node with headline `@vsi foobar.json`. `@vsi` stands for "valuespace input", and the extension .json instructs Leo to parse the file as json. For yaml files, use the extension .yaml.

Symmetrically, `@vso foobar.json` instructs Leo to grab the value of variable 'foobar' and dump its value serialized as JSON to file 'foobar.json'

In addition to reading or writing the data, both @vsi and @vso store the data as read/writted in the body text of the node. If you edit the body text, the changes are silently overwritten the next time you do `vs-update`.

Making data visible in the outline
==================================

It's often useful to display the data in your Leo outline. You can use `@r expr` construct to evaluate a python expression and put the result of evaluation in the body of the node.

E.g.



**@r mystr.upper()**

::

	HELLO WORLD

Anchors
=======

To make valuespace scale to large Leo documents, not every node gets parsed for @x contstructs. To instruct vs-update to scan the body of a node for @x consructs, you need to add an "anchor" (node with @a as headline) as a child of that node. So your outline would look like this:

- Foo
- Bar

  - Baz
  - @a

- Quux
- Xyzzy
- @r myvar

Here, only node "Bar" would have its body text scanned during vs-update. `@r myvar` would get evaluated despite the lack of the anchor, since it's headline-level construct that doesn't require parsing of the body.

You can also give anchors a name; if you have an outline like this:

- Foo
- Bar

  - @a myvar

the contents (body) of node "Bar" would get assigned to variable 'myvar' (as string), **and** the body of node Bar gets scanned for @x tags.

















