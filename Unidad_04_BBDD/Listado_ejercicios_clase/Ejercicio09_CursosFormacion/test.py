import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

#cursos x tipo
cursos = Curso.objects.order_by('curso__nombre')
for c in cursos:
    print(c.nombre)