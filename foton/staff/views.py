#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Thursday, May 19th 2016, 12:45:47 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 12:57:48 am
# @License: Copyright (c) Foton IT, All Right Reserved



# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import Group

from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    View
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------

from foton.users.models import User

# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Scolar, Commercial, Year
from .forms import (
    ScolarCreationForm,
    ScolarChangeForm,
    CommercialCreationForm,
    CommercialChangeForm
)

# ============================================================================

class StaffHome(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required='users.is_scolar' or 'users.is_commercial' or 'users.is_admin'
    template_name = 'theme/backend/home.html'


class ScolarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Scolar
    form_class = ScolarCreationForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'

    def form_valid(self, form):
        form.instance = form.save(commit=True)
        scolar = Group.objects.get(name="scolar")
        form.instance.groups.add(scolar)
        return super(ScolarCreateView, self).form_valid(form)

class ScolarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = Scolar
    form_class = ScolarChangeForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'



class CommercialCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_admin'
    model = Commercial
    form_class = CommercialCreationForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'

    def form_valid(self, form):
        form.instance = form.save(commit=True)
        commercial = Group.objects.get(name="commercial")
        form.instance.groups.add(commercial)
        return super(CommercialCreateView, self).form_valid(form)


class CommercialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_admin'
    model = Commercial
    form_class = CommercialChangeForm
    success_url = reverse_lazy('staff:list-staff')
    template_name = 'staff/create.html'


class StaffListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_admin'
    context_object_name = 'scolars'
    model = Scolar
    ordering = 'last_name'
    template_name = 'staff/list.html'

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['commercials'] = Commercial.objects.order_by('last_name')
        return context


class ActivateScolarView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required='users.is_admin'
    def get(self, request, *args, **kwargs):
        scolar = get_object_or_404(Scolar, pk=kwargs['pk'])
        if scolar.is_active:
            scolar.is_active = False
        else:
            scolar.is_active = True

        scolar.save()
        print(scolar.first_name)
        return redirect('staff:list-staff')

    def post(self, request):
        pass

class ActivateCommercialView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required='users.is_admin'
    def get(self, request, *args, **kwargs):
        commercial = get_object_or_404(Commercial, pk=kwargs['pk'])
        if commercial.is_active:
            commercial.is_active = False
        else:
            commercial.is_active = True

        commercial.save()
        print(commercial.first_name)
        return redirect('staff:list-staff')

    def post(self, request):
        pass

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class YearCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'users.is_admin'
    model = Year
    fields = "__all__"
    template_name = 'staff/year/create.html'
    success_url = reverse_lazy('staff:list-year')

class YearUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'users.is_admin'
    model = Year
    fields = "__all__"
    template_name = 'staff/year/update.html'
    success_url = reverse_lazy('staff:list-year')

class YearListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'users.is_admin'
    queryset = Year.objects.order_by('id')
    context_object_name = 'years'
    template_name = 'staff/year/list.html'
