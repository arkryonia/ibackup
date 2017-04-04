import csv
from django.conf import settings
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import Http404, HttpResponse

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, View)
from django.views.generic.edit import FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Bachelor, Master, Student

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A3, A4, A2, letter
from reportlab.lib.colors import HexColor
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

from datetime import datetime

class GraduationHome(TemplateView):
    template_name = "graduation/home.html"


class GraduationSuccess(TemplateView):
    template_name = "graduation/success.html"


class BachelorCreateView(CreateView):
    model = Bachelor
    template_name = "graduation/create.html"
    fields = [ 'surname',
    			'name',
    			'gender',
    			'date_of_birth',
                'birth_venue',
    			'option',
			]
    success_url = reverse_lazy('graduation:graduation-success')
    def form_valid(self, form):
    	year ="15"
    	g = form.instance.gender
    	s_type = "00"
    	student = Student.objects.order_by('id')
    	total_student = Student.objects.count()
    	if (g == "Female"):
    		gender = "00"
    	else:
    		gender = "01"

    	if total_student==0:
    		form.instance.number = 163
    	else:
    		form.instance.number += Student.objects.last().number

    	m = str(form.instance.number)
    	if (len(m)<4):
    		mat = "{0}".format("0"*(4-len(m))+m)
    	else:
    		mat = m
    	form.instance.matricule_number = "{0}{1}{2}{3}".format(gender, s_type, year, mat)
    	return super(BachelorCreateView, self).form_valid(form)


class MasterCreateView(CreateView):
    model = Master
    template_name = "graduation/create.html"
    fields = [ 'surname',
                'name',
                'gender',
                'date_of_birth',
                'birth_venue',
                'speciality',
            ]
    success_url = reverse_lazy('graduation:graduation-success')
    def form_valid(self, form):
        year ="15"
        g = form.instance.gender
        s_type = "00"
        student = Student.objects.order_by('id')
        total_student = Student.objects.count()
        if (g == "Female"):
            gender = "00"
        else:
            gender = "01"

        if total_student==0:
            form.instance.number = 163
        else:
            form.instance.number = Student.objects.last().number + 1

        m = str(form.instance.number)
        if (len(m)<4):
            mat = "{0}".format("0"*(4-len(m))+m)
        else:
            mat = m
        form.instance.matricule_number = "{0}{1}{2}{3}".format(gender, s_type, year, mat)
        return super(MasterCreateView, self).form_valid(form)


class AdminBachelorCreate(LoginRequiredMixin, CreateView):
    model = Bachelor
    template_name = "graduation/bachelor_create.html"
    fields = [ 'surname',
                'name',
                'gender',
                'date_of_birth',
                'birth_venue',
                'option',
            ]
    success_url = reverse_lazy('presentation:home')
    def form_valid(self, form):
        year ="15"
        g = form.instance.gender
        s_type = "00"
        student = Student.objects.order_by('id')
        total_student = Student.objects.count()
        if (g == "Female"):
            gender = "00"
        else:
            gender = "01"

        if total_student==0:
            form.instance.number = 163
        else:
            form.instance.number = Student.objects.last().number

        m = str(form.instance.number)
        if (len(m)<4):
            mat = "{0}".format("0"*(4-len(m))+m)
        else:
            mat = m
        form.instance.matricule_number = "{0}{1}{2}{3}".format(gender, s_type, year, mat)
        return super(AdminBachelorCreate, self).form_valid(form)

class AdminMasterCreateView(LoginRequiredMixin, CreateView):
    model = Master
    template_name = "graduation/create.html"
    fields = [ 'surname',
                'name',
                'gender',
                'date_of_birth',
                'birth_venue',
                'speciality',
            ]
    success_url = reverse_lazy('presentation:home')
    def form_valid(self, form):
        year ="15"
        g = form.instance.gender
        s_type = "00"
        student = Student.objects.order_by('id')
        total_student = Student.objects.count()
        if (g == "Female"):
            gender = "00"
        else:
            gender = "01"

        if total_student==0:
            form.instance.number = 163
        else:
            form.instance.number += Student.objects.last().number

        m = str(form.instance.number)
        if (len(m)<4):
            mat = "{0}".format("0"*(4-len(m))+m)
        else:
            mat = m
        form.instance.matricule_number = "{0}{1}{2}{3}".format(gender, s_type, year, mat)
        return super(AdminMasterCreateView, self).form_valid(form)




class BachelorUpdateView(LoginRequiredMixin, UpdateView):
    model = Bachelor
    template_name = "graduation/bachelor_update.html"
    fields = [ 'surname',
    			'name',
    			'gender',
    			'date_of_birth',
                'birth_venue',
    			'option',
    			'defense_score',
    			'defense_score',
			]
    success_url = reverse_lazy('graduation:bachelor-list')

    def form_valid(self, form):
    	m = form.instance.defense_score
    	if (m<10):
    		form.instance.class_of_degree = "Third Class (HON)"
    	elif(m>=10 and m<12):
    		form.instance.class_of_degree = "Second Class (HON) Lower Division"
    	elif(m>=12 and m<=16.79):
    		form.instance.class_of_degree = "Second Class (HON) Upper Division"
    	elif(m>16.79):
    		form.instance.class_of_degree = "First Class (HON)"

    	m = form.instance.defense_score
    	if (m==12 and m<13):
    		form.instance.mention = "PASSABLE"
    	elif(m>=13 and m<15):
    		form.instance.mention = "ASSEZ BIEN"
    	elif(m>=15 and m<17):
    		form.instance.mention = "BIEN"
    	elif(m>=17 and m<18):
    		form.instance.mention = "TRES BIEN"
    	elif(m>=18 and m<19):
    		form.instance.mention = "HONORABLE"
    	elif(m>=19 and m<19.5):
    		form.instance.mention = "TRES HONORABLE"
    	elif(m>19.5):
    		form.instance.mention = "EXECELLENT"
    	return super(BachelorUpdateView, self).form_valid(form)

class BachelorList(LoginRequiredMixin, ListView):
    model = Bachelor
    template_name = "bachelor_list.html"
    context_object_name = "bachelors"
    def get_context_data(self, **kwargs):
        context = super(BachelorList, self).get_context_data(**kwargs)
        context['bachelors'] = Bachelor.objects.filter(is_print = False).order_by('surname')
        return context


class BachelorCsvList(View):
    def get(self, request):
        bachelors = Bachelor.objects.filter(is_print=False)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bachelor.csv"'
        writer = csv.writer(response)
        for bachelor in bachelors:
            name = "{0} {1}".format(bachelor.surname, bachelor.name)
            date_of_birth = str(bachelor.date_of_birth)
            birth_venue = str(bachelor.birth_venue)
            option_fr = str(bachelor.option.name_fr)
            mention = str(bachelor.mention)
            option_en = str(bachelor.option.name_en)
            class_of_degree = str(bachelor.class_of_degree)
            matricule_number = "matricule : " + str(bachelor.matricule_number)
            writer.writerow([
                name, 
                date_of_birth, 
                birth_venue, 
                option_fr, 
                mention, 
                option_en,
                class_of_degree,
                matricule_number
            ])
            bachelor.is_print =True
            bachelor.save()
        return response
