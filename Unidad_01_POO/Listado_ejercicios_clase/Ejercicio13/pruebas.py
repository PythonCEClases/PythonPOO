from clases import Producto

# creación de una lista de productos
productos = [
    Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75),
]

productos[0].caducado = True

for pro in productos:
    print(pro.__dict__)
