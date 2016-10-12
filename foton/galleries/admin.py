from django.contrib import admin

from foton.galleries.models import Gallery, Photo

@admin.register(Gallery)
class PlanningAdmin(admin.ModelAdmin):
	pass

@admin.register(Photo)
class PlanningItemAdmin(admin.ModelAdmin):
	pass
