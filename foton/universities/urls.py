from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [

	url(
		regex = r'create/lecturer/$',
		view = views.LecturerCreateView.as_view(),
		name='add-lecturer'
	),

	url(
		regex = r'update/lecturer/(?P<pk>[-\w]+)/$',
		view = views.LecturerUpdateView.as_view(),
		name='update-lecturer'
	),
	 url(
        regex = r'^active/lecturer/(?P<pk>\d+)/$',
        view = views.ActivateLecturerView.as_view(),
        name='lecturer-activate'
    ),
	# url(
	# 	regex = r'(?P<slug>[-\w]+)/$',
	# 	view = views.UniversityDetailView.as_view(),
	# 	name='detail-university'
	# ),


	# =================================================================================
	# ================================= Public urls ===================================
	# =================================================================================

	
]
