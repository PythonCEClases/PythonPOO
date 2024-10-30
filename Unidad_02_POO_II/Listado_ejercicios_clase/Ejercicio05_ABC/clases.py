from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, matricula, marca, modelo, precio):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Marca: {self.marca} -{self.modelo}, Precio: {self.precio}"

    def __eq__(self, otro_vehiculo):
        return self.matricula == otro_vehiculo.matricula


class Turismo(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas, tipo_combustible):
        super().__init__(marca, modelo, precio)
        self.puertas = puertas
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        return f"Turismo: {super().__str__()} - Combustible: {self.tipo_combustible}"


class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, precio, carga):
        super().__init__(marca, modelo, precio)
        self.carga = carga

    def __str__(self):
        return f"Furgoneta: {super().__str__()} - Carga: {self.carga}"


class Autobus(Vehiculo):
    def __init__(self, marca, modelo, precio, asientos):
        super().__init__(marca, modelo, precio)
        self.asientos = asientos

    def __str__(self):
        return f"Autobus: {super().__str__()} - Asientos: {self.asientos}"


class GestionVehiculos:
    def __init__(self):
        self.vehiculos = []

    def add_vehiculo(self, vehiculo):
        if not vehiculo in self.vehiculos:
            self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for v in self.vehiculos:
            print(v)

    def marcas(self):
        return set([v.marca for v in self.vehiculos])

    def vehiculos_tipo(self, tipo):
        return tuple(
            v
            for v in self.vehiculos
            if (tipo.lower() == "turismo" and isinstance(v, Turismo))
            or (tipo.lower() == "furgoneta" and isinstance(v, Furgoneta))
            or (tipo.lower() == "autobus" and isinstance(v, Autobus))
        )
