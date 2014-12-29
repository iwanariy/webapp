# encoding: utf-8
from django.db import models
from datetime import datetime


class Notice(models.Model):
    title = models.CharField(u"件名", max_length=256)
    description = models.TextField(u"内容")
    author = models.CharField(u"作成者", max_length=256)
    published_at = models.DateTimeField(u"発行日")
    created_at = models.DateTimeField(u"作成日", default=datetime.now())
    is_published = models.BooleanField(u"発行済", default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'notices'
        verbose_name = u"お知らせ"
        verbose_name_plural = u"お知らせ"
