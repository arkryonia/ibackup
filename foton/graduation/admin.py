from django.contrib import admin
from .models import Bachelor, Master, Option, Speciality

@admin.register(Option)
class OptionModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Speciality)
class SpecialityModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Bachelor)
class BachelorModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Master)
class MasterModelAdmin(admin.ModelAdmin):
    pass




