from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    direccion = models.TextField()
    localidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellidos

    class Meta:
        db_table = "contacto"
