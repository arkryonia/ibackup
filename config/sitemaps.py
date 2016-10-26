from django.contrib import sitemaps
from django.core.urlresolvers import reverse, reverse_lazy
from foton.presentation.models import About
from foton.publication.models import Publication
from foton.cicanon.models import Post

class HomeViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = "https"
    i18n = True

    def items(self):
        return [reverse_lazy("presentation:home"), reverse_lazy("theme:allianza")]

    def location(self, item):
        return reverse_lazy("presentation:home")


class AboutSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"
    i18n = True

    def items(self):
        return About.objects.all()

    def lastmod(self, obj):
        return obj.modified

    def location(self, item):
        return reverse_lazy("presentation:home")

class PostSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"
    i18n = True

    def items(self):
        return Post.objects.filter(pub = True)

    def lastmod(self, obj):
        return obj.modified

    def location(self, item):
        return reverse_lazy("presentation:home")

class PublicationSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"
    i18n = True

    def items(self):
        return Publication.objects.all()

    def lastmod(self, obj):
        return obj.modified

    def location(self, item):
        return reverse_lazy("presentation:home")
