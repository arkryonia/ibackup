from django.contrib import admin
from .models import Lecturer

# @admin.register(University)
# class UniversityAdmin(admin.ModelAdmin):
# 	pass

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
	pass