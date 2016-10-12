from django.contrib import admin

from foton.notes.models import Course, Note


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	pass