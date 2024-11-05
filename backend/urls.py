from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('index/', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('admin/', admin.site.urls),
    path('registro-creado/', views.registro_creado, name='registro_creado'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
