# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class dailyNews(models.Model):
    nid = models.IntegerField(unique=True)
    title = models.CharField(u'标题内容',max_length=255)
    datetime = models.DateTimeField(u'日期时间')
    value = models.CharField(u'现值', max_length=30)
    forecast = models.CharField(u'预测值', max_length=30)
    previous = models.CharField(u'前值', max_length=30)
    star = models.IntegerField(u'重要性')

    def __unicode__(self):
        return self.title
    class Meta:
        app_label = 'mainapp'
        db_table = 'dailynews'
        ordering = ['datetime']
