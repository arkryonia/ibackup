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
from django.utils.translation import ugettext_lazy as _

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
from foton.courses.models import Course, Content, Module
from foton.universities.models import Lecturer
# from foton.degrees.models import Program, Bachelor, Master
from foton.users.models import User
from foton.courses.forms import OrderField

# ============================================================================

class ElearningProgram(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    pdf = models.FileField(upload_to="pdf/", blank=True)
    students = models.ManyToManyField(User, related_name='program_joined', blank=True)

    class Meta:
        verbose_name = 'E-Program'
        verbose_name_plural = 'E-Programs'

    def __str__(self):
        return self.pdf.url


class ElearningBachelor(ElearningProgram):
    option = models.ForeignKey(Option)
    class Meta:
        verbose_name = 'E-Bachelor'
        verbose_name_plural = 'E-Bachelors'


class ElearningMaster(ElearningProgram):
    speciality = models.OneToOneField(Speciality)

    class Meta:
        verbose_name = 'E-Master'
        verbose_name_plural = 'E-Masters'

class Semester(TimeStampedModel):
    program = models.ForeignKey(ElearningProgram)
    name = models.CharField(default="Semester", max_length=9, blank=True)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"
        unique_together = ("name", "order", "program")

    def __str__(self):
        return "{0} {1}".format(self.name, self.order)

class Lecture(Course):
    owner = models.ForeignKey(Lecturer, related_name='courses_lecturer')
    semester = models.ForeignKey(Semester)
    credits = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"

class LectureModule(Module):
    lecture = models.ForeignKey(Lecture, related_name='modules')
    order = OrderField(blank=True, for_fields=['lecture'])
    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"
    