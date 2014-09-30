#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joe Bloggs'
SITENAME = u'My Blog'
SITEURL = 'http://myblog.me.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en_GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SOCIAL = (
    ('Google+', 'http://plus.google.com/+username',
        'fa fa-google-plus-square fa-fw fa-lg'),
    ('Twitter', 'https://twitter.com/username',
        'fa fa-twitter-square fa-fw fa-lg'),
    ('LinkedIn', 'https://www.linkedin.com/in/username',
        'fa fa-linkedin-square fa-fw fa-lg'),
    ('BitBucket', 'http://bitbucket.org/username',
        'fa fa-bitbucket-square fa-fw fa-lg'),
    ('GitHub', 'http://github.com/username',
        'fa fa-github-square fa-fw fa-lg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ('plugins',)
PLUGINS = ['creole_reader', ]

THEME = 'themes/voidy-bootstrap/'

# DISQUS_SITENAME = 'sitename'
