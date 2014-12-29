# encoding: utf-8
from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(u"Name", max_length=256)
    mail_address = models.EmailField(u"Mail Address", max_length=256)
    subject = models.CharField(u"Subject", max_length=256)
    description = models.TextField(u"Description")
    created_at = models.DateTimeField(u"Created At", default=datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'contact'
        verbose_name = u"お問い合わせ"
        verbose_name_plural = u"お問い合わせ"
