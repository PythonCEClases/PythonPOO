# Def. de la interfaz y las clases
# que la implementan

from abc import ABC, abstractmethod


class IGestionNumeros(ABC):

    @abstractmethod
    def nuevo_numero(self, numero):
        pass

    @abstractmethod
    def buscar_numero(self, valor):
        pass

    @abstractmethod
    def ordenar(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass


class ListaNumeros(IGestionNumeros):

    def __init__(self, numeros):
        self.numeros = numeros

    def nuevo_numero(self, numero):
        self.numeros.append(numero)

    def buscar_numero(self, valor):
        return True if valor in self.numeros else False

    def ordenar(self):
        self.numeros.sort()

    def mostrar(self):
        print(self.numeros)


class TuplaNumeros(IGestionNumeros):

    def __init__(self, numeros):
        self.numeros = numeros

    def nuevo_numero(self, numero):
        self.numeros += (numero,)

    def buscar_numero(self, valor):
        return True if valor in self.numeros else False

    def ordenar(self):
        self.numeros = tuple(sorted(self.numeros))

    def mostrar(self):
        print(self.numeros)
