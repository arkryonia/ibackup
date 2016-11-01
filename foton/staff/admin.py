from django.contrib import admin
from .models import Scolar, Commercial, Year

@admin.register(Scolar, Commercial)
class ScolarModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
	pass