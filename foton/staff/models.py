# @Author: iker
# @Date:   Monday, May 16th 2016, 11:57:13 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   iker
# @Last modified time: Tuesday, May 17th 2016, 1:26:28 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.db import models
from django_extensions.db.models import TimeStampedModel
from foton.users.models import User
from django.utils.translation import ugettext_lazy as _


class Scolar(User):
    class Meta:
        verbose_name = 'Scolar'
        verbose_name_plural = 'Scolars'


class AllianzaAdmin(User):
    class Meta:
        verbose_name = 'Allianza Admin'
        verbose_name_plural = 'Allianza Admins'


class Commercial(User):
    class Meta:
        verbose_name = 'Commercial'
        verbose_name_plural = 'Commercials'

class Year(models.Model):
	start = models.CharField(max_length=4)
	end = models.CharField(max_length=4)
	available = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Year"
		verbose_name_plural = "Years"

	def __str__(self):
		return " {0}-{1} ".format(self.start, self.end)