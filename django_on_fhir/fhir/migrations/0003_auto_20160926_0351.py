# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0002_auto_20160926_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
