from django.db import models

class Contact(models.Model):
    run = models.CharField(max_length = 100, verbose_name = "RUT")
    passport = models.CharField(max_length = 100, verbose_name = "PASAPORTE")
    name = models.CharField(max_length = 100, verbose_name = "NOMBRE")
    lastname = models.CharField(max_length = 100, verbose_name = "APELLIDO")
    email = models.CharField(max_length = 100, verbose_name = "EMAIL")
    confirm_email= models.CharField(max_length = 100, verbose_name = "CONFIRMA_EMAIL")
    password = models.CharField(max_length = 100, verbose_name = "CLAVE")
    confirm_passwrd= models.CharField(max_length = 100, verbose_name = "CONFIRMA_CLAVE")
    country = models.CharField(max_length = 100, verbose_name = "PAIS")
    gender = models.CharField(max_length = 100, verbose_name = "GENERO")
    interest = models.CharField(max_length = 100, verbose_name = "INTERES")
    age =models.CharField(max_length = 100, verbose_name = "EDAD")
    message =  models.TextField(verbose_name = "DESCRIPCION")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Actualizacion")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-updated','-created']
    