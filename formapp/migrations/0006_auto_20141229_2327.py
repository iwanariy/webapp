# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0005_auto_20141229_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 29, 23, 27, 43, 657518), verbose_name='Created At'),
            preserve_default=True,
        ),
    ]
