# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 22:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0010_commentary_publication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='owner',
        ),
        migrations.AddField(
            model_name='commentary',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
