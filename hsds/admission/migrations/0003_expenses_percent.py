# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_auto_20160626_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='percent',
            field=models.DecimalField(decimal_places=2, default=0.3, max_digits=5),
            preserve_default=False,
        ),
    ]
