# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_registree_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registree',
            name='other',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
    ]