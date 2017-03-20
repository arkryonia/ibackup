# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals
from django.contrib.auth.models import Group


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.utils.translation import ugettext_lazy as _
from django import forms

# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Registred, Class, Student

# ============================================================================

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
                    'last_name',
                    'first_name',
                    'gender',
                    'marital_status',
                    'year',
                    'origin',
                    'username',
                    'email',
                    'password',
                    # 'student_type',
                    # 'national_Id',
                    'birth_date',
                    'birth_venue',
                    'phone',
                    'residence',
                    'sponsor_full_name',
                    'sponsor_relationship',
                    'sponsor_address',
                    'sponsor_occupation',
                    'sponsor_phone',
                    'sponsor_email'
                ]
        widgets = {
            'birth_date': DateInput(),
        }


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(StudentForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # if user.student_type==1:
        #     allianza = Group.objects.get(name="allianza")
        #     user.groups.add(allianza)
        if commit:
            user.save()
        return user


class RegistrationForm(forms.ModelForm):
    matricule = forms.IntegerField()
    # clazz = forms.ModelMultipleChoiceField(Class, label = _('Class'))
    class Meta:
        model = Registred
        fields = ['matricule', 'clazz']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        registered = super(RegistrationForm, self).save(commit=False)
        if commit:
            registered.save()
        return registered
