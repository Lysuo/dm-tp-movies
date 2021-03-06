# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieentry',
            name='mActorsI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mAwardsI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mCountryI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mDateReleaseI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mDescriptionI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mDirectorI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat7',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mFormat8',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mGenreI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mImgI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mLanguageI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mRatingI',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mTitleI',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mVotesI',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movieentry',
            name='mYearI',
            field=models.IntegerField(blank=True),
        ),
    ]
