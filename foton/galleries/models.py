from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Gallery(TimeStampedModel):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/')
    slug = models.SlugField(unique= True)
    description = models.TextField()

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return self.name


class Photo(TimeStampedModel):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/')

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return self.title
