from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  View)
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import (LoginRequiredMixin,
										PermissionRequiredMixin
										)
from django.db.models import Q

from io import BytesIO
from reportlab.pdfgen import canvas

from foton.students.models import Class, Student, Registred
from foton.staff.models import Year

from .forms import RegistrationForm, StudentForm

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm,landscape

from django.conf import settings 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# =========================================================================

class ClassList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_scolar'
	queryset = Class.objects.order_by('level')
	template_name = 'students/classes/list.html'
	context_object_name = 'classes'

class ClassCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Class
    fields = ['name_en','name_fr', 'level', 'program']
    success_url = reverse_lazy('students:list-classes')
    template_name = 'students/classes/create.html'
    def form_valid(self, form):
        form.instance.full_name = form.instance.name + form.instance.level
        return super(ClassCreateView, self).form_valid(form)


class ClassUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Class
    fields = ['name_en','name_fr', 'level', 'program']
    success_url = reverse_lazy('students:list-classes')
    template_name = 'students/classes/update.html'
    def form_valid(self, form):
        form.instance.full_name = form.instance.name + form.instance.level
        return super(ClassUpdateView, self).form_valid(form)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==========================================================================


class StudentCreateView(CreateView):
    model = Student
    template_name = "students/students/create.html"
    form_class = StudentForm

    def form_valid(self, form):
        form.instance.is_active = False
        form.instance.student_type = 0
        return super(StudentCreateView, self).form_valid(form)


def student_list(request):
    if ('search' in request.GET):
        search = request.GET.get('search')
        year = Year.objects.filter(available = True)
        first_name = Q(first_name__icontains=search)
        last_name = Q(last_name__icontains=search)
        ref = Q(id__icontains=search)
        students = Student.objects.filter(first_name | last_name | ref).filter(year=year, is_active=False)
    else:
        students = Student.objects.filter(is_active=False)
    return render(request, 'students/students/list.html', {'students':students})

# class StudentUpdateView(UpdateView):
#     model = Student
#     template_name = "students/students/create.html"
#     fields = [  'gender',
#                 'first_name',
#                 'last_name',
#                 'marital_status',
#                 'username',
#                 'year',
#                 'student_type',
#                 'origin',
#                 'national_Id',
#                 'birth_date',
#                 'birth_venue',
#                 'email',
#                 'phone',
#                 'residence'
#                 'sponsor_full_name',
#                 'sponsor_relationship',
#                 'sponsor_address',
#                 'sponsor_occupation',
#                 'sponsor_phone',
#                 'sponsor_email'
#             ]
#     success_url = reverse_lazy("students:students-list")

class StudentDetailView(DetailView):
    model = Student
    template_name = "students/students/success.html"
    context_object_name = "student"

class AdmissionForm(View):
    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['pk'])
        IMG = str(settings.ROOT_DIR('foton/theme/static/theme/img/fiche1.jpg'))
        IMG2 = str(settings.ROOT_DIR('foton/theme/static/theme/img/fiche2.jpg'))
        IMG3 = str(settings.ROOT_DIR('foton/theme/static/theme/img/fiche3.jpg'))
        IMG4 = str(settings.ROOT_DIR('foton/theme/static/theme/img/fiche4.jpg'))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="registration_form.pdf"'
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.setTitle("Registration Form.pdf")

        p.drawInlineImage(IMG, 0, 0, width=600,height=850)

        p.setFont("Helvetica", 14)
        p.drawString(160, 730, "Academic: {0} / Reference Number:{1}".format(student.year, format(student.id)))

        p.setFont("Helvetica", 16)  
        p.drawString(240, 588.5, str(student.last_name))
        p.drawString(150, 551.5, str(student.first_name))
        if student.gender == 0:
            g = "Female"
        else:
            g = "Male"
        p.drawString(120, 514, g)

        p.drawString(130, 476, str(student.birth_date))
        p.drawString(150, 438, str(student.birth_venue))
        p.drawString(120, 400, str(student.residence))
        p.drawString(130, 362, str(student.phone))
        p.drawString(110, 324, str(student.email))
        p.drawString(130, 287, str(student.origin.name))
        p.drawString(135, 249, str(student.national_Id))
        if student.marital_status == 0:
            m = "Single"
        else:
            m = "Maried"
        p.drawString(150, 210, str(m))
        p.showPage()

        # Page 2
        p.drawInlineImage(IMG2, 0, 0, width=600,height=850)
        p.showPage()

        # Page 3
        p.drawInlineImage(IMG3, 0, 0, width=600,height=850)
        p.drawString(290, 525, str(student.sponsor_full_name))
        p.drawString(220, 492.5, str(student.sponsor_relationship))
        p.drawString(180, 459.5, str(student.sponsor_address))
        p.drawString(130, 426.5, str(student.sponsor_occupation))
        p.drawString(125, 393.5, str(student.sponsor_phone))
        p.drawString(110, 360.5, str(student.sponsor_email))
        p.showPage()

        # Page 4
        p.drawInlineImage(IMG4, 0, 0, width=600,height=850)
        p.showPage()
        p.save()

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==========================================================================

