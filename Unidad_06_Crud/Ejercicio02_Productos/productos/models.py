from django.db import models
from categorias.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.ForeignKey(to=Categoria, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'producto'