# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reddit',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]