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

from .models import Bachelor, Master

# ============================================================================


@admin.register(Bachelor)
class BachelorModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Master)
class MasterModelAdmin(admin.ModelAdmin):
    pass
