# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, help_text='', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='', max_length=100)),
            ],
        ),
    ]