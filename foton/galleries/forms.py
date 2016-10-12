from django import forms
from django.db import models
from django.utils.text import slugify

from .models import Gallery

class GalleryCreationForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['name_fr','name_en','image','description_fr','description_en']

    def save(self):
        instance = super(GalleryCreationForm, self).save(commit=False)
        instance.username = slugify(instance.name)
        instance.slug = slugify(instance.name)
        instance.save()

        return instance
