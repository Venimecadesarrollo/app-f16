from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('registro/', views.registro, name='registro'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('registro-creado/', views.registro_creado, name='registro_creado'),
    path('msj-contacto/', views.msj_contacto, name='msj_contacto'),
    path('msj-login/', views.msj_login, name='msj_login'),
]
