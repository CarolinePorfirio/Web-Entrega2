from django import forms

class ContactForm(forms.Form):
    rut = forms.CharField(label="Rut ", min_length=9, max_length=9, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 12345678-9'}))
    passport = forms.CharField(label="Pasaporte ", min_length=8, max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. A1B2C3'}))
    name = forms.CharField(label="Nombre ", min_length=3, max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    lastname = forms.CharField(label="Apellido ", min_length=3, max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    email = forms.EmailField(label="Email",  min_length=5, max_length=30, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@correo.com'}))
    emailconfirm = forms.EmailField(label="Confirmar Email",  min_length=5, max_length=30, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@correo.com'}))
    password = forms.CharField(label="Password ", min_length=5, max_length=10, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    passwordconfirm = forms.CharField(label="Confirma Password ", min_length=5, max_length=10, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    country = forms.ChoiceField(choices=[('CH','CHILE'),('CO','COLOMBIA'),('VE','VENEZUELA')])
    gender = forms.CharField(label ="Genero", widget=forms.RadioSelect(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]))
    interes = forms.CharField(label ="Interés", widget=forms.RadioSelect(choices=[('TU', 'Turismo'), ('TR', 'Trabajo'), ('MO', 'Moradia')]))
    message =  forms.CharField(label="Mensaje ", min_length=3, max_length=300, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}))