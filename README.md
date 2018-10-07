# django-scrapy
just a crawler of financial news \n
结合Django和Scrapy,利用django的model来实例化采集的数据对象，用ORM与（mysql）数据库交互避免了写sql，易扩展更健壮......
不同采集源的数据格式不同(一个model不能适用所有)情况下直接存本地文件也不失为一个好方法。（见另一分支localstorage）

