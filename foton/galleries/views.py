from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse_lazy, reverse

from django.utils.text import slugify

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from foton.galleries.models import Gallery, Photo
from foton.galleries.forms import GalleryCreationForm


# ===============================================
# PUBLIC VIEWS
# ===============================================

class GalleryListView(ListView):
    context_object_name = 'galleries'
    model = Gallery
    template_name = 'galleries/list-galleries.html'

class PhotoListbyGallery(DetailView):
    model = Gallery
    template_name = 'galleries/list-photos.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super(PhotoListbyGallery, self).get_context_data(**kwargs)
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        context['photos'] = Photo.objects.filter(gallery = gallery)
        return context

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'galleries/detail-photo.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        return context


# ===============================================
# ADMIN VIEWS
# ===============================================

class GalleryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_commercial'
    model = Gallery
    form_class = GalleryCreationForm
    success_url = reverse_lazy('galleries:admin-list-galleries')
    template_name = 'galleries/admin/create.html'

    def form_valid(self, form):
        form.instance = form.save()
        form.instance.slug = slugify(form.instance.name)
        return super(GalleryCreateView, self).form_valid(form)

class GalleryAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.is_commercial'
    context_object_name = 'galleries'
    model = Gallery
    template_name = 'galleries/admin/list.html'

class GalleryAdminDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'users.is_commercial'
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'galleries/admin/detail.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryAdminDetailView, self).get_context_data(**kwargs)
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        context['photos'] = Photo.objects.filter(gallery = gallery)
        return context

class GalleryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_commercial'
    model = Gallery
    form_class = GalleryCreationForm
    template_name = 'galleries/admin/update.html'
    success_url = reverse_lazy('galleries:admin-list-galleries')

    def get_context_data(self, **kwargs):
        context = super(GalleryUpdateView, self).get_context_data(**kwargs)
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        return context

class GalleryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'users.is_commercial'
    model = Gallery
    template_name = 'galleries/admin/delete.html'
    context_object_name = 'gallery'
    success_url = reverse_lazy('galleries:admin-list-galleries')

    def get_context_data(self, **kwargs):
        context = super(GalleryDeleteView, self).get_context_data(**kwargs)
        gallery = Gallery.objects.get(slug=self.kwargs['slug'])
        return context

class PhotoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'users.is_commercial'
    model = Photo
    fields = ['gallery','title','image']
    success_url = reverse_lazy('galleries:add-photo')
    template_name = 'galleries/admin/create-photo.html'

class AdminPhotoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'users.is_commercial'
    model = Photo
    template_name = 'galleries/admin/detail-photo.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super(AdminPhotoDetailView, self).get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        return context

class PhotoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'users.is_commercial'
    model = Photo
    template_name = 'galleries/admin/update-photo.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PhotoUpdateView, self).get_context_data(**kwargs)
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('galleries:admin-detail-photo', kwargs={
                'slug': self.kwargs['slug'],
                'pk': self.kwargs['pk']
            }
        )
