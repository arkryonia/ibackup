# -*- coding: utf-8 -*-
# @Author: fallanzi
# @Date:   2016-07-28 06:35:51
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-07-28 06:40:40

from modeltranslation.translator import register, translator, TranslationOptions

from .models import Publication

class PublicationTranslationOptions(TranslationOptions):
	fields = ('category','title','content',)
	required_languages = ('fr',)
translator.register(Publication, PublicationTranslationOptions)
