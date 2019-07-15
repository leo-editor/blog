#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Leo team'
SITENAME = u'Leo Blog'
#SITEURL = 'http://leo-editor.github.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

FEED_DOMAIN = 'http://leo-editor.github.io/blog'
SITEURL = 'http://leo-editor.github.io/blog'

# Blogroll
LINKS =  (('Leo project website', 'http://leoeditor.com/'),
          ('Leo community mailing list', 'https://groups.google.com/forum/?fromgroups#!forum/leo-editor'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)
)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['images',]

DEFAULT_PAGINATION = 10

# markdown config, see options at:
#   http://docs.getpelican.com/en/3.3.0/settings.html
#   http://pythonhosted.org/Markdown/extensions/
MD_EXTENSIONS = (['codehilite(css_class=highlight)','extra', 'nl2br', 'sane_lists'])