# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180920_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='company_id',
            new_name='company_id_related',
        ),
    ]
