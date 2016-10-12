# -*- coding: utf-8 -*-
# @Author: fallanzi
# @Date:   2016-07-28 07:26:39
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-07-28 07:28:15
from modeltranslation.translator import register, translator, TranslationOptions

from .models import Class

class ClassTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('fr','en',)
translator.register(Class, ClassTranslationOptions)
