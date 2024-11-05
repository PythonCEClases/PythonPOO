from clases import *

mis_vehiculos = GestionVehiculos()

# Añadir vehículos
mis_vehiculos.add_vehiculo(Turismo("1234ABC", "Seat", "Ibiza", 12000, 5, "Diesel"))
mis_vehiculos.add_vehiculo(
    Turismo("9882BGG", "Renault", "Megane", 15000, 5, "Gasolina")
)
mis_vehiculos.add_vehiculo(Furgoneta("2232LLM", "Renault", "Kangoo", 15000, 1000))
mis_vehiculos.add_vehiculo(Autobus("9090KSL", "Mercedes", "Tourismo", 120000, 50))

# Buscar x matrícula
v = mis_vehiculos.buscar_vehiculo_matricula("2232LLM")
print(v)  # polimorfismo

# Modificar carga furgoneta
result = mis_vehiculos.modifica_carga_furgoneta("2232LLM", 2000)
print(result)
print(v)  # Comprobar si se hizo cambio

# Mostrar vehículos
mis_vehiculos.mostrar_vehiculos()  # polimorfismo. Se lla a __str__ de cada clase

# Incrementar precio de un vehículo
v.incrementar_precio(1000)
print(v)  # Comprobar si se hizo cambio

# Marcas de los vehículos
marcas = mis_vehiculos.listado_marcas()
print(*marcas, sep=", ")

# Tupla de vehículos x tipo
tupla = mis_vehiculos.vehiculos_por_tipo("furgoneta")
print(*tupla, sep="\n")
