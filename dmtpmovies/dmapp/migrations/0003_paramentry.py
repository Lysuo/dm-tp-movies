# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmapp', '0002_auto_20170117_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParamEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=50)),
                ('mValue', models.CharField(max_length=200)),
            ],
        ),
    ]