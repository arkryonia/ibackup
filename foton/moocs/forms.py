from django import forms

from .models import MoocModule, Mooc
from foton.students.models import Student

from django.utils.translation import ugettext_lazy as _

from django.forms.models import inlineformset_factory


ModuleFormSet = inlineformset_factory(Mooc, MoocModule, fields=['title', 'description'], extra=4, can_delete=False)

class DateInput(forms.DateInput):
    input_type = 'date'

class MoocEnrollForm(forms.Form):
	course = forms.ModelChoiceField(queryset=Mooc.objects.all(), widget=forms.HiddenInput)

class MoocStudentForm(forms.ModelForm):
    password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
                    'last_name',
                    'first_name',
                    'username',
                    'email',
                    'gender',
                    'year',
                    'phone',
                    'password',
                ]


    def __init__(self, *args, **kwargs):
        super(MoocStudentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MoocStudentForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(MoocStudentForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user