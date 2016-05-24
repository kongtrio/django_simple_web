# coding:utf-8
from __future__ import unicode_literals

from django.db import models
import time


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=124, null=False, verbose_name=u"标题")
    author = models.CharField(max_length=32, null=False, default="yangjb", verbose_name=u"作者")
    content = models.TextField(verbose_name=u"内容")
    image = models.CharField(max_length=124, default="/static/images/art_default.png", verbose_name=u"图片地址")
    public_time = models.DateTimeField(editable=True, auto_now=True, verbose_name=u"发布时间")
    alter_time = models.DateTimeField(auto_now_add=True, editable=True, verbose_name=u"修改时间")
    display = models.BooleanField(default=True, verbose_name=u"是否发表")
    read_num = models.IntegerField(default=0, verbose_name=u"阅读数量", editable=False)

    def __unicode__(self):
        return self.title
