# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-06 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puppies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Puppes',
            new_name='Puppies',
        ),
    ]
