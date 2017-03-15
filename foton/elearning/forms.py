# @Author: drxos
# @Date:   Saturday, May 14th 2016, 6:37:12 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 6:37:38 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django import forms
from django.utils.translation import ugettext_lazy as _


from foton.programs.models import Option
from .models import (ElearningBachelor, Semester, Lecture, 
ElearningProgram, LectureModule, AllianzaStudent, AllianzaRegistred)

from django.forms.models import inlineformset_factory
from foton.courses.models import Course

ModuleFormSet = inlineformset_factory(Lecture, LectureModule, \
    fields=['title', 'description'], extra=4, can_delete=False)

class DateInput(forms.DateInput):
    input_type = 'date'

class AllianzaStudentForm(forms.ModelForm):
    password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)

    class Meta:
        model = AllianzaStudent
        fields = [
                    'gender',
                    'first_name',
                    'last_name',
                    # 'marital_status',
                    'origin',
                    # 'program',
                    'year',
                    # 'national_Id',
                    'birth_date',
                    'birth_venue',
                    'username',
                    'email',
                    'phone',
                    'password',
                ]
        widgets = {
            'birth_date': DateInput(),
        }


    def __init__(self, *args, **kwargs):
        super(AllianzaStudentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(AllianzaStudentForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(AllianzaStudentForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class RegistrationForm(forms.ModelForm):
    matricule = forms.IntegerField()
    # clazz = forms.ModelMultipleChoiceField(Class, label = _('Class'))
    class Meta:
        model = AllianzaRegistred
        fields = ['matricule',]

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        registered = super(RegistrationForm, self).save(commit=False)
        if commit:
            registered.save()
        return registered


class ProgramEnrollForm(forms.Form):
	program = forms.ModelChoiceField(queryset=ElearningProgram.objects.all(), \
        widget=forms.HiddenInput)

class BachelorCreateForm(forms.ModelForm):
	option = forms.ModelChoiceField(queryset=None)
	name = forms.CharField(max_length=50)
	
	class Meta:
		model = ElearningBachelor
		fields = ['option','name','pdf']
	
	def __init__(self, *args, **kwargs):
		super(BachelorCreateForm, self).__init__(*args, **kwargs)
		self.fields['option'].queryset = Option.objects.\
        filter(domain__user = self.request.user)

class LectureCreateForm(forms.ModelForm):
    semester = forms.ModelChoiceField(queryset=Semester.objects.filter())
    class Meta: 
    	model = Lecture
    	fields = ['semester']

    # def __init__(self, *args, **kwargs):
    #     super(LectureCreateForm, self).__init__(*args, **kwargs)
    #     program = ElearningProgram.objects.get(slug = self.kwargs['slug'])
    #     self.fields['semester'] = forms.ModelChoiceField(\
    #     	queryset=Semester.objects.filter(program = program)
    # 	)
    #     self.fields['semester'].queryset = \
    #     Semester.objects.filter(domain__user = self.request.user)