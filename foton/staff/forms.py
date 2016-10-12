# @Author: iker
# @Date:   Tuesday, May 17th 2016, 7:52:26 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   iker
# @Last modified time: Tuesday, May 17th 2016, 10:04:28 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django import forms


from .models import Scolar, Commercial
from django.utils.translation import ugettext, ugettext_lazy as _

class ScolarCreationForm(forms.ModelForm):
    # password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)
    class Meta:
        model = Scolar
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'residence']

    def __init__(self, *args, **kwargs):
        super(ScolarCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ScolarCreationForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(ScolarCreationForm, self).save(commit=False)
        user.set_password('passTaka')     #(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class ScolarChangeForm(forms.ModelForm):

    class Meta:
        model = Scolar
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'residence']

    def __init__(self, *args, **kwargs):
        super(ScolarChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ScolarChangeForm, self).clean()
        return cleaned_data

class CommercialCreationForm(forms.ModelForm):
    # password = forms.CharField(label=_('Password') ,widget=forms.PasswordInput)
    class Meta:
        model = Commercial
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'residence']

    def __init__(self, *args, **kwargs):
        super(CommercialCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CommercialCreationForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        user = super(CommercialCreationForm, self).save(commit=False)
        user.set_password('passTaka')     #(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class CommercialChangeForm(forms.ModelForm):

    class Meta:
        model = Commercial
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'residence']

    def __init__(self, *args, **kwargs):
        super(CommercialChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CommercialChangeForm, self).clean()
        return cleaned_data
