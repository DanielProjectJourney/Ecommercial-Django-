# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='My Location', max_length=1200),
        ),
    ]
