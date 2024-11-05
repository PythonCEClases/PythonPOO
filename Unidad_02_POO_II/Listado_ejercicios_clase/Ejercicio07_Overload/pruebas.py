from datetime import date

from clases import *

# Pruebas
pedido1 = Pedido(1, date.today(), "John Doe", ["arroz", "pasta"])
pedido2 = Pedido(2, date.today(), "Jane Doe", ["leche", "huevos"])
pedido3 = Pedido(2, date.today(), "Jane Doe", [])


print(pedido1)
pedido1 + "leche"
pedido1 - "arroz"
print(len(pedido1))

pedido1 += pedido2
print(pedido1)
print(*pedido1.products)


print(bool(pedido1))
print(bool(pedido3))

# order1 += order2

# print(type(order1))
# print(order1.products)
