# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tail_number', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('ac_type', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('serial_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=5)),
                ('elevation', models.IntegerField(verbose_name=b'elevation')),
            ],
        ),
        migrations.CreateModel(
            name='Flightdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_accel', models.DecimalField(verbose_name=b'X-axis acceleration', max_digits=12, decimal_places=6)),
                ('y_accel', models.DecimalField(verbose_name=b'Y-axis acceleration', max_digits=12, decimal_places=6)),
                ('z_accel', models.DecimalField(verbose_name=b'Z-axis acceleration', max_digits=12, decimal_places=6)),
                ('x_gyro', models.DecimalField(verbose_name=b'X-axis rate gyro', max_digits=12, decimal_places=6)),
                ('y_gyro', models.DecimalField(verbose_name=b'Y-axis rate gyro', max_digits=12, decimal_places=6)),
                ('z_gyro', models.DecimalField(verbose_name=b'Z-axis rate gyro', max_digits=12, decimal_places=6)),
                ('heading', models.DecimalField(verbose_name=b'heading', max_digits=12, decimal_places=6)),
                ('course', models.DecimalField(verbose_name=b'course', max_digits=12, decimal_places=6)),
                ('magnetic_heading', models.DecimalField(verbose_name=b'magnetic heading', max_digits=12, decimal_places=6)),
                ('alt', models.DecimalField(verbose_name=b'altitude', max_digits=12, decimal_places=6)),
                ('pressure', models.DecimalField(verbose_name=b'pressure', max_digits=12, decimal_places=6)),
                ('gps_time_delta', models.DateTimeField(verbose_name=b'time from gps signal')),
                ('gps_time', models.DateTimeField(verbose_name=b'gps time')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(verbose_name=b'notes')),
                ('start_time', models.DateTimeField(verbose_name=b'start time')),
                ('end_time', models.DateTimeField(verbose_name=b'end time')),
                ('aircraft', models.ForeignKey(to='postflightdata.Aircraft')),
                ('destination_airport', models.ForeignKey(related_name='destination_airport', to='postflightdata.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('weight', models.DecimalField(verbose_name=b'weight', max_digits=3, decimal_places=1)),
                ('dob', models.DateTimeField(verbose_name=b'dob')),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='pilot',
            field=models.ForeignKey(to='postflightdata.Pilot'),
        ),
        migrations.AddField(
            model_name='mission',
            name='starting_airport',
            field=models.ForeignKey(related_name='starting_airport', to='postflightdata.Airport'),
        ),
        migrations.AddField(
            model_name='flightdata',
            name='mission',
            field=models.ForeignKey(to='postflightdata.Mission'),
        ),
    ]
