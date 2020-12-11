from django import forms
from .widgets import BootstrapDateTimePickerInput
from .widgets import FengyuanChenDatePickerInput

# Create your forms here.

class ContactForm(forms.Form):
    rut = forms.CharField(label="Rut:", min_length=8, max_length=12, required=True)
    pasaporte = forms.CharField(label="Pasaporte:", min_length=8, max_length=12, required=False)
    nombre = forms.CharField(label="Nombre:", min_length=3, max_length=100, required=True)
    apellido = forms.CharField(label="Apellido:", min_length=3, max_length=100, required=True)
    email = forms.EmailField(label="Email:", min_length=5, max_length=100, required=True)
    confirm_email = forms.EmailField(label="Confirme Email:", min_length=5, max_length=100, required=True)
    password = forms.CharField(label="Paswword:", widget=forms.PasswordInput, min_length=8, max_length=20, required=True)
    confirm_password = forms.CharField(label="Confirme Paswword:", widget = forms.PasswordInput, min_length=8, max_length=20, required=True)
    fecha_nac = forms.DateTimeField(widget=BootstrapDateTimePickerInput())
    pais = forms.ChoiceField(choices=[('',''),('Brasil', 'Brasil'),('Colombia', 'Colombia'),('Argentinta', 'Argentina'),('Peru', 'Peru'),('Venezuela', 'Venezuela'),('Uruguay', 'Uruguay')])
    genero = forms.CharField(label='GENERO', widget=forms.RadioSelect(choices=[('M','Male'),('F','Female'),('O','Otro')]))
    interes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=(('Tu','Turismo'),('tr','Trabajo'),('N','Negocios')))
    comentario = forms.CharField(label="Ingrese un comentario:", min_length=5, max_length=300, required=True, widget=forms.Textarea())

    #age = forms.CharField(label="EDAD",min_length=1,max_length=3,required=True)

