from datetime import date

from clases import *

# Pruebas
order1 = Order(1, date.today(), "John Doe", ["arroz", "pasta"])
order2 = Order(2, date.today(), "Jane Doe", ["leche", "huevos"])
# print(order1)
# order1 + "leche"
# print(order1.products)
# print(bool(order1))

order1 += order2

print(type(order1))
print(order1.products)
