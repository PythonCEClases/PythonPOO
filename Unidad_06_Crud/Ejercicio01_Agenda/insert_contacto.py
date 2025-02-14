import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ejercicio01_Agenda.settings")
django.setup()

from agenda.models import Contacto

print("Creando contactos...")

contactos = [
    Contacto(nombre="Juan", apellidos="Perez", telefono="12345678", email="juan@gmail.com", direccion="Calle 123", localidad="Madrid"),  
    Contacto(nombre="Ana", apellidos="Lopez", telefono="87654321", email="ana@lopez.es", direccion="Calle 456", localidad="Barcelona"),
    Contacto(nombre="Luis", apellidos="Gomez", telefono="45678912", email="luis@goemz.es", direccion="Calle 789", localidad="Valencia"),
    Contacto(nombre="Maria", apellidos="Martinez", telefono="78912345", email="maria@martinez.es", direccion="Calle 012", localidad="Sevilla"),
    Contacto(nombre="Pedro", apellidos="Jimenez", telefono="32165498", email="peter@jimenez.es", direccion="Calle 345", localidad="Bilbao"),
    Contacto(nombre="Sara", apellidos="Garcia", telefono="65498732", email="sara@garcia.es", direccion="Calle 678", localidad="Zaragoza"),
]

for contacto in contactos:
    contacto.save()