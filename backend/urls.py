from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("process-register/", views.process_register, name="process_register"),
]

