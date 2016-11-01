from django.contrib import admin
from .models import Category, Discipline, Mooc, MoocModule

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'created']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['created']
	search_fields = ['name',]

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
	list_display = ['name', 'created']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['created']
	search_fields = ['name',]

@admin.register(Mooc)
class MoocAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']
	list_filter = ['created']
	search_fields = ['title',]

@admin.register(MoocModule)
class MoocModuleAdmin(admin.ModelAdmin):
	pass
