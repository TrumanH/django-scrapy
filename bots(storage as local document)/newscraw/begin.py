#!-*-coding:utf-8 -*-
#!@Date&Time:2018-08-23 10:21
#!@Author:Truman He
#!@File:begin.py

#断点调试用
from scrapy import cmdline

#cmdline.execute('scrapy crawl news_spider'.split())
cmdline.execute('scrapy crawl sina_spider'.split())
