# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-07 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='date_added',
        ),
    ]
