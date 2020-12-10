from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        name = request.POST.get('name','')
        email =request.POST.get('email','')
        emailc =request.POST.get('confirm_email','')
        message= request.POST.get('message','')
        password=request.POST.get('password','')
        passwordc=request.POST.get('confirm_password','')
        if email != emailc:
            return redirect(reverse('contacto') + '?MAIL')

        if password != passwordc:
            return redirect(reverse('contacto') + '?PASS')

        if contact_form.is_valid():
            registro = Contact(run=contact_form.cleaned_data['run'],
                                passport=contact_form.cleaned_data['passport'],
                                name=contact_form.cleaned_data['name'],
                                lastname=contact_form.cleaned_data['lastname'],
                                email=contact_form.cleaned_data['email'],
                                confirm_email=contact_form.cleaned_data['confirm_email'],
                                password=contact_form.cleaned_data['password'],
                                confirm_passwrd=contact_form.cleaned_data['confirm_password'],
                                country=contact_form.cleaned_data['country'],
                                gender=contact_form.cleaned_data['gender'],
                                interest=contact_form.cleaned_data['interest'],
                                message=contact_form.cleaned_data['message'],
                                age=contact_form.cleaned_data['age'])
            registro.save()
            
            #crear el correo
            email = EmailMessage(
                "Welcome_Chile : Nuevo Registro",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,message),
                "no-contestar@inbox.mailtrap.io",
                ["rafael.rozas@gmail.com"],
                reply_to=[email]
                )
            try:
                email.send()    
                return redirect(reverse('contacto') + '?OK')
            except:
                return redirect(reverse('contacto') + '?FAIL')
        else:
            return redirect(reverse('contacto') + '?FAIL')

    return render(request,"contact/contacto.html",{'form':contact_form},{'contacto':Contact})