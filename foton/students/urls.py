from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.students import  views

urlpatterns = [

	url(
		regex = r'classe/list/$',
		view = views.ClassList.as_view(),
		name='list-classes'
	),

	url(
		regex = r'classe/create/$',
		view = views.ClassCreateView.as_view(),
		name='create-classes'
	),

	url(
		regex = r'classe/update/(?P<pk>\d+)/$',
		view = views.ClassUpdateView.as_view(),
		name='update-classes'
	),

	# +===================================================

	url(
		regex = r'sign-up/$',
		view = views.StudentCreateView.as_view(),
		name='sign-up'
	),
	url(
		regex = r'student/update/(?P<pk>\d+)/$',
		view = views.StudentUpdateView.as_view(),
		name='student-update'
	),
	url(
		regex = r'student/details/(?P<pk>[-\w]+)/$',
		view = views.StudentDetailView.as_view(),
		name='student-detail'
	),
	url(
		regex = r'student/form/(?P<pk>[-\w]+)/$',
		view = views.AdmissionForm.as_view(),
		name='admission_form'
	),
	url(
		regex = r'admission/$',
		view = views.student_list,
		name='students-list'
	),
	# url(
	# 	regex = r'admission/form$',
	# 	view = views.student_list,
	# 	name='students-form'
	# ),
	# url(
	# 	regex = r'inscription-form/$',
	# 	view = views.inscription,
	# 	name='inscription-form'
	# ),

	# ====================================================

	url(
		regex = r'registred/$',
		view = views.RegistredListByClassView.as_view(),
		name='list-class'
	),

	url(
		regex = r'registred/class/(?P<pk>\d+)/$',
		view = views.RegistredListView.as_view(),
		name='list-registred'
	),

	url(
		regex = r'registred/create/(?P<pk>\d+)/$',
		view = views.RegistredCreateView.as_view(),
		name='create-registred'
	),

	url(
		regex = r'registred/update/(?P<pk>\d+)/$',
		view = views.RegistredUpdateView.as_view(),
		name='update-registred'
	),

	url(
		regex = r'registred/re-registration/$',
		view = views.RegistrationView.as_view(),
		name='registration'
	),

	url(
        regex = r'active/(?P<pk>\d+)/$',
        view = views.ActivateRegistredView.as_view(),
        name='activate'
    ),

 	url(
		regex = r'registred/students/(?P<pk>\d+)/$',
		view = views.StudentUpdateView.as_view(),
		name='update-student'
	),

]