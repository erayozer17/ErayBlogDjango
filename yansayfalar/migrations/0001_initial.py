# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YanSayfalar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yanSayfaBaslik', models.CharField(max_length=100)),
                ('yanSayfaResim', models.ImageField(upload_to='media/')),
                ('yanSayfaGovde', models.TextField()),
            ],
        ),
    ]
