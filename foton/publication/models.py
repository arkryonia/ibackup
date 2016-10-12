# @Author: drxos
# @Date:   Thursday, May 5th 2016, 10:32:21 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 10:17:51 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.db import models
from djrichtextfield.models import RichTextField
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Publication(TimeStampedModel):
    CATEGORIES = (
            ('',_('Select a category')),
            ('news',_('News')),
            ('event',_('Event')),
    )
    category = models.CharField(choices = CATEGORIES, max_length=5)
    title = models.CharField(max_length=250)
    content = models.TextField()
    picture = models.ImageField(upload_to='image/')
