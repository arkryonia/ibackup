
from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import  views


urlpatterns = [
	
	url(
		regex = r'(?P<slug>[\w-]+)/details/$',
		view = views.DomainDetailView.as_view(),
		name = 'domain_detail'
	),

	url(
		regex = r'(?P<pk>[\w-]+)/mooc/$',
		view = views.MoocDetailView.as_view(),
		name = 'mooc_detail'
	),

	url(
		regex = r'enroll-course/$',
		view = views.StudentEnrollMoocView.as_view(),
		name = 'student_enroll_mooc'
	),

	url(
		regex = r'my-specialities/$',
		view = views.StudentMoocListView.as_view(),
		name = 'student_mooc_list_view'
	),

	url(
		regex = r'my-specialities/(?P<pk>[\w-]+)/$',
		view = views.StudentMoocDetailView.as_view(),
		name = 'student_mooc_view'
	),

	url(
		regex = r'my-specialities/(?P<pk>[\w-]+)/(?P<id>[\w-]+)/$',
		view = views.StudentMoocDetailView.as_view(),
		name = 'student_mooc_detail_module'
	),

	url(
		regex = r'owner-list/$',
		view = views.MoocByOwnerListView.as_view(),
		name = 'owner-list'
	),
	
	url(
		regex = r'add/$',
		view = views.MoocCreateView.as_view(),
		name = 'mooc-add'
	),
	
	url(
		regex = r'(?P<pk>[-\w]+)/update/$',
		view = views.MoocUpdateView.as_view(),
		name = 'mooc-update'
	),
	
	url(
		regex = r'(?P<pk>[-\w]+)/mooc/module/create/$',
		view = views.MoocModuleUpdateView.as_view(),
		name = 'mooc_module_create'
	),

	url(
		regex = r'(?P<pk>[-\w]+)/mooc/module/$',
		view = views.ModuleListView.as_view(),
		name = 'mooc-modules'
	),
	
	url(
		regex = r'(?P<pk>[-\w]+)/mooc/module/(?P<module_id>\d+)/list/$',
		view = views.ModuleContentListView.as_view(),
		name = 'mooc_module_content_list'
	),

	url(
		regex = r'(?P<pk>[-\w]+)/mooc/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
		view = views.ContentCreateUpdateView.as_view(),
		name = 'mooc_module_content_create'
	),

	url(
		regex = r'(?P<pk>[-\w]+)/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/edit/$',
		view = views.ContentCreateUpdateView.as_view(),
		name = 'mooc_module_content_update'
	),
]
