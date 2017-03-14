# @Author: drxos
# @Date:   Saturday, May 14th 2016, 10:22:38 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   sadjad
# @Last modified time: 2016-05-20T12:40:57+01:00
# @License: Copyright (c) Foton IT, All Right Reserved

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, get_list_or_404, Http404, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, TemplateView, View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormView
from django.utils.text import slugify
from django.forms.models import modelform_factory
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.models import Group

from foton.programs.models import Option, Speciality

from .models import ElearningBachelor, ElearningMaster, Semester, Lecture, ElearningProgram, LectureModule  

from foton.courses.models import Module, Content, Course
from foton.users.models import User
from .forms import ModuleFormSet, ProgramEnrollForm
from .forms import BachelorCreateForm, LectureCreateForm




class ProgramListView(ListView):
    model = ElearningProgram
    template_name = "elearning/programs/programs_list.html"
    context_object_name = "programs"


# class RegisterProgramView(View):
#     model = ElearningProgram
#     template_name = "elearning/programs/programs_list.html"
#     context_object_name = "programs"


class ProgramDetailView(DetailView):
    model = ElearningProgram
    template_name = "elearning/programs/program_detail.html"
    context_object_name = "program"
    def get_context_data(self, **kwargs):
        context = super(ProgramDetailView, self).get_context_data(**kwargs)
        program = ElearningProgram.objects.get(slug = self.kwargs['slug'])
        context["semesters"] = Semester.objects.filter(program=program).order_by("name")\
        .annotate(total_lectures=Count('lecture'))
        context["lectures"] = Lecture.objects.filter(semester__program=program)\
        .annotate(total_modules=Count('modules')).order_by('-pk')
        context['enrollform'] = ProgramEnrollForm(initial={'program':program})
        user = User.objects.get(username=self.request.user)
        allianza = Group.objects.get(name="allianza")
        if user.student.student_type==1:
            user.groups.add(allianza)
        user.save()            
        return context


class StudentEnrollProgramView(FormView):
    program = None
    form_class = ProgramEnrollForm
    def form_valid(self, form):
        self.program = form.cleaned_data['program']
        self.program.students.add(self.request.user)
        return super(StudentEnrollProgramView, self).form_valid(form)
    def get_success_url(self):
        return reverse_lazy('elearning:student_programs')


class BachelorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_admin'
    context_object_name = 'bachelors'
    model = ElearningBachelor
    template_name = 'elearning/bachelors/list.html'

    def get_context_data(self, **kwargs):
        context = super(BachelorListView, self).get_context_data(**kwargs)
        # context['option'] = Option.objects.all()
        return context

class BachelorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_admin'
    model = ElearningBachelor
    template_name = "elearning/bachelors/detail.html"
    context_object_name = "bachelor"
    def get_context_data(self, **kwargs):
        context = super(BachelorDetailView, self).get_context_data(**kwargs)
        program = ElearningBachelor.objects.get(slug = self.kwargs['slug'])
        context['semesters'] = Semester.objects.filter(program = program).order_by("order")
        context['lectures'] = Lecture.objects.filter(semester__program = program)
        return context


class BachelorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = ElearningBachelor
    fields = ['option','name', 'pdf']
    success_url = reverse_lazy('elearning:bachelor-list')
    template_name = 'elearning/bachelors/create.html'
    
    def get_queryset(self):
        options = Option.objects.filter(domain__user=self.request.user)
        self.fields['option'].queryset = options
        return super(BachelorCreateView, self).get_queryset(self)

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)
        return super(BachelorCreateView, self).form_valid(form)

class BachelorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = ElearningBachelor
    fields = ['option','name','pdf']
    success_url = reverse_lazy('elearning:bachelor-list')
    template_name = 'elearning/bachelors/update.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)
        return super(BachelorCreateView, self).form_valid(form)


#-------------------------------------------------------------------------------

class MasterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_admin'
    context_object_name = 'masters'
    model = ElearningMaster
    template_name = 'elearning/masters/list.html'

class MasterDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_admin'
    model = ElearningMaster
    template_name = "elearning/masters/detail.html"
    context_object_name = "master"
    def get_context_data(self, **kwargs):
        context = super(MasterDetailView, self).get_context_data(**kwargs)
        program = ElearningMaster.objects.get(slug = self.kwargs['slug'])
        context['semesters'] = Semester.objects.filter(program = program).order_by("order")
        context['lectures'] = Lecture.objects.filter(semester__program = program)
        return context


class MasterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = ElearningMaster
    fields = ['speciality','name','pdf']
    success_url = reverse_lazy('elearning:masters-list')
    template_name = 'elearning/masters/create.html'

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)
        return super(MasterCreateView, self).form_valid(form)

class MasterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = ElearningMaster
    fields = ['speciality','name','pdf']
    template_name = 'elearning/masters/update.html'
    
    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name)
        return super(MasterUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('elearning:detail-bachelor', kwargs={'slug': self.kwargs['slug']})


# ------------------------------------------------------------------------------

class BachelorFrontListView(ListView):
    queryset = ElearningBachelor.objects.order_by('option')
    context_object_name = 'bachelors'
    #model = Bachelor
    template_name = 'elearning/bachelor_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(BachelorFrontListView, self).get_context_data(**kwargs)
    #     #context['option'] = Option.objects.all()
    #     return context

class MasterFrontListView(ListView):
    context_object_name = 'masters'
    model = ElearningMaster
    template_name = 'elearning/masters_list.html'

# -----------------------------------------------------------------------------

class SemesterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Semester
    fields = ['name']
    template_name = "elearning/semester/create.html"
    def get_success_url(self):
        return reverse_lazy('elearning:detail-bachelor', kwargs={
               'slug': self.kwargs['slug']
            }
        )

    def form_valid(self, form):
        p = ElearningProgram.objects.get(slug = self.kwargs['slug'])
        s = Semester.objects.filter(program = p)
        if s.count() != 6 :
            if s:
                form.instance.order = s.last().order + 1
            else:
                form.instance.order = 1
            form.instance.name = _("Semester")
            form.instance.program_id = p.id
            instance = form.save()
        else:
            raise Http404("You already have 6 Semester")

        return super(SemesterCreateView, self).form_valid(form)

class SemesterMasterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Semester
    fields = ['name']
    template_name = "elearning/semester/create.html"
    def get_success_url(self):
        return reverse_lazy('elearning:detail-master', kwargs={
               'slug': self.kwargs['slug']
            }
        )
    # def get_success_url(self):
    #     return reverse_lazy('elearning:detail-master', args=self.kwargs['slug'])
    def form_valid(self, form):
        p = ElearningProgram.objects.get(slug = self.kwargs['slug'])
        s = Semester.objects.filter(program = p)
        if s.count() != 4 :
            if s:
                form.instance.order = s.last().order + 1
            else:
                form.instance.order = 1
            form.instance.name = _("Semester")
            form.instance.program_id = p.id

            instance = form.save()
        else:
            raise Http404("You already have 4 Semester")

        return super(SemesterMasterCreateView, self).form_valid(form)

# --------------------------------------------------------------------------------------

class LectureCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Lecture
    # form_class = LectureCreateForm
    fields = ['semester','owner','title','credits','overview','overview_image']
    template_name = "elearning/lecture/create.html"

    def get_success_url(self):
        return reverse_lazy('elearning:detail-bachelor', kwargs={
                'slug': self.kwargs['slug'],
            })

    def form_valid(self, form):
        instance = form.save(False)
        instance.slug = slugify(instance.title)
        return super(LectureCreateView, self).form_valid(form)

class LectureUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = Lecture
    fields = ['semester','owner','title','credits','overview','overview_image']
    template_name = "elearning/lecture/update.html"
    
    def get_success_url(self):
        return reverse_lazy('staff:home')

    def form_valid(self, form):
        instance = form.save(False)
        instance.slug = slugify(instance.title)
        return super(LectureUpdateView, self).form_valid(form)
    
    
class LectureDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_admin'
    model = Lecture
    template_name = "elearning/lecture/detail.html"
    context_object_name = "lecture"
    def get_context_data(self, **kwargs):
        context = super(LectureDetailView, self).get_context_data(**kwargs)
        lecture = Lecture.objects.get(slug = self.kwargs['slug'])
        context['contents'] = Lecture.objects.filter(lecture = lecture)
        return context


class LectureByOwnerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_lecturer'
    model = Lecture
    template_name = "elearning/lecture/list_by_owner.html"
    context_object_name = "lectures"
    def get_context_data(self, **kwargs):
        context = super(LectureByOwnerListView, self).get_context_data(**kwargs)
        context['lectures'] = Lecture.objects.filter(owner = self.request.user)
        return context

class ModuleListView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_lecturer'
    model = Lecture
    template_name = "elearning/module/list_by_course.html"
    context_object_name = "course"
    def get_context_data(self, **kwargs):
        context = super(ModuleListView, self).get_context_data(**kwargs)
        lecture = Lecture.objects.get(slug = self.kwargs['slug'])
        context['modules'] = LectureModule.objects.filter(lecture = lecture)
        return context


class LectureModuleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateResponseMixin, View):
    permission_required='users.is_lecturer'
    template_name = 'elearning/module/create.html'
    course = None
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, slug, lecture_id):
        self.course = get_object_or_404(Lecture, id=lecture_id, owner=request.user)
        return super(LectureModuleUpdateView, self).dispatch(request, lecture_id)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('elearning:lecture-list-by-owner')
        return self.render_to_response({'course': self.course, 'formset': formset})


