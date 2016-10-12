from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import *

urlpatterns = [

    ### ----- urls for planning creation, update, list and details ----- ###

    url(
		regex = r'^$',
		view = PlanningListView.as_view(),
		name='list-planning'
	),
    url(
		regex = r'^create/$',
		view = PlanningCreateView.as_view(),
		name='create-planning'
	),
    url(
		regex = r'^update/(?P<pk>\d+)/$',
		view = PlanningUpdateView.as_view(),
		name='update-planning'
	),
    url(
		regex = r'^(?P<pk>\d+)/details/$',
		view = PlanningDetailView.as_view(),
		name='list-items'
	),

    ### ----- url for planning items list, creation, update and delete ----- ###

    url(
		regex = r'^(?P<pk>\d+)/add-item/$',
		view = ItemCreateView.as_view(),
		name='create-item'
	),
    url(
		regex = r'^update-item/(?P<pk>\d+)/$',
		view = ItemUpdateView.as_view(),
		name='update-item'
	),
    url(
		regex = r'^delete-item/(?P<pk>\d+)/confirmation/$',
		view = ItemDeleteView.as_view(),
		name='delete-item'
	),

    ### ----- Planning Public Urls ----- ###

    url(
		regex = r'^groups/$',
		view = PlanningPublicListView.as_view(),
		name='public-list-planning'
	),

    url(
		regex = r'^groups/(?P<pk>\d+)/detail/$',
		view = PlanningPublicDetailView.as_view(),
		name='public-detail-planning'
	),

]
