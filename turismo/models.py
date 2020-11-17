from django.db import models

# Create your models here.
class Package(models.Model):
     title= models.CharField(max_length = 100, verbose_name = "Titulo")
     duration = models.CharField(max_length = 100, verbose_name = "Duracion")
     description = models.TextField(verbose_name = "Descripcion")
     imag = models.ImageField(verbose_name= "Imagen",upload_to='packages')
     created = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Creacion")
     updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha Actualizacion")

     class Meta:
        verbose_name = "Paquete"
        verbose_name_plural = "Paquetes"
        ordering = ['-updated','-created']
    
     def __str__ (self):
        return self.title