class ModuleContentListView(LoginRequiredMixin, PermissionRequiredMixin, TemplateResponseMixin, View):
    permission_required='users.is_lecturer'
    template_name = 'elearning/content/detail.html'
    
    def get(self, request, slug, module_id):
        module = get_object_or_404(LectureModule, id=module_id, 
        lecture__owner=request.user
        )
        return render(request, self.template_name, {'module':module})
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('theme:backend')
        return self.render_to_response({'course': self.course, 'formset': formset})


class ContentCreateUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required='users.is_lecturer'
    lecture = None
    model = None
    obj = None
    template_name = "elearning/content/create_content.html"
    
    def get_model(self, model_name):
        if model_name in ['text', 'file', 'image']:
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
        self.lecture = get_object_or_404(LectureModule,
                                      id = module_id,
                                      lecture__owner = request.user
                                      )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner = request.user
                                        )
        return super(ContentCreateUpdateView, self).dispatch(request, slug, model_name, id)

    def get(self, request, slug, model_name, id=None):
        form = self.get_form(self.model, instance = self.obj)
        return render(request, self.template_name, {'form':form, 'object':self.obj})

    def post(self, request, slug, model_name, id=None):
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
                Content.objects.create(module=self.lecture, item = obj)
            return redirect(reverse_lazy('elearning:module_content_list',
                                        kwargs = {'slug':self.kwargs['slug'], 'module_id':self.kwargs['module_id']}))        
        return render(request, self.template_name, {'form':form, 'object':self.obj})


# ======================================= Student ======================================


class StudentProgramListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_allianza'
    model = ElearningProgram
    template_name = 'elearning/programs/student_program_list.html'
    context_object_name = "student_programs"
    def get_queryset(self):
        qs = super(StudentProgramListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

class StudentProgramDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_allianza'
    model = ElearningProgram
    template_name = 'elearning/programs/student_programs_detail.html'
    context_object_name = "student_program"

    def get_queryset(self):
        qs = super(StudentProgramDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super(StudentProgramDetailView,self).get_context_data(**kwargs)
        program = self.get_object()
        context["semesters"] = Semester.objects.filter(program=program).order_by("name")\
        .annotate(total_lectures=Count('lecture'))
        context["lectures"] = Lecture.objects.filter(semester__program=program)\
        .annotate(total_modules=Count('modules')).order_by('created')
        return context


class StudentLectureDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_allianza'
    model = Lecture
    template_name = 'elearning/programs/student_lecture_detail.html'

    # def get_queryset(self):
    #     qs = super(StudentLectureDetailView, self).get_queryset()
    #     return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super(StudentLectureDetailView,self).get_context_data(**kwargs)
        lecture = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = lecture.modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = lecture.modules.first()
        return context