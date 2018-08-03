#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin Faulkner'
SITENAME = 'lazytree'
SITEURL = ''
#SITEURL = 'https://www.lazytree.us'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('diaspora', 'https://joindiaspora.com/people/df70ab403afe0134a2ce0242ac110007'),
          ('github', 'http://github.com/kondor6c'),
          ('keybase', 'https://keybase.io/kondor6c'),
          ('HackerNews', 'https://news.ycombinator.com/user?id=kondor6c'),
          ('Gpodder', 'https://news.ycombinator.com/user?id=kondor6c'),
          ('Fedora', 'https://badges.fedoraproject.org/user/kondor6c'),
          ('reddit', 'https://www.reddit.com/user/kondor6c/'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/pelican-bootstrap3"

# Plugins

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

PLUGIN_PATHS = [
    'plugins/'
]
PLUGINS = ['assets', 'sitemap', 'i18n_subsites']
#Consider piwik, this could be invasive, but also useful for audience enumeration
#PIWIK_URL = 'url.where.piwik.install.is.located'
#PIWIK_SSL_URL = ''
#PIWIK_SITE_ID = '1'
