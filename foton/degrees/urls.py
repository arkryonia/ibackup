# @Author: drxos
# @Date:   Friday, May 6th 2016, 6:03:28 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   sadjad
# @Last modified time: 2016-05-19T07:35:48+01:00
# @License: Copyright (c) Foton IT, All Right Reserved



from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import  views


urlpatterns = [
	# --------------------------------------------------------------------------
	url(
		regex = r'^bachelors/$',
		view = views.BachelorListView.as_view(),
		name='bachelor-list'
	),
	url(
		regex = r'^bachelor/create/$',
		view = views.BachelorCreateView.as_view(),
		name='bachelor-add'
	),
	url(
		regex = r'^bachelor/(?P<pk>\d+)/update/$',
		view = views.BachelorUpdateView.as_view(),
		name='update-bachelor'
	),
	# --------------------------------------------------------------------------
	url(
		regex = r'^masters/$',
		view = views.MasterListView.as_view(),
		name='masters-list'
	),
	url(
		regex = r'^master/create/$',
		view = views.MasterCreateView.as_view(),
		name='master-add'
	),
	url(
		regex = r'^master/(?P<pk>\d+)/update/$',
		view = views.MasterUpdateView.as_view(),
		name='master-update'
	),

	#<><><><><><><><><><><><><><><>FrontEnd<><><><><><><><><><><><><><><><><><>#
	url(
		regex = r'^bachelors/list/$',
		view = views.BachelorFrontListView.as_view(),
		name='bachelor-front-list'
	),

	url(
		regex = r'^masters/list$',
		view = views.MasterFrontListView.as_view(),
		name='masters-front-list'
	),

]
