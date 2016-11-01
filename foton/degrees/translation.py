# -*- coding: utf-8 -*-
# @Author: Reysh Technologies
# @Date:   2016-07-28 06:13:32
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-07-28 06:23:44

from modeltranslation.translator import register, translator, TranslationOptions
from .models import Bachelor, Master, Program

# class ProgramTranslationOptions(TranslationOptions):
# 	fields = ('pdf',)
# 	required_languages = ('fr','en',)
# translator.register(Program, ProgramTranslationOptions)

# class BachelorTranslationOptions(TranslationOptions):
# 	fields = ('option',)
# 	required_languages = ('fr','en',)
# translator.register(Bachelor, BachelorTranslationOptions)

# class MasterTranslationOptions(TranslationOptions):
# 	fields = ('speciality',)
# 	required_languages = ('fr','en')
# translator.register(Master, MasterTranslationOptions)