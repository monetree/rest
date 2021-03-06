# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180920_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]
