#!-*-coding:utf-8 -*-
#!@Date&Time:2018-08-23 10:21
#!@Author:Truman He
#!@File:begin.py
from scrapy import cmdline

cmdline.execute('scrapy crawl news_spider'.split())
