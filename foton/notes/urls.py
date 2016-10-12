# @Author: drxos
# @Date:   Friday, May 6th 2016, 6:03:28 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Friday, May 6th 2016, 6:56:12 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django.conf.urls import url
from django.core.urlresolvers import reverse

from foton.notes import  views


urlpatterns = [
	url(
		regex = r'^$',
		view = views.ClassListView.as_view(),
		name='classes-list'
	),
	url(
		regex = r'classes/(?P<pk>\d+)/$',
		view = views.ClassDetailView.as_view(),
		name='class-detail'
	),
	url(
		regex = r'classes/(?P<pk>\d+)/students/$',
		view = views.StudentDetailView.as_view(),
		name='notes'
	),

	# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	# ===============================================================
	# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

	url(
		regex = r'classe/list/$',
		view = views.ClassList.as_view(),
		name='list-classes'
	),

	url(
		regex = r'course/list/$',
		view = views.CourseListView.as_view(),
		name='list-course'
	),

	url(
		regex = r'course/create/$',
		view = views.CourseCreateView.as_view(),
		name='create-course'
	),
	url(
		regex = r'course/update/(?P<pk>\d+)/$',
		view = views.CourseUpdateView.as_view(),
		name='update-course'
	),



	url(
		regex = r'classe/(?P<class_pk>\d+)/students/list/$',
		view = views.ClassStudentList.as_view(),
		name='list-student'
	),

	

	url(
		regex = r'classe/(?P<class_pk>\d+)/students/(?P<registred_pk>\d+)/$',
		view = views.StudentNoteList.as_view(),
		name='list-note'
	),

	url(
		regex = r'classe/(?P<class_pk>\d+)/students/(?P<registred_pk>\d+)/note/create/$',
		view = views.NoteCreateView.as_view(),
		name='create-note'
	),

	url(
		regex = r'classe/(?P<class_pk>\d+)/students/(?P<registred_pk>\d+)/note/(?P<pk>\d+)/$',
		view = views.NoteUpdateView.as_view(),
		name='update-note'
	),
]