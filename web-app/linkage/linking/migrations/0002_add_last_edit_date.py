# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkingproject',
            name='last_edit_date',
            field=models.DateField(auto_now=True, verbose_name='Last edit date'),
        ),
        migrations.AlterField(
            model_name='linkingproject',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('READY', 'Ready'), ('RUNNING', 'In Progress'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='DRAFT', max_length=10, verbose_name='Project Status'),
        ),
        migrations.AlterField(
            model_name='linkingproject',
            name='type',
            field=models.CharField(choices=[('DEDUP', 'De-Duplication'), ('LINK', 'Data Linkage')], default='LINK', max_length=10, verbose_name='Project Type'),
        ),
    ]