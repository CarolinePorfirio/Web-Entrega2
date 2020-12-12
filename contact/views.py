from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form =  Contact_Form(data = request.POST)
        if contact_form.is_valid(): 
            return redirect(reverse('contacto') + "?OK")
       
    
    return render(request,"contact/contacto.html", {'form': contact_form})
