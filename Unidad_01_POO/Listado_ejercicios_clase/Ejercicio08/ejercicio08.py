# importación de la clase Producto del módulo clases
from clases import Producto

# creación de una lista de productos
productos = [
    Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75),
]


# Contar productos con precio entre 2 y 3
cuenta = 0
for producto in productos:
    if producto.precio > 2 and producto.precio < 3:
        cuenta += 1

print(f"Productos con precio entre 2 y 3: {cuenta}")
