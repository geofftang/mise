# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe')),
            ],
        ),
    ]
