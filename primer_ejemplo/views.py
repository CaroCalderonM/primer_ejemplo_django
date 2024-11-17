from django.shortcuts import render  # render nos permite renderizar Templates
from django.http import HttpResponse

# Aquí, home también se podría llamar index
# Aquí defino la función para la url


def home(request):
    # return HttpResponse("<h1>Página principal. Primera vista.</h1>")
    # En el contexto podemos enviar toda la info que queramos para el html
    # Estopermite hacer sitios dinámicos con string, valores enteros, listas, tuplas, arrays, diccionarios, etc.
    context = {
        "titulo": "Home"
    }
    return render(request, "home.html", context)


def reclamos(request):
    # return HttpResponse("<h1>Página reclamos</h1>")
    context = {
        "titulo": "Reclamos"
    }
    return render(request, "reclamos.html", context)


def reclamos(request):
    # return HttpResponse("<h1>Página reclamos</h1>")
    context = {
        "titulo": "Reclamos"
    }
    return render(request, "reclamos.html", context)


def productos(request):
    # return HttpResponse("<h1>Página productos</h1>")
    context = {
        "titulo": "Productos",
        "productos": ["producto 1", "producto 2", "producto 3", "producto 4", "producto 5"]
    }
    return render(request, "productos.html", context)


''' Bibliografía: w3Schools - Django Views
Las vistas se pueden hacer por render o por HttpResponse
https://www.w3schools.com/django/django_views.php

Por render.----------
from django.shortcuts import render

# Create your views here.

Por HttpResponse.-------
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
'''
