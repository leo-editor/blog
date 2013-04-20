screen_capture
##############

:date: 2013-04-20
:tags: plugins
:category: plugins
:slug: screen_capture
:author: Terry Brown
:summary: Captures images of the Leo window

Today I pushed a screen_capture plugin which adds two new
commands to Leo, ``screen_capture_now`` and ``screen_capture_5sec``.
A PNG image of the main Leo window, without window manager decorations,
is saved in ``$HOME/.leo/screen_captures/YYYY-MM-DDTHH:MM:SS.png``
Here's an example:

.. image:: static/images/plugins/screen_capture/screen_capture0.png

``screen_capture_now`` captures an image immediately,
``screen_capture_5sec`` waits five seconds, so you can position the
pointer, open menus etc.  The only feedback is in the console, as
messages in the log would be distracting in the captured image.

Oddly enough, all through development (this project started at the 2013
Leo Sprint), the mouse pointer was not captured. This is not at all
unusual for screen capture software. The plugin includes code to draw a
pointer (from ``.../Icons/recorder/pointer.png``) on the grabbed image.
But at time of writing the pointer is being captured, and that code is
disabled. My guess is the pointer won't be captured in all environments
and a ``@setting`` will be needed to enable pointer drawing by the
plugin.
