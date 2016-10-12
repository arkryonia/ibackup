# @Author: iker
# @Date:   Tuesday, May 17th 2016, 11:26:41 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   iker
# @Last modified time: Tuesday, May 17th 2016, 3:45:20 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

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

from .models import Domain, Option, Speciality


class DomainListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required='users.is_scolar'
    context_object_name = 'domains'
    model = Domain
    ordering = 'name'
    template_name = 'programs/domain/list.html'



class DomainCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required='users.is_scolar'
    model = Domain
    fields = ['name_en', 'name_fr']
    success_url = reverse_lazy('programs:domain-list')
    template_name = 'programs/domain/create.html'


class DomainUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required='users.is_scolar'
    model = Domain
    fields = ['name_en', 'name_fr']
    success_url = reverse_lazy('programs:domain-list')
    template_name = 'programs/domain/update.html'


class OptionListView(LoginRequiredMixin, PermissionRequiredMixin,  ListView):
    permission_required = 'users.is_scolar'
    context_object_name = 'options'
    model = Option
    template_name = 'programs/option/list.html'

    def get_queryset(self):
        domain = Domain.objects.get(pk=self.kwargs['domain_pk'])
        return Option.objects.filter(domain=domain).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(OptionListView, self).get_context_data(**kwargs)
        context['domain'] = Domain.objects.get(pk=self.kwargs['domain_pk'])
        return context


class OptionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Option
    fields = ['name_en','name_fr','domain',]
    template_name = 'programs/option/create.html'

    def get_success_url(self):
        return reverse_lazy('programs:option-list', args=self.kwargs['domain_pk'])


    def get_context_data(self, **kwargs):
        context = super(OptionCreateView, self).get_context_data(**kwargs)
        context['domain'] = Domain.objects.get(pk=self.kwargs['domain_pk'])
        return context

    def form_valid(self, form):
        # form.instance = form.save(commit=False)
        domain = Domain.objects.get(pk=self.kwargs['domain_pk'])
        form.instance.domain = domain
        return super(OptionCreateView, self).form_valid(form)


class OptionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Option
    fields = ['name_en','name_fr','domain',]
    template_name = 'programs/option/update.html'

    def get_success_url(self):
        return reverse_lazy('programs:option-list', args=self.kwargs['domain_pk'])



# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW


class SpecialityListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_scolar'
    context_object_name = 'specialities'
    model = Speciality
    template_name = 'programs/speciality/list.html'

    def get_queryset(self):
        option = Option.objects.get(pk=self.kwargs['option_pk'])
        return Speciality.objects.filter(option=option).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(SpecialityListView, self).get_context_data(**kwargs)
        context['domain'] = Domain.objects.get(pk=self.kwargs['domain_pk'])
        context['option'] = Option.objects.get(pk=self.kwargs['option_pk'])
        return context


class SpecialityCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Speciality
    fields = ['name_en','name_fr','option']
    template_name = 'programs/speciality/create.html'

    def get_success_url(self):
        return reverse_lazy('programs:speciality-list', kwargs={
                'domain_pk': self.kwargs['domain_pk'],
                'option_pk': self.kwargs['option_pk']
            }
        )


    def get_context_data(self, **kwargs):
        context = super(SpecialityCreateView, self).get_context_data(**kwargs)
        context['option'] = Option.objects.get(pk=self.kwargs['option_pk'])
        return context

    def form_valid(self, form):
        # form.instance = form.save(commit=False)
        option = Option.objects.get(pk=self.kwargs['option_pk'])
        form.instance.option = option
        return super(SpecialityCreateView, self).form_valid(form)


class SpecialityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Speciality
    fields = ['name_en','name_fr','option']
    template_name = 'programs/speciality/update.html'

    def get_success_url(self):
        return reverse_lazy('programs:speciality-list', kwargs={
                'domain_pk': self.kwargs['domain_pk'],
                'option_pk': self.kwargs['option_pk']
            }
        )

    def get_context_data(self, **kwargs):
        context = super(SpecialityUpdateView, self).get_context_data(**kwargs)
        context['option'] = Option.objects.get(pk=self.kwargs['option_pk'])
        return context
