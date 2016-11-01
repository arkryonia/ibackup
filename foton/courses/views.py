from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.forms.models import modelform_factory
from django.apps import apps

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  View,
                                  FormView
                                  )
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin
                                        )
from django.db.models import Q

from foton.courses.models import Course, Module, Content
from foton.universities.models import University
from .formset import CourseEnrollForm

class StudentEnrollCourseView(FormView):
    course = None
    form_class = CourseEnrollForm
    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses', args=[self.course.program.slug, self.course.id])

# ===============Course
class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/admin/courses/create_course.html"

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/admin/courses/update_course.html"

class CourseAdminListView(ListView):
    model = Course
    template_name = "courses/admin/courses/list_course.html"
    context_object_name = "course"


# ===============Module

class ModuleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Module
    template_name = "courses/admin/module/create_module.html"

class ModuleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Module
    template_name = "courses/admin/module/create_module.html"

class ModuleAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Module
    template_name = "courses/admin/module/list_module.html"
    context_object_name = "module"



# ===============Content
class ContentCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required='users.is_lecturer'
    module = None
    model = None
    obj = None
    template_name = "courses/admin/create_content.html"
    
    def get_model(self, model_name):
        if model_name in ['text', 'file', 'image', 'video']:
            return apps.get_model(app_label = 'courses',
                                    model_name = model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'order',
                                                 'created',
                                                 'updated'
                                                ]
                                )
        return Form(*args, **kwargs)

    def dispatch(self, request, slug, module_id, model_name, id=None):
        self.module = get_object_or_404(Module,
                                      id = module_id,
                                      course__owner = request.user
                                      )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner = request.user
                                        )
        return super(ContentCreateView, self).dispatch(request, module_id, model_name, id)

    def get(self, request, slug, module_id, model_name, id=None):
        form = self.get_form(self.model, instance = self.obj)
        return render(request, self.template_name, {'form':form, 'object':self.obj})

    def post(self, request, slug, module_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance = self.obj,
                             data = request.POST,
                             files = request.FILES   
                            )
        if form.is_valid():
            obj = form.save(commit = False)
            obj.owner = request.user
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item = obj)
            return redirect(reverse_lazy('courses:detail-course', kwargs = {'slug':self.kwargs['slug']}))
                
        return render(request, self.template_name, {'form':form, 'object':self.obj})