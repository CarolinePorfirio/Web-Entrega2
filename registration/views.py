from django.shortcuts import render

# Create your views here.
def backoffice(request):
    return render(request,"registration/login.html")