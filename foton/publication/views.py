from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from foton.publication.models import Publication
from .forms import PostCreateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

### =================================================== ###

### ----------------   Backend Views   ---------------- ###

### =================================================== ###

class PublicationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_commercial'
    model = Publication
    success_url = reverse_lazy('publication:list-publication')
    template_name = 'publication/admin/create.html'
    form_class = PostCreateForm

class PublicationListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_commercial'
    context_object_name = 'publications'
    model = Publication
    template_name = 'publication/admin/list.html'

class PublicationDetailView(DetailView):
    permission_required = 'users.is_commercial'
    model = Publication
    template_name = 'publication/admin/detail.html'
    context_object_name = 'publication'

class PublicationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_commercial'
    model = Publication
    success_url = reverse_lazy('publication:list-publication')
    template_name = 'publication/admin/update.html'
    fields = ['category',
                'title_en',
                'title_fr',
                'content_en',
                'content_fr',
                'picture',
            ]


### =================================================== ###

### ----------------   Frontend Views   --------------- ###

### =================================================== ###

class NewsList(ListView):
    context_object_name = 'publications'
    model = Publication
    paginate_by = 7
    template_name = 'publication/public/news-list.html'

class EventsList(ListView):
    context_object_name = 'publications'
    model = Publication
    paginate_by = 7
    template_name = 'publication/public/events-list.html'

class PublicationDetail(DetailView):
    model = Publication
    template_name = 'publication/public/detail.html'
    context_object_name = 'publication'
