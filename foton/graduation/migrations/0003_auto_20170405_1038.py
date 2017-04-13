# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-05 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0002_auto_20170405_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='graduation.Speciality'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth (mm/dd/yyyy)'),
        ),
    ]