# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20170819_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]