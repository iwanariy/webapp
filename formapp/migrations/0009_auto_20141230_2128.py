# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_auto_20141230_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 21, 28, 41, 550113), verbose_name='Created At'),
            preserve_default=True,
        ),
    ]
