#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Owen'
SITENAME = u'Owen Campbell'
SITEURL = 'http://owencampbell.me.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en_GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

SOCIAL = (
    ('Google+', 'http://plus.google.com/+OwenCampbell1',
        'fa fa-google-plus-square fa-fw fa-lg'),
    ('Twitter', 'https://twitter.com/opcampbell',
        'fa fa-twitter-square fa-fw fa-lg'),
    ('LinkedIn', 'https://www.linkedin.com/in/owencampbell',
        'fa fa-linkedin-square fa-fw fa-lg'),
    ('BitBucket', 'http://bitbucket.org/meatballs',
        'fa fa-bitbucket-square fa-fw fa-lg'),
    ('GitHub', 'http://github.com/meatballs',
        'fa fa-github-square fa-fw fa-lg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ('pelican-plugins',)
PLUGINS = ['creole_reader', ]

THEME = 'themes/voidy-bootstrap/'

DISQUS_SITENAME = 'owencampbell'
