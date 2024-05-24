from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import TemplateView

app_name = "web"

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('', home, name='home'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name='web/robots.txt', content_type='text/plain')),

    path('servicios/', servicios, name='servicios'),
    path('servicios/bicicleta', bicicleta, name='bicicleta'),
    path('servicios/patinete', patinete, name='patinete'),

    path('electrifica/', electrifica, name='electrifica'),

    path('politica/', politica, name='politica'),

    path('ocasion/', ProductList.as_view(), name='ocasion'),
    path('ocasion/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

    path('contacto/', contacto, name='contacto'),
    path('contacto_exitoso/', contacto_exitoso, name='contacto_exitoso'),
]