# @Author: drxos
# @Date:   Thursday, May 5th 2016, 9:31:54 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 5th 2016, 10:51:53 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from foton.students.models import Registred, Class


class Course(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    coefficient = models.IntegerField(default=1)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.name

class Note(TimeStampedModel):
    TYPE = (
        ('', '------'),
        ('test', _('Test')),
        ('exam', _('Exam')),
        ('average', _('Average')),
    )
    category = models.CharField(choices=TYPE, max_length=8)
    course = models.ForeignKey(Course)
    value = models.FloatField(default=0.0)
    registred = models.ForeignKey(Registred)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ("category",)

    def __str__(self):
        return str(self.value)
        pass