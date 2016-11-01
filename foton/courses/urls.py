from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.courses import  views

urlpatterns = [

	url(
		regex = r'(?P<slug>[-\w]+)/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
		view = views.ContentCreateView.as_view(),
		name = 'module_content_create'
	),
	url(
		regex = r'module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/update/(?P<id>\d+)$',
		view = views.ContentCreateView.as_view(),
		name = 'module_content_update'
	),

	# ======================Domain
]