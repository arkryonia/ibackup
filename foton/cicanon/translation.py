# -*- coding: utf-8 -*-
# @Author: fallanzi
# @Date:   2016-07-28 07:37:05
# @Last Modified by:   fallanzi
# @Last Modified time: 2016-08-10 18:45:54
from modeltranslation.translator import register, translator, TranslationOptions

from .models import Category, Post

class CategoryTranslationOptions(TranslationOptions):
	fields = ('name','slug',)
	required_languages = ('fr','en',)
translator.register(Category, CategoryTranslationOptions)

class PostTranslationOptions(TranslationOptions):
	fields = ('title','slug','content',)
	required_languages = ('fr','en',)
translator.register(Post, PostTranslationOptions)