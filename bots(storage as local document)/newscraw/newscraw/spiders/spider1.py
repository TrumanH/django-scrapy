#!-*-coding:utf-8 -*-
#!@Date&Time:2018-08-28 11:13
#!@Author:Truman He
#!@File:spider1.py

import re
import scrapy
from ..items import sinaItem
from scrapy.http import Request

#You can define other spiders blow, and just remember to add condition judgement branchs in pipelines
class NewsSpider1(scrapy.Spider):
    name = 'sina_spider'
    def start_requests(self):
        start_urls = ['http://finance.sina.com.cn/stock/cpbd/']
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
        for url in start_urls:
            yield Request(url, headers=headers, callback=self.parse)
    def parse(self, response):
        item = sinaItem()
        item['content'] = ''
        re_list = response.xpath('//div[@class="content hg_content"]//text()').extract()
        for i in re_list:
            item['content'] += i
        #也可使用正则表达式匹配到内容中的所有s 空格 \n换行 和 <.*?>所有的标签
        #pattern = re.compile(r'\s|\n|<.*?>', re.S)
        #item['content'] = pattern.sub('', contents)
        yield item
