from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import GalleryListView, PhotoListbyGallery, GalleryCreateView, GalleryAdminListView, GalleryAdminDetailView, GalleryUpdateView, PhotoCreateView, PhotoDetailView, AdminPhotoDetailView, PhotoUpdateView, GalleryDeleteView

urlpatterns = [

    ### ----- urls for public galleries views ----- ###

    url(
		regex = r'^$',
		view = GalleryListView.as_view(),
		name='list-galleries'
	),

    url(
		regex = r'^(?P<slug>[-\w]+)/photos/$',
		view = PhotoListbyGallery.as_view(),
		name='list-photos'
	),

    url(
		regex = r'^(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/detail/$',
		view = PhotoDetailView.as_view(),
		name='detail-photo'
	),

    ### ----- urls for admin galleries views ----- ###

    url(
		regex = r'^backend/$',
		view = GalleryAdminListView.as_view(),
		name='admin-list-galleries'
	),

    url(
		regex = r'^backend/new-gallery/$',
		view = GalleryCreateView.as_view(),
		name='create-gallery'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/photos/$',
		view = GalleryAdminDetailView.as_view(),
		name='admin-detail-gallery'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/update/$',
		view = GalleryUpdateView.as_view(),
		name='update-gallery'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/delete-confirmation/$',
		view = GalleryDeleteView.as_view(),
		name='delete-gallery'
	),

    url(
		regex = r'^backend/add-photo/$',
		view = PhotoCreateView.as_view(),
		name='add-photo'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/detail/$',
		view = AdminPhotoDetailView.as_view(),
		name='admin-detail-photo'
	),

    url(
		regex = r'^backend/(?P<slug>[-\w]+)/photos/(?P<pk>\d+)/update/',
		view = PhotoUpdateView.as_view(),
		name='update-photo'
	),

]
