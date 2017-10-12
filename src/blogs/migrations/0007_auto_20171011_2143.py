# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20170927_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Commentary'),
        ),
    ]
