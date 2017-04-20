from django.db import models
from django_extensions.db.models import TimeStampedModel
from foton.courses.models import Module, Course
from foton.users.models import User
from foton.courses.forms import OrderField

class Category(TimeStampedModel):
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	class Meta:
		verbose_name = "Domain"
		verbose_name_plural = "Domains"

	def __str__(self):
		return self.name

class Discipline(TimeStampedModel):
	domain = models.ForeignKey(Category)
	name = models.CharField(max_length=100)
	slug = models.SlugField()
	class Meta:
		verbose_name = "Discipline"
		verbose_name_plural = "Disciplines"

	def __str__(self):
		return self.name

class Mooc(Course):
	owner = models.ForeignKey(User, related_name='courses_mooc')
	discipline = models.ForeignKey(Discipline)

	class Meta:
		verbose_name = "Mooc"
		verbose_name_plural = "Moocs"

class MoocModule(Module):
	course = models.ForeignKey(Mooc, related_name='mooc_modules')
	order = OrderField(blank=True, for_fields=['course'])
	class Meta:
		verbose_name = "Mooc Module"
		verbose_name_plural = "Mooc Modules"