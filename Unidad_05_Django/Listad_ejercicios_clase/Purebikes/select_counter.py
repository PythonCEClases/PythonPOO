import os

import django

from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Purebikes.settings")
django.setup()

from bikes.models import Bike

grouped_data = Bike.objects.values_list('brand').annotate(
        # total_value=Sum('value'),
        counter=Count('id')
    )

for data in grouped_data:
    print(data[0], data[1])
    
