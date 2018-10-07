# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class newsItem(scrapy.Item):
    nid = scrapy.Field()
    title = scrapy.Field()
    datetime = scrapy.Field()
    value = scrapy.Field()
    forecast = scrapy.Field()
    previous = scrapy.Field()
    stars = scrapy.Field()

class sinaItem(scrapy.Item):
    #date = scrapy.Field()
    content = scrapy.Field()





