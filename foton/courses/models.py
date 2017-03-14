from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from foton.users.models import User
from foton.universities.models import Lecturer
from foton.students.models import Student
from foton.courses.forms import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class Course(TimeStampedModel):

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	overview = models.TextField()
	overview_image = models.ImageField(upload_to='img/') 
	students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

	class Meta:
		# ordering = ('-created',)
		verbose_name = "Course"
		verbose_name_plural = "Courses"

	def __str__(self):
		return self.title

class Module(TimeStampedModel):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	class Meta:
		# abstract = True
		# ordering = ('order',)
		verbose_name = "Module"
		verbose_name_plural = "Modules"

	def __str__(self):
		return self.title


class Content(TimeStampedModel):
	module = models.ForeignKey(Module, related_name='contents')
	content_type = models.ForeignKey(ContentType,
		limit_choices_to = {'model__in':(	'text',
											# 'video',
											'image',
											'file')})
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')

	class Meta:
		verbose_name = "Content"
		verbose_name_plural = "Contents"
    
		
class ItemBase(TimeStampedModel):
	owner = models.ForeignKey(User, related_name='%(class)s_related')
	title = models.CharField(max_length=200)

	class Meta:
		abstract = True
		verbose_name = "ItemBase"
		verbose_name_plural = "ItemBases"

	def __str__(self):
		return self.title

	def render(self):
		return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})

class Text(ItemBase):
	content = models.TextField()
	class Meta:
		verbose_name = "Text"
		verbose_name_plural = "Texts"

class File(ItemBase):
	file = models.FileField(upload_to='files/')
	class Meta:
		verbose_name = "File"
		verbose_name_plural = "Files"

class Image(ItemBase):
	file = models.FileField(upload_to='images/')
	class Meta:
		verbose_name = "Image"
		verbose_name_plural = "Images"

class Video(ItemBase):
	video = models.FileField(upload_to='videos/')
	class Meta:
		verbose_name = "Video"
		verbose_name_plural = "Videos"
    