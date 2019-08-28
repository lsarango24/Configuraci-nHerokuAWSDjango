from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = '', null=False)
    #aparezca en el admin
    class Meta:
        verbose_name= "Producto"
        verbose_name_plural = "Productos"
        #lo que va a retornar
    def __str__(self):
        return self.nombre