class RegistredListByClassView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_scolar'
	queryset = Class.objects.order_by('id')
	template_name = "students/registred/class_list.html"
	context_object_name = 'classes'

class RegistredListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_scolar'
    queryset = Registred.objects.order_by('student')
    template_name = "students/registred/list.html"
    def get_context_data(self, **kwargs):
        context = super(RegistredListView, self).get_context_data(**kwargs)
        clazz = Class.objects.get(pk =self.kwargs['pk'])
        year = Year.objects.filter(available = True)
        registreds = Registred.objects.filter(clazz=clazz, student__year=year)
        context["registreds"] = registreds.order_by("student__last_name")
        return context

class RegistredCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Registred
    template_name = "students/registred/create.html"
    fields = ['clazz']
    success_url = reverse_lazy('students:list-class')

    def form_valid(self, form):
        # student = form.cleaned_data['student'].pk
        form.instance.matricule = form.instance.number()+1
        student = Student.objects.get(pk=self.kwargs['pk'])
        form.instance.student = student
        registred = get_object_or_404(Student, pk = student)
        registred.is_active = True
        form.instance.matricule_number = form.instance.matricul()
        registred.save()
        subject = "Registration completed"
        message = "Dear {0},\nMatricule {1},\n\nOFFER OF PROVISIONAL ADMISSION.\n\nIn reference to your application for an admission as an undergraduate student of IRGIB-Africa, we are delighted to inform you that you have been offered provisional admission to undertake the following Class {2}.All credentials ( Originals ) will be checked during registration. The University reserves the right to withdraw this admission if it is discovered that any of your claims in the application or documents submitted are false.\n\nThe rules and regulations governing the University must be strictly adhered to. Please contact your academic advisor for information on your course and academic information.\n\nAs an indication of your acceptance of this provincial offer of admission, you are required to complete your fees payment and all registration processes within one month of receipt of this letter.\n\nFor more information regarding registration, our programs and admission, please visit the school’s website : http://www.irgibafrica.university or by contacting us at contact@irgibafrica.university.\n\nCongratulations on receiving an offer into IRGIB-Africa University. If you have any questions or would like any further information at this time, please feel free to contact us. We look forward to welcoming you.\n \n \nYours sincerely, \n \n \nSimon AMOUSSOU-GUENOU \n\nRegistar.".format(form.instance.student, form.instance.matricule_number, form.instance.clazz)
        email = EmailMessage(subject,
                             message,
                             settings.EMAIL_HOST_USER,
                             [registred.email]
                            )
        email.send()
        return super(RegistredCreateView, self).form_valid(form)


class RegistredUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_scolar'
	model = Registred
	template_name = "students/registred/update.html"
	fields = ['student', 'clazz', 'image']
	def get_success_url(self):
		return reverse_lazy('students:list-class')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_scolar'
	model = Student
	template_name = "students/registred/student_update.html"
	fields = [  'gender',
                'first_name',
                'last_name',
                'marital_status',
                'username',
                'year',
                'student_type',
                'origin',
                'national_Id',
                'birth_date',
                'birth_venue',
                'email',
                'phone',
                'residence',
                'sponsor_full_name',
                'sponsor_relationship',
                'sponsor_address',
                'sponsor_occupation',
                'sponsor_phone',
                'sponsor_email'
            ]
	success_url = reverse_lazy('students:list-class')


class ActivateRegistredView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "users.is_scolar"
    def get(self, request, *args, **kwargs):
        registred = get_object_or_404(Student, pk=kwargs['pk'])
        if registred.is_active:
            registred.is_active = False
        else:
            registred.is_active = True
        registred.save()
        return redirect('students:list-class')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# =====================================================================================

class RegistrationView(LoginRequiredMixin, UpdateView):
    template_name = "students/registred/registration.html"
    success_url = reverse_lazy('students:list-class')
    model = Registred
    def form_valid(self, form):
        user = self.request.user
        registred = Registred.objects.filter(student = user).get(pk=self.kwargs['registred_pk'])
        form.instance.registred = registred
        form.instance.clazz = form.cleaned_data['clazz']
        return super(RegistrationView, self).form_valid(form)