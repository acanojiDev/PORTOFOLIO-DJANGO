from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('trabajos/', views.trabajos, name='trabajos'),
    path('trabajos/<int:trabajo_id>/', views.trabajo_detalle, name='trabajo_detalle'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
]

