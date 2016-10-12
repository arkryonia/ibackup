from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.ejournal import  views

urlpatterns = [
	url(
		regex = r'magasine/$',
		view = views.MagasineListView.as_view(),
		name='list-magasine'
	),

	url(
		regex = r'magasine/create/$',
		view = views.MagasineCreateView.as_view(),
		name='create-magasine'
	),

	url(
		regex = r'magasine/update/(?P<pk>[-\w]+)/$',
		view = views.MagasineUpdateView.as_view(),
		name='update-magasine'
	),





	url(
		regex = r'magasine/(?P<pk>[-\w]+)/$',
		view = views.MagasineDetailView.as_view(),
		name='detail-magasine'
	),
	url(
		regex = r'magasine/(?P<pk>[-\w]+)/sommary/$',
		view = views.SommaryCreateView.as_view(),
		name='create-sommary'
	),

	url(
		regex = r'magasine/sommary/update/(?P<pk>[-\w]+)/$',
		view = views.SommaryUpdateView.as_view(),
		name='update-sommary'
	),

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ===========================================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	url(
		regex = r'^$',
		view = views.MagasinePubListView.as_view(),
		name='magasines'
	),

	url(
		regex = r'journal/(?P<pk>[-\w]+)/$',
		view = views.MagasinePubDetail.as_view(),
		name='detail'
	),
]