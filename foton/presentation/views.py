# @Author: drxos
# @Date:   Tuesday, May 10th 2016, 6:07:58 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 12:34:11 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django.shortcuts import render


from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import UpdateView, CreateView

from foton.presentation.models import About, Item

class HomeTemplateView(TemplateView):
    template_name = 'presentation/home.html'


class ContactView(TemplateView):
    template_name = 'theme/contact.html'


class AboutTemplateView(TemplateView):
    template_name = 'presentation/about.html'


class AboutView(View):
    template_name = 'presentation/about.html'

    def get(self, request):
        about = About()

        try:
            about = About.objects.first()
        except Exception as e:
            raise e


        items = Item.objects.filter(about=about).order_by('id')

        return render(request, self.template_name, {
                "about":about, "items":items
            })

    def post(self, request):
        pass


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# =======================================================================
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class AboutCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'users.is_commercial'
    model = About
    fields = ['title_en','title_fr','intro_en','intro_fr','image']
    template_name = 'presentation/about/create.html'
    success_url = reverse_lazy('presentation:list-about')

class AboutListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'users.is_commercial'
    queryset = About.objects.order_by('id')
    context_object_name = 'abouts'
    template_name = 'presentation/about/list.html'


class AboutUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'users.is_commercial'
    model = About
    fields = ['title_en','title_fr','intro_en','intro_fr','image']
    template_name = 'presentation/about/update.html'
    success_url = reverse_lazy('presentation:list-about')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ======================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class ItemListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'users.is_commercial'
    queryset = Item.objects.all()
    template_name = 'presentation/item/list.html'
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        about = About.objects.get(pk = self.kwargs['about_pk'])
        context['items'] = Item.objects.filter(about = about)
        return context

class ItemCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'users.is_commercial'
    model = Item
    fields = ['title_en','title_fr','description_en','description_fr','image']
    template_name = 'presentation/item/create.html'

    def get_success_url(self):
        return reverse_lazy('presentation:list-items', kwargs={
               'about_pk': self.kwargs['about_pk'],
            }
        )

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['about'] = About.objects.get(pk=self.kwargs['about_pk'])
        return context

    def form_valid(self, form):

        about = About.objects.get(pk=self.kwargs['about_pk'])
        form.instance.about = about
        return super(ItemCreateView, self).form_valid(form)

class ItemUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'users.is_commercial'
    model = Item
    fields = [  'about_en',
                'about_fr',
                'title_en',
                'title_fr',
                'description_en',
                'description_fr',
                'image'
            ]
    template_name = 'presentation/item/update.html'
    success_url = reverse_lazy('presentation:list-about')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# =====================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
