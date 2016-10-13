from django.contrib import admin

from foton.galleries.models import Gallery, Photo

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Photo)
class GalleryItemAdmin(admin.ModelAdmin):
	pass