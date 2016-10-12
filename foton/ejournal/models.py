from django.db import models

from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Magasine(TimeStampedModel):

	title = models.CharField(_('title'), max_length=250)
	abstract = models.TextField(_('abstract'))
	issn = models.CharField(max_length=50, blank=True)
	issue = models.CharField( _('issue') , max_length=50)
	shop_link = models.URLField(blank=True)
	free = models.BooleanField(default=True)
	file = models.FileField(upload_to='files/')
	image = models.ImageField(upload_to='files/')
	class Meta:
		verbose_name = "Magasine"
		verbose_name_plural = "Magasines"

	def __str__(self):
		return self.title

class Sommary(TimeStampedModel):

	title = models.CharField( _('title'), max_length=250)
	author = models.CharField( _('author'), max_length=100)
	page = models.IntegerField(_('page'))
	keywords = models.CharField( _('keywords'), max_length=50)
	magasine = models.ForeignKey(Magasine)

	class Meta:
		verbose_name = "Sommary"
		verbose_name_plural = "Sommaries"

	def __str__(self):
		return self.title
