# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import
import datetime


# ============================================================================




# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify as s
from foton.users.models import User
from django.db.models import Model
from django.utils import timezone


# ============================================================================




# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------




# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from django_extensions.db.models import TimeStampedModel


# ============================================================================


class Category(TimeStampedModel, Model):
	"""
		Category Model aims to manage categoories entries in database
	"""
	name = models.CharField(_('Name'), max_length=50)
	slug = models.SlugField(_('Slug'), unique=True)

	class Meta:
		verbose_name 		=_('Category')
		verbose_name_plural = _('Categories')
		ordering 			= ['name']

	def __str__(self):
			return self.name


class Post(TimeStampedModel, Model):
	"""
		Post Model aims to manage post entries in the database
	"""
	title = models.CharField(_('Title'), max_length=250)
	slug = models.SlugField(_('Slug'), unique=True)
	category = models.ForeignKey(Category)
	content = models.TextField(_('Content'))
	picture = models.ImageField(upload_to='image/')
	pub = models.BooleanField(default=False)
	author = models.ForeignKey(User)

	class Meta:
		verbose_name 		=_('Post')
		verbose_name_plural = _('Posts')

	def __str__(self):
		return self.title
