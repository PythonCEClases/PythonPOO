# Definición de clases
from abc import ABC, abstractmethod


class Participante:
    def __init__(self, nombre, apellidos, correo_electronico):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo_electronico = correo_electronico

    def __str__(self):
        return f"{self.nombre} {self.correo_electronico}"

    def __eq__(self, otro_participante):
        return self.correo_electronico == otro_participante.correo_electronico


class Premio:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def __str__(self):
        return f"{self.descripcion} - {self.valor}"

    def __eq__(self, otro_premio):
        return (
            self.descripcion == otro_premio.descripcion
            and self.valor == otro_premio.valor
        )


class ISorteable(ABC):

    @abstractmethod
    def add_participante(self, participante):
        pass

    @abstractmethod
    def add_premio(self, premio):
        pass

    @abstractmethod
    def sortear(self):
        pass


class Sorteo(ISorteable):
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.premios = []
        self.participantes = {}

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"

    def add_participante(self, participante):
        if participante.correo_electronico not in self.participantes:
            self.participantes[participante.correo_electronico] = participante
            return True
        return False

    def add_premio(self, premio):
        if premio not in self.premios:
            self.premios.append(premio)
            return True
        return False

    def sortear(self):
        import random

        correos_participantes_copia = self.participantes.keys()
        resultado_sorteo = {}
        for premio in self.premios:
            random.shuffle(correos_participantes_copia)
            numero_participantes = len(correos_participantes_copia)
            correo_azar = correos_participantes_copia[
                random.randint(0, numero_participantes)
            ]
            resultado_sorteo[correo_azar] = premio
        return resultado_sorteo
