# @Author: drxos
# @Date:   Saturday, May 14th 2016, 6:37:12 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 6:37:38 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django import forms
from foton.programs.models import Option
from .models import ElearningBachelor, Semester, Lecture, ElearningProgram, LectureModule

from django.forms.models import inlineformset_factory
from foton.courses.models import Course

ModuleFormSet = inlineformset_factory(Lecture, LectureModule, fields=['title', 'description'], extra=4, can_delete=False)


class ProgramEnrollForm(forms.Form):
	program = forms.ModelChoiceField(queryset=ElearningProgram.objects.all(), widget=forms.HiddenInput)

class BachelorCreateForm(forms.ModelForm):
	option = forms.ModelChoiceField(queryset=None)
	name = forms.CharField(max_length=50)
	
	class Meta:
		model = ElearningBachelor
		fields = ['option','name','pdf']
	
	def __init__(self, *args, **kwargs):
		super(BachelorCreateForm, self).__init__(*args, **kwargs)
		self.fields['option'].queryset = Option.objects.filter(domain__user = self.request.user)

class LectureCreateForm(forms.ModelForm):
    semester = forms.ModelChoiceField(queryset=None)


    class Meta: 
    	model = Lecture
    	fields = ['semester']
    def __init__(self, *args, **kwargs):
        super(LectureCreateForm, self).__init__(*args, **kwargs)
        program = Program.objects.get(pk = self.kwargs['pk'])
        self.fields['semester'].queryset = Semester.objects.filter(program = program)