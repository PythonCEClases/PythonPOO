from datetime import date

from clases import Cliente, Vehiculo, VehiculoAlquilado

cliente1 = Cliente(1, "Juan", "Perez", "juanperez@go.es")
vehiculo1 = Vehiculo("1234ABC", "Ford", "Focus", 100, 50)
alquiler1 = VehiculoAlquilado(vehiculo1, cliente1, date.today(), 5)

cliente2 = Cliente(2, "Ana", "Lopez", "ana@casa.com")
vehiculo2 = Vehiculo("5678DEF", "Seat", "Ibiza", 90, 40)
alquiler2 = VehiculoAlquilado(vehiculo2, cliente2, date(2024, 10, 10), 10)

print(alquiler1.importe_alquiler())
print(alquiler2.importe_alquiler())
