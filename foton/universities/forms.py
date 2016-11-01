from __future__ import absolute_import, unicode_literals
from django import forms
from django.http import Http404

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .models import Lecturer


class LecturerCreationForm(forms.ModelForm):
    # password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)
    class Meta:
        model = Lecturer
        fields = ['username',
        			'first_name',
        			'last_name',
        			'email', 'phone',
        			'residence',
        			'presentation',
        			'website',
        			'twitter',
        			'facebook',
        			'google_plus'
    			]

    def __init__(self, *args, **kwargs):
        super(LecturerCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(LecturerCreationForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(LecturerCreationForm, self).save(commit=False)
        user.set_password('passTaka')     #(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LecturerChangeForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ['username',
        			'first_name',
        			'last_name',
        			'email', 'phone',
        			'residence',
        			'presentation',
        			'website',
        			'twitter',
        			'facebook',
        			'google_plus'
    			]
    def __init__(self, *args, **kwargs):
        super(LecturerChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(LecturerChangeForm, self).clean()
        return cleaned_data