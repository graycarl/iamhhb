# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import webfs.models


class Migration(migrations.Migration):

    dependencies = [
        ('webfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webfile',
            name='metadata',
            field=webfs.models.JsonField(blank=True, max_length=256, use_db_null=True),
        ),
        migrations.AlterField(
            model_name='webfile',
            name='mimetype',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='webfile',
            name='size',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
