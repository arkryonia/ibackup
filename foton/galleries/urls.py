from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [

    ### ----- urls for public galleries views ----- ###

    url(
		regex = r'^$',
		view = views.GalleryListView.as_view(),
		name='list-galleries'
	),

    url(
		regex = r'^(?P<slug>[-\w]+)/photos/$',
		view = views.PhotoListbyGallery.as_view(),
		name='list-photos'
	),

    url(
		regex = r'^(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/detail/$',
		view = views.PhotoDetailView.as_view(),
		name='detail-photo'
	),

    ### ----- urls for admin galleries views ----- ###

    url(
		regex = r'^backend/$',
		view = views.GalleryAdminListView.as_view(),
		name='admin-list-galleries'
	),

    url(
		regex = r'^backend/new-gallery/$',
		view = views.GalleryCreateView.as_view(),
		name='create-gallery'
	),

    url(
		regex = r'^backend/(?P<pk>[-\w]+)/list-photos/$',
		view = views.GalleryPhotoListView.as_view(),
		name='admin-list-photo'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/update/$',
		view = views.GalleryUpdateView.as_view(),
		name='update-gallery'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/delete-confirmation/$',
		view = views.GalleryDeleteView.as_view(),
		name='delete-gallery'
	),

    url(
		regex = r'^backend/add-photo/$',
		view = views.PhotoCreateView.as_view(),
		name='add-photo'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/detail/$',
		view = views.AdminPhotoDetailView.as_view(),
		name='admin-detail-photo'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/update/',
		view = views.PhotoUpdateView.as_view(),
		name='update-photo'
	),

]
