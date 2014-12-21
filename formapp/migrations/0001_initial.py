# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('mail_address', models.CharField(max_length=256, verbose_name='Mail Address')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'db_table': 'contact',
                'verbose_name': '\u304a\u554f\u3044\u5408\u308f\u305b',
                'verbose_name_plural': '\u304a\u554f\u3044\u5408\u308f\u305b',
            },
            bases=(models.Model,),
        ),
    ]
