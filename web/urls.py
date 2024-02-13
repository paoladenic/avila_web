from django.urls import path
from .views import *

app_name = "web"

urlpatterns = [
    path('', home, name='homepage'),

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