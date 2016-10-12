# -*- coding: utf-8 -*-
# @Author: fallanzi
# @Date:   2016-07-28 06:30:12
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-07-28 06:34:56

from modeltranslation.translator import register, translator, TranslationOptions

from .models import Domain, Option, Speciality

class DomainTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('fr',)
translator.register(Domain, DomainTranslationOptions)


class OptionTranslationOptions(TranslationOptions):
	fields = ('name','domain',)
	required_languages = ('fr',)
translator.register(Option, OptionTranslationOptions)

class SpecialityTranslationOptions(TranslationOptions):
	fields = ('name','option',)
	required_languages = ('fr',)
translator.register(Speciality, SpecialityTranslationOptions)