from django.contrib import admin

from .models import Domain, Option, Speciality

@admin.register(Domain, Option, Speciality)
class ProgramsModelAdmin(admin.ModelAdmin):
    pass
