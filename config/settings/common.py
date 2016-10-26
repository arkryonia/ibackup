#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Reysh Tech
# @Date:   Wednesday, May 18th 2016, 12:53:35 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 1:56:43 pm
# @License: Copyright (c) Foton IT, All Right Reserved Hello
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext as _

import environ


ROOT_DIR = environ.Path(__file__) - 3 # (/a/b/MYFILE.PY - 3 = /)
PUBLIC_DIR = ROOT_DIR.path('public')

env = environ.Env()


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY", default='dc3kl5+hv^tz0#o2)afmnqciiq*qf9x7_oo_+93650y3x5a22v')


# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # Admin
    # 'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    # Your third party stuff goes here
    'rosetta',
    'crispy_forms',  # Form layouts
    'easy_thumbnails',
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'modeltranslation',
    # 'parler',
    'django.contrib.admin',
    'django_wysiwyg',
)

LOCAL_APPS = (
    'foton.users',
    'foton.theme',
    'foton.staff',
    'foton.programs',
    'foton.presentation',
    'foton.degrees',
    'foton.cicanon',
    'foton.planning',
    'foton.ejournal',
    'foton.students',
    'foton.notes',
    'foton.publication',
    'foton.galleries',
    'foton.seo',
)

INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", False)


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("Hodonou SOUNTON", 'sounton@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres:///irgib"),
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# gettext = lambda s: s
LANGUAGES = (
    ("fr", 'Francais'),
    ("en", "Anglais"),
)
# MODELTRANSLATION_LANGUAGES = ('en', 'fr')

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Africa/Porto-Novo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROSETTA_MESSAGES_PER_PAGE = 50
ROSETTA_EXCLUDED_APPLICATIONS = ['rosetta']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PUBLIC_DIR.path('templates'))
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'foton.presentation.context_processors.presentation',
                'foton.seo.context_processors.seo',
            ],
            'debug': DEBUG,
        },
    },
)


MEDIA_ROOT = ROOT_DIR('mediafiles')  # str(PUBLIC_DIR('media'))
MEDIA_URL = '/media/'

STATIC_ROOT =  ROOT_DIR('assets')   # str(PUBLIC_DIR('static'))
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    str(PUBLIC_DIR.path('staticfiles')),
    str(PUBLIC_DIR.path('media')),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# FIXTURE_DIRS = [
#     str(ROOT_DIR('foton/staff/fixtures')),
# ]

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
)


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #'none' 

ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_ADAPTER = 'foton.users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'foton.users.adapters.SocialAccountAdapter'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

SITE_NAME = 'IrgibAfrica University'
SITE_DESCRIPTION = 'IRGIB AFRICA UNIVERSITY'
SITE_KEYWORDS = 'Irgib, Africa, University, Université, Excellence, Paramilitaire,\
 Paramilitary, Bio, Ingénierie, '
SITE_SLOGAN = 'University of Excellence'
DJANGO_WYSIWYG_FLAVOR = 'ckeditor'
DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + "ckeditor/"
