from django.contrib import admin


from foton.publication.models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
	list_display = ('title',)
