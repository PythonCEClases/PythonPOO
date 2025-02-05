import json
import os
from collections import defaultdict

ventas = [
    ["tomate", 1000, 1.5],
    ["lechuga", 500, 0.5],
    ["cebolla", 300, 0.75],
    ["tomate", 2000, 1.5],
    ["lechuga", 1000, 0.5],
    ["cebolla", 600, 0.75],
    ["pera", 300, 1.75],
    ["manzana", 500, 1.25],
    ["uva", 1000, 2.5],
    ["uva", 2000, 2.5],
]

# Crear diccionario con totales
totales = defaultdict(float)
for venta in ventas:
    producto, cantidad, precio = venta
    totales[producto] += cantidad * precio

list_dict = []
for producto, total in totales.items():
    dicc_producto = {}
    dicc_producto["producto"] = producto
    dicc_producto["total"] = total
    list_dict.append(dicc_producto)

json_dict = json.dumps(list_dict, indent=4)

try:
    archivo_json = os.path.join(os.path.dirname(__file__), "totales.json")
    with open(archivo_json, "w") as archivo:
        json.dump(list_dict, archivo, indent=4)
except IOError as e:
    print(f"Error al guardar datos en {os.path.basename(archivo_json)}")
else:
    print(f"Datos guardados en {os.path.basename(archivo_json)}")
