# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.DomainListView.as_view(),
        name='domain-list'
    ),

    url(
        regex=r'^domain/add/$',
        view=views.DomainCreateView.as_view(),
        name='domain-add'
    ),
    url(
        regex=r'^domain/update/(?P<pk>\d+)/$',
        view=views.DomainUpdateView.as_view(),
        name='domain-update'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/options/$',
        view=views.OptionListView.as_view(),
        name='option-list'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/option/add/$',
        view=views.OptionCreateView.as_view(),
        name='option-add'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/option/update/(?P<pk>\d+)/$',
        view=views.OptionUpdateView.as_view(),
        name='option-update'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/option/(?P<option_pk>\d+)/specialities/$',
        view=views.SpecialityListView.as_view(),
        name='speciality-list'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/option/(?P<option_pk>\d+)/speciality/add/$',
        view=views.SpecialityCreateView.as_view(),
        name='speciality-add'
    ),
    url(
        regex=r'^domain/(?P<domain_pk>\d+)/option/(?P<option_pk>\d+)/speciality/update/(?P<pk>\d+)/$',
        view=views.SpecialityUpdateView.as_view(),
        name='speciality-update'
    ),
]
