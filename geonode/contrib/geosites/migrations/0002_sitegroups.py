# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0028_auto_20180606_1543'),
        ('sites', '0002_alter_domain_unique'),
        ('geosites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(blank=True, to='groups.GroupProfile')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Site Groups',
            },
        ),
    ]
