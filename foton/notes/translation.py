# -*- coding: utf-8 -*-
# @Author: fallanzi
# @Date:   2016-07-28 07:50:17
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-07-28 07:51:21
from modeltranslation.translator import register, translator, TranslationOptions

from .models import Course

class CourseTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('fr','en',)
translator.register(Course, CourseTranslationOptions)
