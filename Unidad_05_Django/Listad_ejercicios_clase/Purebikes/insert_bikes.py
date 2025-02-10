import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Purebikes.settings")
django.setup()

from bikes.models import Bike

print("Creando bicicletas")

bikes = [
    # Bike(brand="Trek", model="Marlin 5", year=2021, price=500.00, description="Bicicleta de montaña"),
    # Bike(brand="Specialized", model="Rockhopper", year=2021, price=600.00, description="Bicicleta de montaña"),
    # Bike(brand="Giant", model="ATX 3", year=2021, price=400.00, description="Bicicleta de montaña"),
    # Bike(brand="Cannondale", model="Trail 8", year=2021, price=500.00, description="Bicicleta de montaña"),
    # Bike(brand="Giant", model="Escape 3", year=2021, price=400.00, description="Bicicleta de ruta"),
    # Bike(brand="Specialized", model="Allez", year=2021, price=600.00, description="Bicicleta de ruta"),
    # Bike(brand="Trek", model="Domane AL 2", year=2021, price=700.00, description="Bicicleta de ruta"),
    Bike(brand="Cannondale", model="Synapse", year=2021, price=800.00, description="Bicicleta de ruta"),
    Bike(brand="Giant", model="Contend 3", year=2021, price=500.00, description="Bicicleta de ruta"),
    Bike(brand="Specialized", model="Sirrus 1.0", year=2021, price=400.00, description="Bicicleta híbrida"),
    Bike(brand="Trek", model="FX 1", year=2021, price=400.00, description="Bicicleta híbrida"),
    Bike(brand="Giant", model="Escape 3", year=2021, price=400.00, description="Bicicleta híbrida"),
    Bike(brand="Cannondale", model="Quick 8", year=2021, price=400.00, description="Bicicleta híbrida"),
    Bike(brand="Specialized", model="Turbo Vado", year=2021, price=2000.00, description="Bicicleta eléctrica"),
    Bike(brand="Trek", model="Verve 2", year=2021, price=700.00, description="Bicicleta eléctrica"),
    Bike(brand="Giant", model="Explore E+ 4", year=2021, price=2000.00, description="Bicicleta eléctrica"),
    Bike(brand="Cannondale", model="Quick Neo", year=2021, price=2000.00, description="Bicicleta eléctrica"),
    Bike(brand="Specialized", model="Turbo Como", year=2021, price=2000.00, description="Bicicleta eléctrica"),
    Bike(brand="Trek", model="Roscoe 6", year=2021, price=1000.00, description="Bicicleta de montaña"),
    Bike(brand="Specialized", model="Fuse 27.5", year=2021, price=1000.00, description="Bicicleta de montaña"),
    Bike(brand="Giant", model="Talon 3", year=2021, price=500.00, description="Bicicleta de montaña"),
    Bike(brand="Cannondale", model="Cujo 3", year=2021, price=800.00, description="Bicicleta de montaña"),
    Bike(brand="Giant", model="Escape 2", year=2021, price=450.00, description="Bicicleta de ruta"),
    Bike(brand="Specialized", model="Allez", year=2021, price=600.00, description="Bicicleta de ruta"),
    Bike(brand="Trek", model="Domane AL 3", year=2021, price=800.00, description="Bicicleta de ruta"),
    Bike(brand="Cannondale", model="Synapse", year=2021, price=800.00, description="Bicicleta de ruta"),
    Bike(brand="Giant", model="Contend 2", year=2021, price=600.00, description="Bicicleta de ruta"),
    
    
]

for bike in bikes:
    bike.save()  # Guardar en la base de datos
    print(f"Bicicleta {bike.brand} {bike.model} creada con éxito")