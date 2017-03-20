# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    residence = models.CharField(blank=True, max_length=100, verbose_name=_("Residence"))
    phone = models.CharField(blank=True, max_length=100, verbose_name=_("Phone"))

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_complete_name(self):
        return "%s %s"%(self.last_name, self.first_name)

User._meta.get_field('first_name').verbose_name=_('First Name')
User._meta.get_field('first_name').blank=False
User._meta.get_field('first_name').null=False

User._meta.get_field('last_name').null=False
User._meta.get_field('last_name').blank=False
User._meta.get_field('last_name').verbose_name=_('Last Name')
User._meta.get_field('email').blank=False