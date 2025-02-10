from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=50, default="Madrid")

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'clientes'