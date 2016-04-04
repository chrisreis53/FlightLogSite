# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('postflightdata', '0002_mission_mission_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='airport',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='mission',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='weight',
            field=models.DecimalField(verbose_name=b'weight', max_digits=4, decimal_places=1),
        ),
    ]
