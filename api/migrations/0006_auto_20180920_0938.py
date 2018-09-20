# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180920_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='catalog',
            new_name='catalog_id',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='company_name',
        ),
        migrations.AddField(
            model_name='catalog',
            name='company_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]