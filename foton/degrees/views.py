# @Author: drxos
# @Date:   Saturday, May 14th 2016, 10:22:38 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   sadjad
# @Last modified time: 2016-05-20T12:40:57+01:00
# @License: Copyright (c) Foton IT, All Right Reserved



from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, TemplateView, View


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from foton.programs.models import Option, Speciality

from .models import Bachelor, Master




# ------------------------------------------------------------------------------
class BachelorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_scolar'
    context_object_name = 'bachelors'
    model = Bachelor
    template_name = 'degrees/bachelors/list.html'

    def get_context_data(self, **kwargs):
        context = super(BachelorListView, self).get_context_data(**kwargs)
        # context['option'] = Option.objects.all()
        return context


class BachelorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Bachelor
    fields = ['option','pdf']
    success_url = reverse_lazy('degrees:bachelor-list')
    template_name = 'degrees/bachelors/create.html'

class BachelorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Bachelor
    fields = ('option','pdf')
    success_url = reverse_lazy('degrees:bachelor-list')
    template_name = 'degrees/bachelors/update.html'

#-------------------------------------------------------------------------------

class MasterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_scolar'
    context_object_name = 'masters'
    model = Master
    template_name = 'degrees/masters/list.html'


class MasterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Master
    fields = ['speciality','pdf']
    success_url = reverse_lazy('degrees:masters-list')
    template_name = 'degrees/masters/create.html'

class MasterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Master
    fields = ['speciality','pdf','pdf']
    success_url = reverse_lazy('degrees:masters-list')
    template_name = 'degrees/masters/update.html'

# ------------------------------------------------------------------------------

class BachelorFrontListView(ListView):
    queryset = Bachelor.objects.order_by('option')
    context_object_name = 'bachelors'
    #model = Bachelor
    template_name = 'degrees/bachelor_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(BachelorFrontListView, self).get_context_data(**kwargs)
    #     #context['option'] = Option.objects.all()
    #     return context

class MasterFrontListView(ListView):
    context_object_name = 'masters'
    model = Master
    template_name = 'degrees/masters_list.html'
