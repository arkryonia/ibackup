from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from foton.ejournal.models import Magasine, Sommary

# ==================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Backend<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ==================================================================

class MagasineListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
	permission_required = 'users.is_commercial'
	model = Magasine
	template_name = "ejournal/magasine/list.html"
	context_object_name = "magasines"


class MagasineCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = 'users.is_commercial'
	model = Magasine
	template_name = "ejournal/magasine/create.html"
	fields = ['title', 'image', 'abstract', 'issn', 'issue', 'shop_link', 'file', 'free']
	success_url = reverse_lazy("ejournal:list-magasine")

class MagasineUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_commercial'
	model = Magasine
	fields = ['title', 'image', 'abstract', 'issn', 'issue', 'shop_link', 'file', 'free']
	success_url = reverse_lazy('ejournal:list-magasine')
	template_name = "ejournal/magasine/update.html"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class MagasineDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
	permission_required = 'users.is_commercial'
	model = Magasine
	context_object_name = 'magasine'
	template_name = 'ejournal/sommary/list.html'

	def get_context_data(self, **kwargs):
		context = super(MagasineDetailView, self).get_context_data(**kwargs)
		magasine = Magasine.objects.get(pk=self.kwargs['pk'])
		context['sommaries'] = Sommary.objects.filter(magasine=magasine)
		return context


class SommaryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = 'users.is_commercial'
	model = Sommary
	fields = [ 'title', 'author', 'page', 'keywords']
	template_name = 'ejournal/sommary/create.html'
	success_url = reverse_lazy('ejournal:list-magasine')

	def form_valid(self, form):
		magasine = Magasine.objects.get(pk=self.kwargs['pk'])
		form.instance.magasine = magasine
		return super(SommaryCreateView, self).form_valid(form)

class SommaryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	permission_required = 'users.is_commercial'
	model = Sommary
	fields = ['magasine', 'title', 'author', 'page', 'keywords']
	template_name = 'ejournal/sommary/update.html'
	success_url = reverse_lazy('ejournal:list-magasine')
	def get_context_data(self, **kwargs):
	    context = super(SommaryUpdateView, self).get_context_data(**kwargs)
	    context['sommary'] = Sommary.objects.get(pk = self.kwargs['pk'])
	    return context


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==============================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class MagasinePubListView(ListView):
	queryset = Magasine.objects.order_by('-id')
	template_name = 'ejournal/list.html'
	context_object_name = 'magasines'
	paginate_by = 5
	def get_context_data(self, **kwargs):
	    context = super(MagasinePubListView, self).get_context_data(**kwargs)
	    context['mags'] = Magasine.objects.order_by('-id')[:20]
	    return context

class MagasinePubDetail(DetailView):
	model = Magasine
	context_object_name = 'magasine'
	template_name = 'ejournal/detail.html'
	def get_context_data(self, **kwargs):
		context = super(MagasinePubDetail, self).get_context_data(**kwargs)
		magasine = Magasine.objects.get(pk=self.kwargs['pk'])
		context['sommaries'] = Sommary.objects.filter(magasine=magasine).order_by('id')
		return context
