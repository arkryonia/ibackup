# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------

from django_countries.fields import CountryField
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm,landscape
from django.http import Http404, HttpResponse

# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from foton.users.models import User
from foton.degrees.models import Program
from foton.staff.models import Year

# ============================================================================


# class Program(models.Field):
#     """docstring for Program"""
#     def __init__(self, arg):
#         super(Program, self).__init__()
#         self.arg = arg
        


class Class(TimeStampedModel):
    TYPE = (
        ('', '----'),
        ('1', ('1')),
        ('2', ('2')),
        ('3', ('3')),
        ('4', ('4')),
        ('5', ('5')),
    )
    name = models.CharField(max_length=50, blank=True)
    level = models.CharField(choices=TYPE, default=1, max_length=1)
    program = models.ForeignKey(Program)
    full_name = models.CharField(max_length=51, blank=True, unique=True)

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')

    def __str__(self):
        return self.name + " " + self.level


class Student(User):
    GENDERS = (
        ("",_("Choose your gender")),
        (0, _("Female")),
        (1, _("Male")),
    )
    TYPES = (
        ("",_("Choose your type")),
        (0, _("Regular Student")),
        (1, _("Allianza Student")),
    )

    MARITAL = (
        ("",_("Choose your marital status")),
        (0, _("Single")),
        (1, _("Maried")),
    )
    
    gender      = models.IntegerField(choices=GENDERS, verbose_name = _("Gender (required) "))
    student_type = models.IntegerField(choices=TYPES, verbose_name = _("Type (required)"), default=0)
    origin      = CountryField(blank_label=_('(select country)'), verbose_name = _("Nationality (required)"))
    birth_date  = models.DateField(default=timezone.now, verbose_name=_('Birth Date (required)'))
    birth_venue = models.CharField(max_length=100, verbose_name = _("Place of Birth (required)"))
    year = models.ForeignKey(Year, verbose_name = _("Academic Year (required)"))
    national_Id = models.CharField(max_length=50, blank=True, verbose_name=_('National ID (optional)'))
    marital_status = models.IntegerField(choices=MARITAL,
                                        default=0,
                                        verbose_name = _("Marital Status (required)")
                                        )
    sponsor_full_name = models.CharField(max_length=100, verbose_name=_('Sponsor or guardian full name (required)'))
    sponsor_relationship = models.CharField(max_length=50, verbose_name = _("Relationship with Sponsor or Guardian (required)"), help_text=_('Relation to Applicant'))
    sponsor_address = models.CharField(max_length=50,verbose_name = _("Sponsor or Guardian Address (required)"), help_text=_('Sponsor or Guardian Permanent Address'))
    sponsor_occupation = models.CharField(max_length=150, verbose_name = _("Occupation (required)"))
    sponsor_phone = models.CharField(max_length=50, verbose_name = _("Sponsor or Guardian Telphone (required)"))
    sponsor_email = models.EmailField(verbose_name = _("Sponsor or Guardian Email (required)"))

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        # ordering = ('last_name',)
    
    def __str__(self):
        return self.first_name + '  ' + self.last_name

    def get_absolute_url(self):
        return reverse_lazy('students:student-detail', kwargs={'pk': self.pk})

   

class Registred(TimeStampedModel):
    student = models.OneToOneField(Student)
    clazz = models.ForeignKey(Class, verbose_name=_("Class"))
    image = models.ImageField(upload_to = 'student_img/', blank=True)
    matricule = models.IntegerField(default=1)
    matricule_number = models.CharField(max_length=12, blank=True)
    
    class Meta:
        verbose_name = _('Registred')
        verbose_name_plural = _('Registreds')

    def __str__(self):
        return "{0} is registred in {1}".format(self.student.first_name, self.student.id)

    def number(self):
        year = Year.objects.filter(available = True)
        c = Registred.objects.filter(student__year=year).all().count()
        if c == 0:
            num = 0
        else:
            num = Registred.objects.filter(student__year=year).last().matricule
        return  num

    def matricul(self):
        year = "{0}{1}".format(str(self.student.year.start[2]), str(self.student.year.start[3]))
        g = self.student.gender
        s_t = self.student.student_type
        m = str(self.matricule)
        
        if (g == 0) :
            gender = "00"
        else:
            gender = "01"

        if (s_t == 0):
            s_type = "00"
        else:
            s_type = "01"
        if len(m) == 1:
            mat = "{0}{1}".format("000", m)
        elif len(m) == 2:
            mat = "{0}{1}".format("00", m)
        elif len(m) == 3:
            mat = "{0}{1}".format("0", m)
        else:
            mat = m
        matricule_number = "{0}{1}{2}{3}".format(gender, s_type, year, mat)
        # self.matricule_number = matricule_number 
        return matricule_number

