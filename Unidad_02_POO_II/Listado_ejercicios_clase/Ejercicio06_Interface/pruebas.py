from clases_interfaces import *

# list
lista1 = ListaNumeros([1, 10, 2, -4])
lista1.nuevo_numero(33)
lista1.ordenar()
lista1.mostrar()
print(f"Buscando: {lista1.buscar_numero(10)}")

# tuple
t = TuplaNumeros((1, 10, 2, -4))
t.nuevo_numero(33)

t.ordenar()
t.mostrar()
print(f"Buscando: {t.buscar_numero(10)}")
