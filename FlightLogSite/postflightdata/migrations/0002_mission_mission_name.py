# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postflightdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='mission_name',
            field=models.TextField(default=b'mission_name'),
        ),
    ]
