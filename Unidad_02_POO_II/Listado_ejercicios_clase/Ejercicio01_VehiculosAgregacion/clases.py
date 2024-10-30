# Clases Vehiculo, Cliente y VehiculoAlquilado


class Vehiculo:
    def __init__(self, matricula, marca, modelo, potencia, precio_alquiler):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.precio_alquiler = precio_alquiler

    def __str__(self):
        print(
            f"Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio_alquiler}"
        )


class Cliente:
    def __init__(self, id, nombre, apellidos, correo):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo

    def __str__(self):
        print(
            f"Nombre: {self.nombre} - Apellidos: {self.apellidos} - Telefono: {self.telefono}"
        )


class VehiculoAlquilado:
    def __init__(self, vehiculo, cliente, fecha_alquiler, numero_dias):
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.fecha_alquiler = fecha_alquiler
        self.numero_dias = numero_dias

    def __str__(self):
        print(
            f"Vehiculo: {self.vehiculo} - Cliente: {self.cliente} - Fecha: {self.fecha_alquiler} - Dias: {self.numero_dias}"
        )

    def importe_alquiler(self):
        return self.vehiculo.precio_alquiler * self.numero_dias
