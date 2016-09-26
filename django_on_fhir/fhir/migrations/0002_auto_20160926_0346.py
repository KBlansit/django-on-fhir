# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanname',
            name='use',
            field=models.CharField(blank=True, choices=[('usual', 'usual'), ('official', 'offical'), ('temp', 'temp'), ('nickname', 'nickname'), ('anonymous', 'anonymous'), ('old', 'old'), ('maiden', 'maiden')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='identifier',
            name='use',
            field=models.CharField(blank=True, choices=[('usual', 'usual'), ('official', 'official'), ('temp', 'temp'), ('secondary', 'secondary')], max_length=100),
        ),
    ]
