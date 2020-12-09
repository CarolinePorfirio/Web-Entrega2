from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact


# Create your views here.
def contacto(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            registro = Contact(run=contact_form.cleaned_data['run'])
            registro.save()
            return redirect(reverse('contacto') + '?OK')
        else:
            return redirect(reverse('contacto') + '?FAIL')

    return render(request,"contact/contacto.html",{'form':contact_form},{'packages':Contact})