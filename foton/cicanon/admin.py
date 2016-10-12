from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from foton.cicanon.models import Category, Post

@admin.register(Category)
class ategoryAdmin(TranslationAdmin):
	pass

@admin.register(Post)
class PostAdmin(TranslationAdmin):
	pass


