from django.shortcuts import render
from .models import Package
#from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def turismo(request):
    packages = Package.objects.all()
    return render(request,"turismo/turismo.html",{'packages':packages})

