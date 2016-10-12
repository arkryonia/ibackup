from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import *

urlpatterns = [

    ### ----- urls for publication creation, update, list and details ----- ###

    url(
		regex = r'^$',
		view = PublicationListView.as_view(),
		name='list-publication'
	),

    url(
		regex = r'^create/$',
		view = PublicationCreateView.as_view(),
		name='create-publication'
	),

    url(
		regex = r'^(?P<pk>\d+)/detail/$',
		view = PublicationDetailView.as_view(),
		name='detail-publication'
	),

    url(
		regex = r'^(?P<pk>\d+)/update/$',
		view = PublicationUpdateView.as_view(),
		name='update-publication'
	),


    ### ----- Publication Public Urls ----- ###

    url(
		regex = r'^news/list/$',
		view = NewsList.as_view(),
		name='list-new'
	),

    url(
		regex = r'^events/list/$',
		view = EventsList.as_view(),
		name='list-event'
	),

    url(
		regex = r'^(?P<pk>\d+)/$',
		view = PublicationDetail.as_view(),
		name='public-detail-publication'
	),

]
