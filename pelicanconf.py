#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

AUTHOR = u'HDU 计算机青协'
SITENAME = u"News"
SITEURL = 'http://news.hdujsjqx.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = '%Y-%m-%d'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'ZH'

THEME = 'Just-Read'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
