# -*- coding: utf-8 -*-

BOT_NAME = 'scrapy_80s_all_movie'

SPIDER_MODULES = ['scrapy_80s_all_movie.spiders']
NEWSPIDER_MODULE = 'scrapy_80s_all_movie.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
FEED_URI = u'file:///tmp/80s_allmovies.csv'
FEED_FORMAT = 'CSV'
