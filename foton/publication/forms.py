from __future__ import absolute_import, unicode_literals

from django import forms

from django.utils.translation import ugettext as _

from .models import Publication

class PostCreateForm(forms.ModelForm):	

	# title = forms.CharField(
	# 	widget=forms.TextInput(attrs={
	# 		'placeholder': _('Enter the post title')
	# 	}))


	# category = forms.ModelChoiceField(
	# 	queryset=Category.objects.all(),
	# 	widget=forms.Select(attrs={
	# 		'class':'w100 pas'
	# 	})

	# )
	content = forms.CharField(widget=forms.Textarea(attrs={'row': 30 , 'class':'w100'}))
	# img = forms.ImageField(required=False)

	class Meta:
		model = Publication
		fields = ['category', 'title', 'content', 'picture']

