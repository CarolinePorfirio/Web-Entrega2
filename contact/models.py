from django.db import models

# Create your models here.

class Contact(models.Model):
    rut = models.CharField(max_length = 100, verbose_name = "RUT")
    pasaporte = models.CharField(max_length = 100, verbose_name = "PASAPORTE", blank=True)
    nombre = models.CharField(max_length = 100, verbose_name = "NOMBRE")
    apellido = models.CharField(max_length = 100, verbose_name = "APELLIDO")
    email = models.CharField(max_length = 100, verbose_name = "EMAIL")
    #confirm_email= models.CharField(max_length = 100, verbose_name = "CONFIRMA_EMAIL")
    password = models.CharField(max_length = 100, verbose_name = "CLAVE")
    #confirm_password= models.CharField(max_length = 100, verbose_name = "CONFIRMA_CLAVE")
    pais = models.CharField(max_length = 100, verbose_name = "PAIS")
    genero = models.CharField(max_length = 100, verbose_name = "GENERO")
    interes = models.CharField(max_length = 100, verbose_name = "INTERES")
    edad =models.CharField(max_length = 100, verbose_name = "EDAD")
    comentario =  models.TextField(verbose_name = "DESCRIPCION")
    created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Actualizacion")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-updated','-created']

    def __str__ (self):
        return self.nombre