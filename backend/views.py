from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def registro(request):
    return render(request, "registro.html")


def calculadora(request):
    return render(request, "calculadora.html")