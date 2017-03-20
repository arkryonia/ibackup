# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-15 09:31
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_auto_20170315_1031'),
        ('elearning', '0002_auto_20161101_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllianzaRegistred',
            fields=[
                ('registred_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.Registred')),
            ],
            options={
                'verbose_name': 'Allianza Registred',
                'verbose_name_plural': 'Allianza Registreds',
            },
            bases=('students.registred',),
        ),
        migrations.CreateModel(
            name='AllianzaStudent',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.Student')),
            ],
            options={
                'verbose_name': 'Allianza Student',
                'verbose_name_plural': 'Allianza Students',
            },
            bases=('students.student',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]