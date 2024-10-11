# clase vehículo
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.precio}"
