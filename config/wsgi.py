"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling, MediaCling

application = MediaCling(get_wsgi_application())
application = Cling(application)
# application = DjangoWhiteNoise(application)