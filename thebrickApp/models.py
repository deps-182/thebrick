from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="productos",null=True)
    talla = models.IntegerField()
    genero = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre
    