# @Author: drxos
# @Date:   Friday, May 13th 2016, 8:49:26 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Friday, May 13th 2016, 9:57:14 am
# @License: Copyright (c) Foton IT, All Right Reserved

from modeltranslation.translator import register, translator, TranslationOptions

from .models import About, Item

class AboutTranslationOptions(TranslationOptions):
	fields = ('title','slug','intro',)
	required_languages = ('fr',)
translator.register(About, AboutTranslationOptions)


class ItemTranslationOptions(TranslationOptions):
	fields = ('about','title','slug','description',)
	required_languages = ('fr',)
translator.register(Item, ItemTranslationOptions)
    
