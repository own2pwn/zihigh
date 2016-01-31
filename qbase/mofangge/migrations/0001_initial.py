# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outline',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('course', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('options', models.TextField()),
                ('answer', models.TextField()),
                ('oname', models.CharField(max_length=1000)),
                ('explain', models.TextField()),
            ],
        ),
    ]
