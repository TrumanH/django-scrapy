# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from newscraw.items import newsItem
import time
import json
import os
import codecs
import re

class NewscrawPipeline(object):
    def __init__(self):
        self.path = os.getcwd()
        
    def process_item(self, item, spider):
        if spider.name == 'news_spider': #In case there's other spider
            self.file0 = codecs.open(self.path + "dailynews.json", 'a+', encoding="utf-8")
            self.file0.seek(0)
            existing = self.file0.read() #读取已存在的数据
            for i in item['items']:
                m = {}
                m['nid'] = i['id']
                m['title'] = (i['country']+i['title'])
                m['datetime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['public_date']))
                m['value'] = i['actual']+i['unit'] if(i['actual']!='') else ''
                m['forecast'] = i['forecast']+i['unit'] if(i['forecast']!='') else ''
                m['previous'] = i['previous']+i['unit'] if(i['previous']!='') else ''
                m['star'] = i['importance']
                line = json.dumps(m, ensure_ascii=False) + '\n'
                if not re.search(line, existing): #与已存在的数据进行比对不重复则存入
                    self.file0.write(line)
            self.file0.close()
            #return item
        #when run the seconde spider
        if spider.name == 'sina_spider':
            self.file1 = codecs.open(self.path+"sinanews.txt", 'a+', encoding="utf-8")
            self.file1.seek(0)
            existing = self.file1.read()
            if not re.search(item['content'], existing):
                #不重复则追加写入
                self.file1.write(item['content'])
            self.file1.close()
            

    #def close_spider(self, spider):

    #Local tested, bugfree  --2018-08-30,Truman He
        
        
        




