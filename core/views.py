from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/index.html")

def contacto(request):
    return render(request, "core/contacto.html")

def preguntas(request):
    return render(request, "core/preguntas.html")

def quienSomos(request):
    return render(request, "core/quienSomos.html")

def tramites(request):
    return render(request, "core/tramites.html")

def turismo(request):
    return render(request, "core/turismo.html")

