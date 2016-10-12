# @Author: drxos
# @Date:   Tuesday, May 10th 2016, 3:10:33 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 12th 2016, 2:54:23 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django.contrib import admin

from foton.planning.models import Planning, PlanningItem

@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
	list_display = ('clazz',)

@admin.register(PlanningItem)
class PlanningItemAdmin(admin.ModelAdmin):
	list_display = ('planning','day','start','end','course','venue')
