#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Thursday, May 19th 2016, 12:21:42 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 12:32:36 pm
# @License: Copyright (c) Foton IT, All Right Reserved



from django.conf.urls import url
from foton.presentation import  views

urlpatterns = [
	url(
		regex = r'^$',
		view = views.HomeTemplateView.as_view(),
		name='home'
	),

	url(
		regex = r'about-us/$',
		view = views.AboutView.as_view(),
		name='about'
	),

	url(
		regex = r'contact-us/$',
		view = views.ContactView.as_view(),
		name='contact'
	),
# ==========================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==========================================================

	url(
		regex = r'about/$',
		view = views.AboutListView.as_view(),
		name='list-about'
	),

	url(
		regex = r'about/create/$',
		view = views.AboutCreateView.as_view(),
		name='create-about'
	),

	url(
		regex = r'about/update/(?P<pk>[-\w]+)/$',
		view = views.AboutUpdateView.as_view(),
		name='update-abouts'
	),

# ==========================================================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ==========================================================

	url(
		regex = r'about/(?P<about_pk>[-\w]+)/items/$',
		view = views.ItemListView.as_view(),
		name='list-items'
	),

	url(
		regex = r'about/(?P<about_pk>[-\w]+)/items/create/$',
		view = views.ItemCreateView.as_view(),
		name='create-items'
	),

	url(
		regex = r'about/(?P<about_pk>[-\w]+)/items/update/(?P<pk>[-\w]+)/$',
		view = views.ItemUpdateView.as_view(),
		name='update-items'
	),
]
