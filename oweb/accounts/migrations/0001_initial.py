# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 04:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('born_date', models.DateField(blank=True, default=None, null=True, verbose_name='Born date')),
                ('last_connection', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of last connection')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date of Birthday')),
            ],
        ),
    ]
