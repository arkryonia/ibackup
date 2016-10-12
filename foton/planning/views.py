from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from foton.planning.models import Planning, PlanningItem

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

### ----------------   Backend Views ---------------- ###

class PlanningCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = Planning
    success_url = reverse_lazy('planning:list-planning')
    template_name = 'planning/classes/create.html'
    fields = ['clazz',]


class PlanningListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_scolar'
    context_object_name = 'plannings'
    queryset = Planning.objects.all().order_by('clazz__name', 'clazz__level')
    template_name = 'planning/classes/list.html'


class PlanningUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = Planning
    template_name = 'planning/classes/update.html'
    success_url = reverse_lazy('planning:list-planning')
    fields = ['clazz',]


class PlanningDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'users.is_scolar'
    template_name = 'planning/classes/detail.html'
    model = Planning
    context_object_name = 'planning'

    def get_context_data(self, **kwargs):
        context = super(PlanningDetailView, self).get_context_data(**kwargs)
        planning = Planning.objects.get(pk=self.kwargs['pk'])
        context['items'] = PlanningItem.objects.filter(planning = planning).order_by('start')
        return context


class ItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_scolar'
    model = PlanningItem
    template_name = 'planning/items/create.html'
    fields = ['day','start','end','course','venue','planning',]
    success_url = reverse_lazy('planning:list-planning')

class ItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_scolar'
    model = PlanningItem
    success_url = reverse_lazy('planning:list-planning')
    template_name = 'planning/items/update.html'
    fields = ['day','start','end','course','venue','planning',]

class ItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'users.is_scolar'
    model = PlanningItem
    context_object_name = 'item'
    success_url = reverse_lazy('planning:list-planning')
    template_name = 'planning/items/delete.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDeleteView, self).get_context_data(**kwargs)
        item = PlanningItem.objects.get(pk=self.kwargs['pk'])
        return context

### ----------------   Public Views ---------------- ###


class PlanningPublicListView(ListView):
    context_object_name = 'plannings'
    queryset = Planning.objects.all().order_by('clazz__name', 'clazz__level')
    template_name = 'planning/public/list.html'

class PlanningPublicDetailView(DetailView):
    template_name = 'planning/public/detail.html'
    model = Planning
    context_object_name = 'planning'

    def get_context_data(self, **kwargs):
        context = super(PlanningPublicDetailView, self).get_context_data(**kwargs)
        planning = Planning.objects.get(pk=self.kwargs['pk'])
        context['items'] = PlanningItem.objects.filter(planning = planning).order_by('start')
        return context
