# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('view_time', models.IntegerField()),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
            ],
        ),
    ]
