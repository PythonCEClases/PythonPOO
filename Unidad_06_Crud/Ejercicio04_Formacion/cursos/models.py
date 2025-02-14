from django.db import models

# Create your models here.

tematica = (
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('BD', 'Bases de Datos'),
    ('JS', 'JavaScript'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('Otros', 'Otros')
)
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tematica = models.CharField(max_length=100, choices=tematica)

    def __str__(self):
        return f'{self.nombre} - {self.tematica}'
    
    class Meta:
        db_table = 'cursos'
        ordering = ['fecha_inicio']
        

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'estudiantes'
        ordering = ['apellidos']
        
