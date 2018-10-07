import os
from scrapy import cmdline

os.chdir('newscraw')
#cmdline.execute('scrapy crawl news_spider'.split()) #cmdline only execute one line
#cmdline.execute('scrapy crawl sina_spider'.split())

os.system("scrapy crawl news_spider")
os.system("scrapy crawl sina_spider")

''' 定时执行的写法：
while True:
    print('The first spider')
    os.system("scrapy crawl news_spider")
    print('The second spider')
    os.system("scrapy crawl sina_spider")
    time.sleep(86400)# 24hours
'''
