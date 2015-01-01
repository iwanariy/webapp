# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/Users/YukiIwanari/src/simple_web_page/static/')),
                ('file_name', models.CharField(max_length=256, verbose_name='\u30d5\u30a1\u30a4\u30eb\u540d')),
                ('description', models.TextField(verbose_name='\u8aac\u660e')),
                ('published_at', models.DateTimeField(verbose_name='\u767a\u884c\u65e5')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 21, 28, 41, 551599), verbose_name='\u4f5c\u6210\u65e5')),
                ('is_published', models.BooleanField(default=False, verbose_name='\u767a\u884c\u6e08')),
            ],
            options={
                'db_table': 'images',
                'verbose_name': '\u753b\u50cf',
                'verbose_name_plural': '\u753b\u50cf',
            },
            bases=(models.Model,),
        ),
    ]
