# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180920_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ManyToManyField(to='api.User'),
        ),
    ]
