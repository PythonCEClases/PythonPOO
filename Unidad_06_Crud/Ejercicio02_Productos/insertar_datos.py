import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio02_Productos.settings')
django.setup()

from productos.models import Categoria, Producto

# Insertar datos en la tabla Categoria
categorias = [
    Categoria(nombre='Electrodomésticos', descripcion='Productos para el hogar'),
    Categoria(nombre='Tecnología', descripcion='Productos tecnológicos'),
    Categoria(nombre='Deportes', descripcion='Productos deportivos'),
    Categoria(nombre='Ropa', descripcion='Ropa para hombres y mujeres'),
    Categoria(nombre='Hogar', descripcion='Productos para el hogar'),
    Categoria(nombre='Juguetes', descripcion='Juguetes para niños'),
    Categoria(nombre='Libros', descripcion='Libros de diferentes géneros'),
    Categoria(nombre='Calzado', descripcion='Zapatos para hombres y mujeres'),
    Categoria(nombre='Muebles', descripcion='Muebles para el hogar'),
    Categoria(nombre='Accesorios', descripcion='Accesorios de moda'),
    Categoria(nombre='Perfumería', descripcion='Perfumes y colonias'),
    Categoria(nombre='Cuidado Personal', descripcion='Productos de cuidado personal')
]

for categoria in categorias:
    categoria.save()
    
# Insertar datos en la tabla Producto
productos = [
    Producto(nombre='TV Fenix 4', descripcion='Televisor de 50 pulgadas', precio=500.00, categoria=Categoria.objects.get(nombre='Electrodomésticos')),
    Producto(nombre='Laptop Dell', descripcion='Laptop de 15 pulgadas', precio=800.00, categoria=Categoria.objects.get(nombre='Tecnología')),
    Producto(nombre='Cafetera Nespresso', descripcion='Cafetera de cápsulas', precio=150.00, categoria=Categoria.objects.get(nombre='Electrodomésticos')),
    Producto(nombre='Smartphone Samsung', descripcion='Teléfono inteligente de última generación', precio=700.00, categoria=Categoria.objects.get(nombre='Tecnología')),
    Producto(nombre='Bicicleta de montaña', descripcion='Bicicleta con suspensión delantera', precio=300.00, categoria=Categoria.objects.get(nombre='Deportes')),
    Producto(nombre='Raqueta de tenis', descripcion='Raqueta de tenis profesional', precio=100.00, categoria=Categoria.objects.get(nombre='Deportes')),
    Producto(nombre='Camiseta deportiva', descripcion='Camiseta de poliéster', precio=25.00, categoria=Categoria.objects.get(nombre='Ropa')),
    Producto(nombre='Pantalones vaqueros', descripcion='Pantalones de mezclilla', precio=40.00, categoria=Categoria.objects.get(nombre='Ropa')),
    Producto(nombre='Zapatos de cuero', descripcion='Zapatos formales de cuero', precio=80.00, categoria=Categoria.objects.get(nombre='Calzado')),
    Producto(nombre='Zapatillas deportivas', descripcion='Zapatillas para correr', precio=60.00, categoria=Categoria.objects.get(nombre='Calzado')),
    Producto(nombre='Libro de cocina', descripcion='Recetas de cocina internacional', precio=30.00, categoria=Categoria.objects.get(nombre='Libros')),
    Producto(nombre='Novela de misterio', descripcion='Libro de misterio y suspense', precio=20.00, categoria=Categoria.objects.get(nombre='Libros')),
    Producto(nombre='Muñeca Barbie', descripcion='Muñeca con accesorios', precio=35.00, categoria=Categoria.objects.get(nombre='Juguetes')),
    Producto(nombre='Lego Star Wars', descripcion='Set de construcción de Lego', precio=100.00, categoria=Categoria.objects.get(nombre='Juguetes')),
    Producto(nombre='Reloj de pulsera', descripcion='Reloj analógico de pulsera', precio=150.00, categoria=Categoria.objects.get(nombre='Accesorios')),
    Producto(nombre='Gafas de sol', descripcion='Gafas de sol polarizadas', precio=50.00, categoria=Categoria.objects.get(nombre='Accesorios')),
    Producto(nombre='Bolso de mano', descripcion='Bolso de cuero', precio=200.00, categoria=Categoria.objects.get(nombre='Accesorios')),
    Producto(nombre='Perfume Chanel', descripcion='Perfume de mujer', precio=120.00, categoria=Categoria.objects.get(nombre='Perfumería')),
    Producto(nombre='Colonia Hugo Boss', descripcion='Colonia de hombre', precio=90.00, categoria=Categoria.objects.get(nombre='Perfumería')),
    Producto(nombre='Aspiradora Dyson', descripcion='Aspiradora sin cable', precio=400.00, categoria=Categoria.objects.get(nombre='Electrodomésticos')),
    Producto(nombre='Microondas LG', descripcion='Microondas con grill', precio=150.00, categoria=Categoria.objects.get(nombre='Electrodomésticos'))
]

for producto in productos:
    producto.save()