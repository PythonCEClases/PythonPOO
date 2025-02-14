from django.db import models

# Create your models here.


class Lugar(models.Model):
    
    tipos = (('Desierto', 'Desierto'), ('Montaña', 'Montaña'), ('Playa', 'Playa'), ('Bosque', 'Bosque'), ('Ciudad', 'Ciudad'))
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()    
    pais = models.CharField(max_length=100)
    localizacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=tipos)
    imagen = models.ImageField(upload_to='lugares', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'lugares'
        ordering = ['nombre']
        
