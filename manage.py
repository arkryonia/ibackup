#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Hodonou Sounton <drxos>
# @Date:   Monday, April 25th 2016, 6:15:30 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 12:04:49 am
# @License: Copyright (c) Foton IT, All Right Reserved



import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
