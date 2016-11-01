from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django_countries.fields import CountryField

from foton.users.models import User

class Lecturer(User):
	# institution = models.ForeignKey(University, verbose_name = _("university"), related_name = "University")
	presentation = models.CharField(_("Presentation"), max_length=250, blank=True)
	website = models.URLField(_("Website"), unique=True, blank=True)
	twitter = models.URLField(blank=True)
	facebook = models.URLField(blank=True)
	google_plus = models.URLField(blank=True)

	class Meta:
		verbose_name = _('Lecturer')
		verbose_name_plural = _('Lecturers')

	# def __str__(self):
	# 	return self.full_name