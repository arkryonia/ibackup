# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.StaffHome.as_view(),
        name='home'
    ),
    url(
        regex=r'^list/$',
        view=views.StaffListView.as_view(),
        name='list-staff'
    ),
    url(
        regex=r'^scolar/add/$',
        view=views.ScolarCreateView.as_view(),
        name='add-scolar'
    ),
    url(
        regex=r'^commercial/add/$',
        view=views.CommercialCreateView.as_view(),
        name='add-commercial'
    ),
    url(
        regex=r'^scolar/update/(?P<pk>\d+)/$',
        view=views.ScolarUpdateView.as_view(),
        name='update-scolar'
    ),
    url(
        regex=r'^commercial/update/(?P<pk>\d+)/$',
        view=views.CommercialUpdateView.as_view(),
        name='update-commercial'
    ),
    url(
        regex = r'^scolar/active/(?P<pk>\d+)/$',
        view = views.ActivateScolarView.as_view(),
        name='scolar-activate'
    ),
    url(
        regex = r'^commercial/active/(?P<pk>\d+)/$',
        view = views.ActivateCommercialView.as_view(),
        name='activate'
    ),

    url(
        regex = r'year/$',
        view = views.YearListView.as_view(),
        name='list-year'
    ),

    url(
        regex = r'year/create/$',
        view = views.YearCreateView.as_view(),
        name='create-year'
    ),

    url(
        regex = r'year/update/(?P<pk>[-\w]+)/$',
        view = views.YearUpdateView.as_view(),
        name='update-year'
    ),
    
]
