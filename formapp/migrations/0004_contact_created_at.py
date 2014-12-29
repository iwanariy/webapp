# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0003_auto_20141222_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 15, 54, 33, 348796), verbose_name='Created At'),
            preserve_default=True,
        ),
    ]
