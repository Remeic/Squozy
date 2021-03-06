# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShrinked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('shrinked_code', models.CharField(editable=False, max_length=30, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('tmstamp', models.IntegerField(null=True)),
            ],
        ),
    ]
