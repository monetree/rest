# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180920_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='catalog_id',
            new_name='catalog',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='company_id_related',
        ),
        migrations.AddField(
            model_name='catalog',
            name='company_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]