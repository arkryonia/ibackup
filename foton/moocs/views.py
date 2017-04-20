from django.conf import settings
from django.core.mail import EmailMessage
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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Category, Discipline, Mooc, MoocModule
from foton.courses.models import Content
from foton.users.models import User
from foton.students.models import Student

from .forms import ModuleFormSet, MoocEnrollForm, MoocStudentForm

from twilio.rest import TwilioRestClient
# client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


class MoocCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_lecturer'
    model = Mooc
    fields = ['discipline','title','overview','overview_image']
    template_name = "moocs/mooc/create.html"

    def get_success_url(self):
        return reverse_lazy('moocs:owner-list')

    def form_valid(self, form):
        instance = form.save(False)
        instance.slug = slugify(instance.title)
        instance.owner = self.request.user
        return super(MoocCreateView, self).form_valid(form)

class MoocUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_lecturer'
    model = Mooc
    fields = ['discipline','title','overview','overview_image']
    template_name = "moocs/mooc/create.html"
    def get_success_url(self):
        return reverse_lazy('moocs:owner-list')

    def form_valid(self, form):
        instance = form.save(False)
        instance.slug = slugify(instance.title)
        return super(MoocUpdateView, self).form_valid(form)
       
class MoocDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required='users.is_lecturer'
    model = Mooc
    template_name = "degrees/mooc/detail.html"
    context_object_name = "mooc"
    def get_context_data(self, **kwargs):
        context = super(MoocDetailView, self).get_context_data(**kwargs)
        mooc = Mooc.objects.get(slug = self.kwargs['slug'])
        context['contents'] = Content.objects.filter(lecture = lecture)
        return context

class MoocByOwnerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_lecturer'
    model = Mooc
    template_name = "moocs/mooc/list_by_owner.html"
    context_object_name = "moocs"
    def get_context_data(self, **kwargs):
        context = super(MoocByOwnerListView, self).get_context_data(**kwargs)
        context['moocs'] = Mooc.objects.filter(owner = self.request.user)
        return context

class ModuleListView(DetailView):
    model = Mooc
    template_name = "moocs/module/list_by_course.html"
    context_object_name = "mooc"
    def get_context_data(self, **kwargs):
        context = super(ModuleListView, self).get_context_data(**kwargs)
        mooc = Mooc.objects.get(pk = self.kwargs['pk'])
        context['modules'] = MoocModule.objects.filter(course = mooc)
        return context

class MoocModuleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateResponseMixin, View):
    permission_required='users.is_lecturer'
    template_name = 'moocs/module/create.html'
    course = None
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Mooc, id=pk, owner=request.user)
        return super(MoocModuleUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('moocs:owner-list')
        return self.render_to_response({'course': self.course, 'formset': formset})


class ModuleContentListView(LoginRequiredMixin, PermissionRequiredMixin, TemplateResponseMixin, View):
    permission_required='users.is_lecturer'
    template_name = 'moocs/content/detail.html'
    
    def get(self, request, pk, module_id):
        module = get_object_or_404(MoocModule, id=module_id, 
        course__owner=request.user
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

    def dispatch(self, request, pk, module_id, model_name, id=None):
        self.lecture = get_object_or_404(MoocModule,
                                      id = module_id,
                                      course__owner = request.user
                                      )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner = request.user
                                        )
        return super(ContentCreateUpdateView, self).dispatch(request, pk, model_name, id)

    def get(self, request, pk, model_name, id=None):
        form = self.get_form(self.model, instance = self.obj)
        return render(request, self.template_name, {'form':form, 'object':self.obj})

    def post(self, request, pk, model_name, id=None):
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
            return redirect(reverse_lazy('moocs:mooc_module_content_list',
                                        kwargs = {'pk':self.kwargs['pk'], 'module_id':self.kwargs['module_id']}))        
        return render(request, self.template_name, {'form':form, 'object':self.obj})


class MoocDetailView(DetailView):
    model = Mooc
    template_name = 'moocs/mooc/student_detail_mooc.html'
    def get_context_data(self, **kwargs):
        context = super(MoocDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = MoocEnrollForm(initial={'course':self.object})
        return context



# class MoocStudentCreateView(CreateView):
#     model = Student
#     template_name = "students/students/create.html"
#     form_class = MoocStudentForm
#     success_url = reverse_lazy("presentation:home")
#     def form_valid(self, form):
#         mooc = Mooc.objects.get(slug=self.kwargs['slug'])
#         form.instance.is_active = False
#         admin_message = "You have new student to register in Allianza \n {0} {1}"\
#         .format(form.instance.first_name, form.instance.last_name, form.instance.email )
#         admin_email = EmailMessage("New student in Allianza",
#                              admin_message,
#                              settings.EMAIL_HOST_USER,
#                              settings.ALLIANZA_ADMIN_EMAIL
#                             )
#         admin_email.send()
#         # message = client.messages.create(body="You have new student to register in Allianza \n {0} {1}"\
#         # .format(form.instance.first_name, form.instance.last_name, form.instance.email ),
#         #                                           to = settings.ALLIANZA_ADMIN_PHONE,  
#         #                                           from_= "+16466811807"
#         #                   )
#         # print(message.sid)
#         return super(MoocStudentCreateView, self).form_valid(form)




class MoocStudentByProgram(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "users.is_allianzadmin"
    model = User
    template_name = "moocs/mooc/moocstudent_list.html"
    context_object_name = "students"
    def get_context_data(self, **kwargs):
        context = super(MoocStudentByProgram, self).get_context_data(**kwargs)
        mooc = Mooc.objects.get(slug=self.kwargs['slug'])
        registreds = mooc.students.all()
        context['registreds'] = registreds.order_by('pk')
        context['mooc'] = Mooc.objects.get(slug=self.kwargs['slug'])
        return context


class ActivateMoocStudentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "users.is_allianzadmin"
    def get(self, request, *args, **kwargs):
        student= get_object_or_404(User, pk=kwargs['pk'])
        if student.is_active:
            student.is_active = False
        else:
            student.is_active = True
        student.save()
        return redirect("moocs:mooc-student", slug=kwargs['slug'])



class StudentEnrollMoocView(LoginRequiredMixin, FormView):
    course = None
    form_class = MoocEnrollForm
    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        user = self.request.user
        if not user.groups:
            user.is_active = False
        elif user.groups != "superadmin":
            user.is_active = True
        user.save()
        return super(StudentEnrollMoocView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('moocs:mooc-succes-registration')


class SuccessRegistration(TemplateView):
    template_name = "moocs/mooc/success.html"


class StudentMoocListView(LoginRequiredMixin, ListView):
    model = Mooc
    template_name = 'moocs/mooc/student_mooc_list.html'
    context_object_name = "student_moocs"
    def get_queryset(self):
        qs = super(StudentMoocListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentMoocDetailView(LoginRequiredMixin, DetailView):
    model = Mooc
    template_name = 'moocs/mooc/student_mooc_detail.html'

    def get_queryset(self):
        qs = super(StudentMoocDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super(StudentMoocDetailView,self).get_context_data(**kwargs)
        mooc = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = mooc.mooc_modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = mooc.mooc_modules.all()[0]
        return context


class DomainDetailView(DetailView):
    model = Category
    context_object_name = "domain"
    template_name = "moocs/domain/details.html"
    def get_context_data(self, **kwargs):
        context = super(DomainDetailView, self).get_context_data(**kwargs)
        context['domains'] = Category.objects.order_by('name')
        domain = Category.objects.get(slug = self.kwargs['slug'])
        context['disciplines'] = Discipline.objects.filter(domain = domain).order_by('name')
        context['moocs'] = Mooc.objects.filter(discipline__domain = domain)
        return context

