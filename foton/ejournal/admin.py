from django.contrib import admin

from foton.ejournal.models import Magasine, Sommary

@admin.register(Magasine)
class MagasineAdmin(admin.ModelAdmin):
	list_display = ('title', 'abstract', 'issn', 'issue', 'shop_link', 'file', 'free')
	

@admin.register(Sommary)
class SommaryAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'page', 'keywords', 'magasine')
	