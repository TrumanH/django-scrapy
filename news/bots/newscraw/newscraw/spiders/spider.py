# -*- coding: utf-8 -*-
import scrapy
import json
import urllib.request
#from ..items import NewscrawItem #from newscraw.items
from scrapy.http import Request

# 时间戳后缀构造函数,生成今天的链接后缀
def ht():
    import time
    # 获取当前(日期)并转化为str格式，结果如 '2018-08-20'
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 加入时间并转化为时间数组格式
    head = time.strptime(date + ' 00:00:00', "%Y-%m-%d %H:%M:%S")
    tail = time.strptime(date + ' 23:59:59', "%Y-%m-%d %H:%M:%S")
    # 转化为所需要的时间戳格式(timestamp)
    head = str(int(time.mktime(head)))
    tail = str(int(time.mktime(tail)))
    return [head, tail]  #timestamp，such as:[1534694400, 1534780799]

class NewsSpider(scrapy.Spider):
    name = 'news_spider'

    def start_requests(self):
        t = ht()  # start&end [1534694400, 1534780799]
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
        start_urls = ['https://api-prod.wallstreetcn.com/apiv1/finance/macrodatas?start=' + t[0] + '&end=' + t[1]]
        #first scrawl
        for url in start_urls:
            yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # urllib.request.urlopen(url).read().decode('utf-8')
        item = json.loads(response.text)['data']  #['items']

        print('测试', item['items'][0])
        #[{"id":155419,"public_date":1534719660,"observation_date":"2018-08-01",
        #"wscn_ticker":"UK161642","country":"英国","title":"8月Rightmove平均房屋要价指数同比",
        yield item  #a dict contained a list which contained dicts

        #pipelines will recieve the item and process it(storage in mysql)
'''
 ERROR: Spider must return Request, BaseItem, dict or None, got 'list' in
<GET https://api-prod.wallstreetcn.com/apiv1/finance/macrodatas?start=1534867200&end=1534953599>
'''