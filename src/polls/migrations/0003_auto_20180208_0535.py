# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-08 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_myuuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='myuuid',
            field=models.PositiveIntegerField(default=polls.models.get_my_uuid2),
        ),
    ]
