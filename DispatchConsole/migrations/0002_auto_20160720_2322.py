# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DispatchConsole', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='Nature',
            new_name='nature',
        ),
    ]
