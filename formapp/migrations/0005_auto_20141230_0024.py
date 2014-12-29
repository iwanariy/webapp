# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 0, 24, 29, 69068), verbose_name='Created At'),
            preserve_default=True,
        ),
    ]
