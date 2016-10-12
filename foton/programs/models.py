#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Tuesday, May 17th 2016, 12:10:52 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 1:12:15 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Domain(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    def __str__(self):
        return self.name

class Option(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    domain = models.ForeignKey(Domain)

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')

    def __str__(self):
        return self.name

class Speciality(TimeStampedModel):
    name= models.CharField(max_length=100, unique=True)
    option = models.ForeignKey(Option)

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return self.name
