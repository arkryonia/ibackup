# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals



# ============================================================================




# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.text import slugify


# ============================================================================




# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------
from braces.views import LoginRequiredMixin, PermissionRequiredMixin



# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Category, Post


# ============================================================================


class CategoryCreateView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			CreateView):
	"""
		This class allows admin users to create categories
	"""
	model = Category
	success_url = reverse_lazy('cicanon:list-cats')
	template_name = 'cicanon/theme/categories/create.html'
	permission_required = 'users.is_commercial'
	raise_exception = True
	fields = ['name_en','name_fr',]


	def dispatch(self, *args, **kwargs):
		return super(CategoryCreateView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		form.instance.slug_en = slugify(form.instance.name_en)
		form.instance.slug_fr = slugify(form.instance.name_fr)
		return super(CategoryCreateView, self).form_valid(form)


class CategoryListView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			ListView):
	"""
		This class aims to list categories.
	"""
	model = Category
	template_name = 'cicanon/theme/categories/list.html'
	context_object_name = 'cats'
	permission_required = 'users.is_commercial'
	raise_exception = True


class CategoryPublicListView(ListView):
	"""
		This class aims to list categories.
	"""
	model = Category
	template_name = 'cicanon/theme/categories/list-public.html'
	context_object_name = 'cats'
	raise_exception = True


class CategoryUpdateView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			UpdateView):
	"""
		This class aims to update a category object
	"""
	model = Category
	fields = ['name_en','name_fr']
	success_url = reverse_lazy('cicanon:list-cats')
	template_name = 'cicanon/theme/categories/update.html'
	permission_required = 'users.is_commercial'
	raise_exception = True

	def form_valid(self, form):
		form.instance.slug_en = slugify(form.instance.name_en)
		form.instance.slug_fr = slugify(form.instance.name_fr)
		return super(CategoryUpdateView, self).form_valid(form)


class CatPostListView(DetailView):
	model = Category
	template_name = 'cicanon/theme/categories/detail-public.html'
	context_object_name = 'category'

	def get_context_data(self, **kwargs):
		context = super(CatPostListView, self).get_context_data(**kwargs)
		category = Category.objects.get(slug=self.kwargs['slug'])
		context['posts'] = Post.objects.filter(category = category)
		return context



# ============================================================================


class PostCreateView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			CreateView):
	"""
		This class allows admin users to create categories
	"""
	model = Post
	success_url = reverse_lazy('cicanon:list-posts')
	template_name = 'cicanon/theme/posts/create.html'
	permission_required = 'users.is_commercial'
	raise_exception = True
	fields = ['title_fr','title_en','category','content_fr','content_en','picture']


	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.slug_fr = slugify(form.instance.title_fr)
		form.instance.slug_en = slugify(form.instance.title_en)
		return super(PostCreateView, self).form_valid(form)


class PostListView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			ListView):
	"""
		This class aims to list categories.
	"""
	model = Post
	 # paginate_by = 2
	template_name = 'cicanon/theme/posts/list.html'
	context_object_name = 'posts'
	permission_required = 'users.is_commercial'
	raise_exception = True


	def get_queryset(self):
		# queryset = super(PostListView, self).get_queryset()
		user = self.request.user
		queryset = user.post_set.all()
		return queryset


class PostDetailView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			DetailView):
	"""
		This class aims to list categories.
	"""
	model = Post
	template_name = 'cicanon/theme/posts/detail.html'
	context_object_name = 'post'
	permission_required = 'users.is_commercial'
	raise_exception = True


class PostUpdateView(
			LoginRequiredMixin,
			PermissionRequiredMixin,
			UpdateView):
	"""
		This class aims to update a category object
	"""
	model = Post
	fields = ['title_fr','title_en','category','content_fr','content_en','picture']
	success_url = reverse_lazy('cicanon:list-posts')
	template_name = 'cicanon/theme/posts/create.html'
	permission_required = 'users.is_commercial'
	raise_exception = True

	def form_valid(self, form):
		form.instance.slug_fr = slugify(form.instance.title_fr)
		form.instance.slug_en = slugify(form.instance.title_en)
		return super(PostUpdateView, self).form_valid(form)


class PostPublicListView(ListView):
	"""
		This class aims to list categories.
	"""
	model = Post
	template_name = 'cicanon/theme/posts/list-public.html'
	context_object_name = 'posts'
	queryset = Post.objects.filter(pub=True).order_by('-created')


class PostPublicDetailView(DetailView):
	model = Post
	template_name = 'cicanon/theme/posts/detail-public.html'
	context_object_name = 'post'

# ============================================================================


@permission_required('users.is_commercial')
def pub_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if post.pub :
		post.pub = False
	else :
		post.pub = True
	post.save()
	return redirect('cicanon:list-posts')
