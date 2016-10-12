# @Author: drxos
# @Date:   Thursday, May 12th 2016, 9:13:11 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 10:19:20 am
# @License: Copyright (c) Foton IT, All Right Reserved



from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


from foton.notes.models import Course, Note
from foton.staff.models import Year
from foton.students.models import Class
from foton.students.models import Registred
from foton.ejournal.models import Magasine

class ClassListView(LoginRequiredMixin, ListView):
	queryset = Class.objects.order_by('name')
	template_name = 'notes/class_list.html'
	context_object_name = 'classes'
	def get_context_data(self, **kwargs):
	    context = super(ClassListView, self).get_context_data(**kwargs)
	    # context['magasines'] = Magasine.objects.order_by('-id')[:5]
	    return context


class ClassDetailView(LoginRequiredMixin, DetailView):
	model = Class
	template_name = 'notes/class_detail.html'
	context_object_name = 'pedagogic'
	def get_context_data(self, **kwargs):
		context = super(ClassDetailView, self).get_context_data(**kwargs)
		pedagogic = Class.objects.get(pk = self.kwargs['pk'])
		year = Year.objects.filter(available = True)
		registers = Registred.objects.filter(clazz = pedagogic, student__year = year)
		context['registreds'] = registers.order_by("student__last_name")
		return context

class StudentDetailView(LoginRequiredMixin, DetailView):
	model = Registred
	template_name = 'notes/student.html'
	context_object_name = 'studs'
	def get_context_data(self, **kwargs):
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		registred = Registred.objects.get(pk = self.kwargs['pk'])
		context['notes'] = Note.objects.filter(registred = registred).order_by('course')
		return context

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Backend
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


class ClassList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_scolar'
	queryset = Class.objects.order_by('level')
	template_name = 'notes/classes/list.html'
	context_object_name = 'classes'


# ========================================================================================

class CourseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_scolar'
	queryset = Course.objects.order_by('name')
	template_name = 'notes/courses/list.html'
	context_object_name = 'courses'

class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = 'users.is_scolar'
	model = Course
	fields = ['name_en','name_fr','coefficient']
	success_url = reverse_lazy('notes:list-course')
	template_name = 'notes/courses/create.html'

class CourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_scolar'
	model = Course
	fields = ['name_en','name_fr','coefficient']
	success_url = reverse_lazy('notes:list-course')
	template_name = 'notes/courses/update.html'


#>>>>>>>>>>>>>>>>>Student Registered Notes by classes<<<<<<<<<<<<

class ClassStudentList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	paginate_by = 20
	permission_required = 'users.is_scolar'
	model = Registred
	template_name = 'notes/students/list.html'
	context_object_name = 'students'

	def get_queryset(self):
		clazz = Class.objects.get(pk=self.kwargs['class_pk'])
		return Registred.objects.filter(clazz=clazz)

	def get_context_data(self, **kwargs):
		context = super(ClassStudentList, self).get_context_data(**kwargs)
		context['clazz'] = Class.objects.get(pk=self.kwargs['class_pk'])
		return context



# >>>>>>>>>>>>>>>>>>>>>Students notes <<<<<<<<<<<<<<<<<<<<<<<<<<<<

class StudentNoteList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_scolar'
	model = Note
	template_name = 'notes/note/list.html'
	context_object_name = 'notes'

	def get_queryset(self):
		registred = Registred.objects.get(pk=self.kwargs['registred_pk'])
		return Note.objects.filter(registred=registred).order_by('course')

	def get_context_data(self, **kwargs):
		context = super(StudentNoteList, self).get_context_data(**kwargs)
		context['clazz'] = Class.objects.get(pk=self.kwargs['class_pk'])
		context['student'] = Registred.objects.get(pk=self.kwargs['registred_pk'])
		return context


class NoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = 'users.is_scolar'
	model = Note
	template_name = "notes/note/create.html"
	fields = [ 'course', 'category', 'value']

	def get_success_url(self):
		return reverse_lazy('notes:list-note', kwargs={
		       'class_pk': self.kwargs['class_pk'],
		       'registred_pk': self.kwargs['registred_pk']
			}
		)

	def get_context_data(self, **kwargs):
		context = super(NoteCreateView, self).get_context_data(**kwargs)
		context['courses'] = Course.objects.all()
		context['registred'] = Registred.objects.get(pk=self.kwargs['registred_pk'])
		return context
    
	def form_valid(self, form):
		registred = Registred.objects.get(pk=self.kwargs['registred_pk'])
		form.instance.registred = registred
		return super(NoteCreateView, self).form_valid(form)

class NoteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_scolar'
	model = Note
	fields = ['category', 'course', 'course', 'value']
	template_name = "notes/note/update.html"

	def get_success_url(self):
		return reverse_lazy('notes:list-note', kwargs={
				'class_pk': self.kwargs['class_pk'],
		        'registred_pk': self.kwargs['registred_pk'],
		    }
		)