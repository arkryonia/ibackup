from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.graduation import views

urlpatterns = [
	
	url(
		regex = r'^$',
		view = views.GraduationHome.as_view(),
		name='graduation-home'
	),
	
	url(
		regex = r'^success/$',
		view = views.GraduationSuccess.as_view(),
		name='graduation-success'
	),

	url(
		regex = r'^bachelor/form/$',
		view = views.BachelorCreateView.as_view(),
		name='bachelor-create'
	),

	url(
		regex = r'^master/form/$',
		view = views.MasterCreateView.as_view(),
		name='master-create'
	),

	url(
		regex = r'^bachelor/list/$',
		view = views.BachelorList.as_view(),
		name='bachelor-list'
	),
	url(
		regex = r'^bachelor/list/csv$',
		view = views.BachelorCsvList.as_view(),
		name='bachelor-csvlist'
	),

	url(
		regex = r'^bachelor/update/(?P<pk>\d+)/$',
		view = views.BachelorUpdateView.as_view(),
		name='bachelor-update'
	),

]