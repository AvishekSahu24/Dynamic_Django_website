# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-07 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Manage All Contacts.',
            },
        ),
    ]
