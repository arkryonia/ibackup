#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: drxos
# @Date:   Thursday, May 19th 2016, 12:21:42 pm
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Thursday, May 19th 2016, 12:29:09 pm
# @License: Copyright (c) Foton IT, All Right Reserved



# ----------------------------------------------------------------------------
# Std imports
# ============================================================================

from __future__ import absolute_import, unicode_literals


# ============================================================================




# ----------------------------------------------------------------------------
# Core Django imports
# ============================================================================

from django.conf import settings


# ============================================================================



# ----------------------------------------------------------------------------
# Third-party app imports
# ============================================================================



# ============================================================================


# ----------------------------------------------------------------------------
# Current app imports
# ============================================================================

from .models import About
from foton.ejournal.models import Magasine
from foton.publication.models import Publication
from foton.galleries.models import Gallery, Photo
from foton.cicanon.models import Post

# ============================================================================


def presentation(request):

    about = About.objects.first()
    new = Publication.objects.filter(category='news').last()
    event = Publication.objects.filter(category='event').last()
    magasines = Magasine.objects.order_by('-id')[:5]
    gallery = Gallery.objects.last()
    photos = Photo.objects.filter(gallery=gallery)
    post = Post.objects.filter(pub=True).last()

    return {

        # 'CICANON': settings.CICANON,
        # 'DISQUS_SITE_NAME':settings.DISQUS_SITE_NAME,
        'ABOUT': about,
        'NEW': new,
        'EVENT':event,
        'Magasine' : magasines,
        'GALLERY':gallery,
        'PHOTOS':photos,
        'blog_post':post,
    }
