from django.contrib import admin
from foton.courses.models import Course, Content

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ['created']
	search_fields = ['title','overview']
	# inlines = [ModuleInline]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
	list_display = ['content_type']