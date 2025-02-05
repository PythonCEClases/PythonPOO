import json
import os

archivo_json = os.path.join(os.path.dirname(__file__), "people.json")

try:
    with open(archivo_json, "r") as archivo:
        datos = json.load(archivo)
        personas = datos["people"]
        for persona in personas:
            print(f"Nombre: {persona['firstName']} {persona['lastName']}")
            print(f"Edad: {persona['age']}")
            print(f"Género: {persona['gender']}")
            print()
        print(type(datos))

except IOError as e:
    print(f"Error al leer datos de {os.path.basename(archivo_json)}")
else:
    print(f"Datos leídos de {os.path.basename(archivo_json)}")
