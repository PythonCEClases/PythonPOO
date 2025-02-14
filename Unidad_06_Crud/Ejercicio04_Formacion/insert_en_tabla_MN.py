import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ejercicio04_Formacion.settings")
django.setup()

from cursos.models import Estudiante, Curso

# Insertar datos en la tabla M:N Estudiante_Curso

estudiantes = Estudiante.objects.all()
cursos = Curso.objects.all()

import random
for e in estudiantes:
    for  i in range(0, 3):
        numero = random.randint(0, len(cursos)-1)
        curso = cursos[numero]
        if curso not in e.cursos.all():
            e.cursos.add(curso)
            e.save()
            print(e.nombre, curso.nombre)
        