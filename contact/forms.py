from django import forms

class ContactForm(forms.Form):
    run = forms.CharField(label="RUT",min_length=9,max_length=11,required=True) 
    passport = forms.CharField(label="PASAPORTE",min_length=9,max_length=11,required=False)
    name = forms.CharField(label="NOMBRE",min_length=3,max_length=100,required=True)
    lastname =forms.CharField(label="APELLIDO",min_length=3,max_length=100,required=True)
    email = forms.EmailField(label="EMAIL",min_length=5,max_length=100,required=True)
    confirm_email =forms.EmailField(label="CONFIRMAR EMAIL",min_length=5,max_length=100,required=True)
    password = forms.CharField(label="CLAVE",widget=forms.PasswordInput,min_length=6,max_length=12,required=True)
    confirm_password = forms.CharField(label="CONFIRMAR CLAVE",widget=forms.PasswordInput,min_length=6,max_length=12,required=True)
    country = forms.ChoiceField(choices=[('CH','CHILE'),('CO','COLOMBIA'),('VE','VENEZUELA')])
    gender = forms.CharField(label='GENERO', widget=forms.RadioSelect(choices=[('M','Male'),('F','Female'),('O','Otro')]))
    interest = forms.CharField(label='GENERO', widget=forms.RadioSelect(choices=[('Tu','Turismo'),('tr','Trabajo'),('N','Negocios')]))
    message = forms.CharField(label="COMENTARIOS",min_length=5,max_length=300,required=True,widget=forms.Textarea)
    age = forms.CharField(label="EDAD",min_length=1,max_length=3,required=True)
