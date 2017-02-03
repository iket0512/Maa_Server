# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-03 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='map_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('name', models.CharField(default='Dr. Ram Agrawal', max_length=120)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
