from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),  # Ruta para la página principal
]
