# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------

from __future__ import absolute_import, unicode_literals


# ============================================================================



# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from django.contrib.sitemaps import GenericSitemap

from .sitemaps import HomeViewSitemap, PublicationSitemap, PostSitemap, AboutSitemap

# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------



# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------



# ============================================================================

sitemaps = {
    'pubs'  : PublicationSitemap,
    'home'  : HomeViewSitemap,
    'posts' : PostSitemap,
    'about' : AboutSitemap,
}




urlpatterns = [
    # Admin site
    url(r'^reysh/', include(admin.site.urls)),

    ### User management
    url(r'^users/', include("foton.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Our stuff goes from here

    # ----- PRESENTATION ----- #
    url(r'^', include('foton.presentation.urls', namespace="presentation")),

    # ----- STAFF ----- #
    url(r'^staff/', include("foton.staff.urls", namespace="staff")),

    # ----- PROGRAMS ----- #
    url(r'^programs/', include("foton.programs.urls", namespace="programs")),

    # ----- DEGREE ----- #
    url(r'^degrees/', include("foton.degrees.urls", namespace="degrees")),

    # ----- BLOG ----- #
    url(r'^blog/', include("foton.cicanon.urls", namespace="cicanon")),

    # ----- NOTES ----- #
    url(r'^notes/', include("foton.notes.urls", namespace="notes")),

    # ----- STUDENTS ----- #
    url(r'^students/', include("foton.students.urls", namespace="students")),

    # ----- E-JOURNAL ----- #
    url(r'^e-journal/', include("foton.ejournal.urls", namespace="ejournal")),

    # ----- E-LEARNING ----- #
    url(r'^e-learning/', include("foton.theme.urls", namespace="theme")),

    # ----- PLANNING ----- #
    url(r'^planning/', include("foton.planning.urls", namespace="planning")),

    # ----- PUBLICATION ----- #
    url(r'^publications/', include("foton.publication.urls", namespace="publication")),

    # ----- GALLERY ----- #
    url(r'^galleries/', include('foton.galleries.urls', namespace='galleries')),

    url(r'^elearning/', include("foton.elearning.urls", namespace="elearning")),
    
    url(r'^university/', include("foton.universities.urls", namespace="universities")),
    
    url(r'^moocs/', include("foton.moocs.urls", namespace="moocs")),

    # ------ Diplompa ------- #

    # url(r'^diploma/', include("foton.diploma.urls", namespace="diploma")),

    # Rosetta
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    # Sitemaps

    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps}),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
        url(r'^502/$', default_views.server_error),
    ]
