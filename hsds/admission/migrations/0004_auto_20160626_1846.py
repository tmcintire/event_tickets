# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_expenses_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='percent',
            field=models.IntegerField(max_length=3),
        ),
    ]
