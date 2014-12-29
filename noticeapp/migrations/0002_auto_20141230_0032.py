# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 0, 32, 37, 173178), verbose_name='\u4f5c\u6210\u65e5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 0, 32, 37, 173155), verbose_name='\u767a\u884c\u65e5'),
            preserve_default=True,
        ),
    ]
