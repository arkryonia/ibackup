from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from foton.presentation.models import About, Item

@admin.register(About)
class AboutAdmin(TranslationAdmin):
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Item)
class ItemAdmin(TranslationAdmin):
	prepopulated_fields = {'slug': ('title',)}


