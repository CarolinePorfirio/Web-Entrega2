from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"core/index.html")

def quiensomos(request):
    return render(request,"core/quiensomos.html")

def tramites(request):
    return render(request,"core/tramites.html")

def preguntas(request):
    return render(request,"core/preguntas.html")


