# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import NewscrawItem
import time


class NewscrawPipeline(object):
    def process_item(self, item, spider):
        for i in item['items']:
            model = NewscrawItem()
            model['nid'] = i['id']
            model['title'] = (i['country']+i['title'])
            model['datetime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['public_date']))
            model['value'] = i['actual']+i['unit'] if(i['actual']!='') else ''
            model['forecast'] = i['forecast']+i['unit'] if(i['forecast']!='') else ''
            model['previous'] = i['previous']+i['unit'] if(i['previous']!='') else ''
            model['star'] = i['importance']
            print(model['title'])
            model.save()
        #return item
