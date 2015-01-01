# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0002_auto_20141230_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 21, 28, 41, 550842), verbose_name='\u4f5c\u6210\u65e5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notice',
            name='published_at',
            field=models.DateTimeField(verbose_name='\u767a\u884c\u65e5'),
            preserve_default=True,
        ),
    ]
