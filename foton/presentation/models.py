# @Author: drxos
# @Date:   Tuesday, May 10th 2016, 6:07:58 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Friday, May 13th 2016, 9:43:07 am
# @License: Copyright (c) Foton IT, All Right Reserved

from django.db import models

from django_extensions.db.models import TimeStampedModel

from django.utils.translation import ugettext_lazy as _

class About(TimeStampedModel):

	title = models.CharField( _('Title'), max_length=150)
	intro = models.TextField(_('Content'))
	slug = models.SlugField( _('slug'), default='')
	image = models.ImageField(upload_to='image/')
	class Meta:
		verbose_name = "About"
		verbose_name_plural = "Abouts"

	def __str__(self):
		return self.title


class Item(TimeStampedModel):

	about = models.ForeignKey(About, related_name='about')
	title = models.CharField( ('Title'), max_length=150)
	slug = models.SlugField(default='')
	description =  models.TextField(('Description'))
	image = models.ImageField(upload_to='image/')
	class Meta:
		verbose_name = "Item"
		verbose_name_plural = "Items"

	def __str__(self):
		return self.title
