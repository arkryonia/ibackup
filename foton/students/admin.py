from django.contrib import admin

from foton.students.models import Student, Registred, Class

@admin.register(Registred)
class RegistredAdmin(admin.ModelAdmin):
	pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	pass

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
	pass