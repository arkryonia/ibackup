# @Author: drxos
# @Date:   Thursday, May 5th 2016, 10:32:21 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 10:17:51 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from foton.students.models import Class
from foton.notes.models import Course

class Planning(TimeStampedModel):
    clazz = models.ForeignKey(Class, default=False)

    class Meta:
        verbose_name = _('Planning')
        verbose_name_plural = _('Plannings')

    def __str__(self):
        return self.clazz.name + ' ' + self.clazz.level

class PlanningItem(TimeStampedModel):
    DAYS = (
            ('', '----'),
            ('lundi', 'Lundi'),
            ('mardi', 'Mardi'),
            ('mercredi', 'Mercredi'),
            ('jeudi', 'Jeudi'),
            ('vendredi', 'Vendredi'),
            ('samedi', 'Samedi'),
        )
    day = models.CharField(choices=DAYS, max_length=8, default='lundi')
    start = models.IntegerField(default=1)
    end = models.IntegerField(default=1)
    course = models.ForeignKey(Course)
    venue = models.CharField(max_length=100)
    planning = models.ForeignKey(Planning, default='')

    class Meta:
        verbose_name = _('PlanningItem')
        verbose_name_plural = _('PlanningItems')

    def __str__(self):
        return self.course.name
