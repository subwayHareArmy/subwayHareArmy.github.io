#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Fix for ipynb plugin https://github.com/danielfrg/pelican-ipynb/issues/49 Uncomment the following lines
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import os
import sys
from datetime import date
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Blog name
AUTHOR = u'Ayush Yembarwar'
#SITENAME = u'get paid, get laid, gatorade'
SITENAME = u'Ayush Yembarwar'
SITESUBTITLE = u'Ayush Yembarwar'
SITEURL = u'https://subwayharearmy.github.io'   #Don't put a slash at the end
PATH = u'/content/'
OUTPUT_PATH = '/blog/subwayHareArmy.github.io/output/'
DELETE_OUTPUT_DIRECTORY = True
PAGE_PATHS = '/content/pages/'
ARTICLE_PATHS = '/content/articles/'

# Timezone, Language and Region
TIMEZONE = u'Asia/Kolkata'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Set the URL patterns
ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'


# EXPERIMENTAL URLs FOR TAGS COMMENT LATER IF REQUIRED
#TAG_URL = 'tag/{slug}/'
#TAG_SAVE_AS = 'tag/{slug}/index.html'
#TAGS_URL = 'tags/'
#TAGS_SAVE_AS = 'tags/index.html'

TAG_URL = 'taaaag/{slug}/'               #Generates: taaaag/t1/
TAG_SAVE_AS = 'taaaag/{slug}/index.html' #Generates: taaaag/t1/index.html

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'
#




DEFAULT_PAGINATION = 4


MARKUP = ['md']
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [	'readtime', 					# this plugin gets a rough idea of how much time people spend on posts
			'neighbors',					# 
			#'render_math', 				# not needed, since theme has support for MathJAX
			'post_stats', 					# generating stats
			'sitemap',						# generating sitemap for crawlers
			'summary',       				# auto-summarizing articles
			'feed_summary',  				# use summaries for RSS, not full articles
			'ipynb.liquid',  				# for embedding notebooks
			'liquid_tags.img',  			# embedding images
			'liquid_tags.video', 			# embedding videos
			'liquid_tags.include_code',  	# including code blocks
			'liquid_tags.literal',
            'liquid_tags.youtube',
            'liquid_tags.notebook'
		  ]

		  
# add [TOC] in markdown article to add table of contents
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Contents:' 
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

		  
# Sitemap generation for crawlers
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# for liquid tags
CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'


DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", "CNAME", "README.md", "favicon.ico", "robots.txt", "404.md", "404.html", "team.html"]

STATIC_PATHS = ['images', 'figures', 'videos', 'notebooks', 'code', 'favicon.ico' , 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# THEME SETTINGS-
THEME = "../pelican-themes/matthewkudija"

ABOUT_PAGE = 'https://subwayHareArmy.github.io/pages/about.html'
MOONSHOT_PAGE = 'https://subwayharearmy.github.io/pages/daancorona.html'
GITHUB_USERNAME = 'subwayHareArmy'
#AUTHOR_BLOG = 'https://subwayHareArmy.github.io/'
AUTHOR_CV = 'https://drive.google.com/file/d/1m3blPo5-EnrEFJn2LYsztuQWgOZmZiX1/view?usp=sharing'
#AUTHOR_EMAIL = "mailto:AyushYembarwar@gmail.com?Subject=Redirect%20from%20Blog%3A%20&Body=Hey%20Ayush%2C%0A%0A"
PAGES_LINK = 'https://subwayHareArmy.github.io/pages/pages.html'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds
ENABLE_MATHJAX = True
AUTHOR_WEBSITE = 'https://subwayHareArmy.github.io'

GOOGLE_ANALYTICS = "UA-121240916-1"
GOOGLE_OPTIMIZE = "OPT-T426J3T"

# Footer info

LICENSE_URL = "https://github.com/subwayHareArmy/subwayHareArmy.github.io/master/LICENSE"
LICENSE = "MIT"

