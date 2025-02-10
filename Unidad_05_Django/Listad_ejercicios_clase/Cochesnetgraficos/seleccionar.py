import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cochesnetgraficos.settings")
django.setup()
from datetime import datetime
from graficos.models import Coche, Marca
from functools import reduce

years = Coche.objects.all().dates('fecha_fabricacion', 'year')
y = [year.year for year in years]
cuenta = [Coche.objects.filter(fecha_fabricacion__year=year).count() for year in y]
print(y)
print(cuenta)