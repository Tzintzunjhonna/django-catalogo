from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "core/home.html")

def accesorios(request):
    return render(request, "core/accesorios.html")

def calzado(request):
    return render(request, "core/calzado.html")

def ropa(request):
    return render(request, "core/ropa.html")

def maternidad(request):
    return render(request, "core/maternidad.html")

