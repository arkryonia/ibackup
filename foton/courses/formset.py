from django import forms

from django.forms.models import inlineformset_factory
from foton.courses.models import Course, Module

# ModuleFormSet = inlineformset_factory(Course, Module, fields=['title', 'description'], extra=4	)

class CourseEnrollForm(forms.Form):
	course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)