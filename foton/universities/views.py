from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, TemplateView, View, UpdateView
from django.views.generic.edit import FormMixin
from django.utils import timezone

from django.core.urlresolvers import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

from .forms import LecturerCreationForm, LecturerChangeForm
from foton.universities.models import Lecturer
from foton.degrees.models import Bachelor, Master


class LecturerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Lecturer
    form_class = LecturerCreationForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'

    def form_valid(self, form):
        form.instance = form.save(commit=True)
        lecturer = Group.objects.get(name="lecturer")
        form.instance.groups.add(lecturer)
        return super(LecturerCreateView, self).form_valid(form)

class LecturerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = Lecturer
    form_class = LecturerChangeForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'

class ActivateLecturerView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required='users.is_admin'
    def get(self, request, *args, **kwargs):
        lecturer = get_object_or_404(Lecturer, pk=kwargs['pk'])
        if lecturer.is_active:
            lecturer.is_active = False
        else:
            lecturer.is_active = True

        lecturer.save()
        print(lecturer.first_name)
        return redirect('staff:list-staff')