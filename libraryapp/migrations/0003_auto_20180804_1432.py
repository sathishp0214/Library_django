# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20180729_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='make_query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='Name:')),
                ('email', models.EmailField(max_length=254, verbose_name='Email_ID:')),
                ('mobile', models.IntegerField(verbose_name='Mobile_No:')),
                ('message', models.CharField(max_length=300, verbose_name='Message:')),
            ],
            options={
                'db_table': 'user_queries',
            },
        ),
        migrations.RemoveField(
            model_name='bookdata',
            name='bookname',
        ),
    ]
