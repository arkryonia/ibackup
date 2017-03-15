#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Thursday, May 19th 2016, 8:51:56 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 9:03:15 am
# @License: Copyright (c) Foton IT, All Right Reserved



# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.db import models

# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------

from django_extensions.db.models import TimeStampedModel

# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from foton.programs.models import Speciality, Option

# ============================================================================

class Program(TimeStampedModel):
    pdf = models.FileField(upload_to="pdf/")

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self._meta.model_name


class Bachelor(Program):
    option = models.ForeignKey(Option)
    class Meta:
        verbose_name = 'Bachelor'
        verbose_name_plural = 'Bachelors'
    
    def __str__(self):
        return self.option.name


class Master(Program):
    speciality = models.OneToOneField(Speciality)

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'

    def __str__(self):
        return self.speciality.name