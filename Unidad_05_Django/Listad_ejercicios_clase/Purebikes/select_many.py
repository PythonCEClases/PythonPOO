import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Purebikes.settings")
django.setup()

from bikes.models import Bike

brands = Bike.objects.values_list('brand', 'model').distinct()

for brand in brands:
    print(brand)
