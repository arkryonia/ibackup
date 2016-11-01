from django import forms

from .models import MoocModule, Mooc

from django.forms.models import inlineformset_factory


ModuleFormSet = inlineformset_factory(Mooc, MoocModule, fields=['title', 'description'], extra=4, can_delete=False)


class MoocEnrollForm(forms.Form):
	course = forms.ModelChoiceField(queryset=Mooc.objects.all(), widget=forms.HiddenInput)