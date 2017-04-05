from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Option(TimeStampedModel):
	name = models.CharField(max_length=200, verbose_name='Name')
	class Meta:
		verbose_name = "Option"
		verbose_name_plural = "Options"

	def __str__(self):
		return self.name


class Speciality(TimeStampedModel):
	option = models.ForeignKey(Option)
	name = models.CharField(max_length=100, verbose_name='Name')
	class Meta:
		verbose_name = "Speciality"
		verbose_name_plural = "Specialities"

	def __str__(self):
		return self.name


class Student(TimeStampedModel):
	GENDER = (
		("Female", _("Female")),
		("Male", _("Male")),
	)
	surname = models.CharField(max_length=100, verbose_name='Surname')
	name = models.CharField(max_length=100, verbose_name='Name(s)')
	gender = models.CharField(max_length=10, choices=GENDER)
	date_of_birth = models.DateField(verbose_name='Date of Birth')
	birth_venue = models.CharField(max_length=200, verbose_name='Birth Venue (for example \'Surulere, Lagos\')')
	number = models.IntegerField(unique=True)
	matricule_number = models.CharField(max_length=10, verbose_name='Matricule Number')
	defense_score = models.FloatField(blank=True, verbose_name='Defense Score', null=True)
	mention = models.CharField(max_length=50, blank=True)
	class_of_degree = models.CharField(max_length=100, blank=True, verbose_name='Class of Degree')
	is_print = models.BooleanField(default=False, verbose_name='Is Print')
   
	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Students"

	def __str__(self):
		return "{0} {1}".format(self.surname, self.name)
    


class Bachelor(Student):
	option = models.ForeignKey(Option, blank=True, verbose_name='Option')
	class Meta:
		verbose_name = "Bachelor"
		verbose_name_plural = "Bachelors"


class Master(Student):
	speciality = models.ForeignKey(Speciality, blank=True)
	class Meta:
		verbose_name = "Master"
		verbose_name_plural = "Masters"



    

