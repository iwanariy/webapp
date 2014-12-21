# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_auto_20141222_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mail_address',
            field=models.EmailField(max_length=256, verbose_name='Mail Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=256, verbose_name='Subject'),
            preserve_default=True,
        ),
    ]
