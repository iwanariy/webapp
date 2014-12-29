# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u4ef6\u540d')),
                ('description', models.TextField(verbose_name='\u5185\u5bb9')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u6210\u8005')),
                ('published_at', models.DateTimeField(default=datetime.datetime(2014, 12, 29, 23, 27, 43, 658247), verbose_name='\u767a\u884c\u65e5')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 12, 29, 23, 27, 43, 658269), verbose_name='\u4f5c\u6210\u65e5')),
                ('is_published', models.BooleanField(default=False, verbose_name='\u767a\u884c\u6e08')),
            ],
            options={
                'db_table': 'notices',
                'verbose_name': '\u304a\u77e5\u3089\u305b',
                'verbose_name_plural': '\u304a\u77e5\u3089\u305b',
            },
            bases=(models.Model,),
        ),
    ]
