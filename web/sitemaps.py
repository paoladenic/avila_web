from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['web:home', 'web:servicios', 'web:bicicleta', 'web:patinete', 'web:electrifica', 'web:contacto', 'web:politica']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()
    
    def lastmod(self, obj):
        return obj.created_at