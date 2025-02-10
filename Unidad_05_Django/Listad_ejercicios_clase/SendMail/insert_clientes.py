import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SendMail.settings")
django.setup()

from clientes.models import Cliente

print("Creando clientes...")

clientes = [
    Cliente(nombre="Juan", apellido="González", email="juan@gmail.com", telefono="123456789", direccion="Calle Mayor 1"),   
    Cliente(nombre="María", apellido="López", email="maria.lopez@obrero.es", telefono="987654321", direccion="Calle Menor 2", poblacion="Madrid"),  
    Cliente(nombre="Antonio", apellido="Martínez", email="antonio.martinez@casa.es", telefono="123456789", direccion="Calle Principal 3", poblacion="Barcelona"),
    Cliente(nombre="Ana", apellido="García", email="ana.garcia@sucasa.com", telefono="987654321", direccion="Calle Secundaria 4", poblacion="Valencia"),
    Cliente(nombre="Pedro", apellido="Sánchez", email="pedro.sanchez@noesno.es", telefono="123456789", direccion="Calle de la Iglesia 5", poblacion="Sevilla"),
    Cliente(nombre="Jo", apellido="Gómez", email="tomasjodido@gmail.com", telefono="987654321", direccion="Calle de la Plaza 6", poblacion="Bilbao"),
]

for cliente in clientes:
    cliente.save()
