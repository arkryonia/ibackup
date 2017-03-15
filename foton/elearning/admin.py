#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Friday, May 20th 2016, 9:55:41 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Friday, May 20th 2016, 9:56:04 am
# @License: Copyright (c) Foton IT, All Right Reserved



# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.contrib import admin


# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from .models import (ElearningBachelor, ElearningMaster, Semester, Lecture,
	AllianzaStudent, AllianzaRegistred)

# ============================================================================


@admin.register(AllianzaStudent)
class ElearningBachelorModelAdmin(admin.ModelAdmin):
	pass

@admin.register(AllianzaRegistred)
class ElearningBachelorModelAdmin(admin.ModelAdmin):
	pass

@admin.register(ElearningBachelor)
class ElearningBachelorModelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

@admin.register(ElearningMaster)
class ElearningMasterModelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Semester)
class SemesterModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Lecture)
class LectureModelAdmin(admin.ModelAdmin):
    pass
