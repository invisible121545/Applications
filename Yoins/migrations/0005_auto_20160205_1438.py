# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-05 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Yoins', '0004_auto_20160205_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='ecategoryfilter',
            options={'managed': True},
        ),
    ]
