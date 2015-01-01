# encoding: utf-8
from django.db import models
from datetime import datetime


class Image(models.Model):
    image = models.ImageField(upload_to='upload')
    file_name = models.CharField(u"ファイル名", max_length=256)
    description = models.TextField(u"説明")
    published_at = models.DateTimeField(u"発行日")
    created_at = models.DateTimeField(u"作成日", default=datetime.now())
    is_published = models.BooleanField(u"発行済", default=False)

    def __unicode__(self):
        return self.file_name

    class Meta:
        db_table = 'images'
        verbose_name = verbose_name_plural = u"画像"
