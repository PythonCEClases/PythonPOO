# Clases del proyecto Sorteo.


class Sorteo:

    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha  # 0       1        2      3        4      5
        self.participantes = ["Juan", "Pedro", "Luis", "Ana", "Maria", "Pepe"]
        self.premios = ["Iphone 15", "Viaje a Cancun", "TV 50 pulgadas"]
        self.sorteo_realizado = False

    def anadir_participante(self, nuevo_participante):
        if nuevo_participante not in self.participantes:
            self.participantes.append(nuevo_participante)
            return True
        return False

    def anadir_premio(self, nuevo_premio):
        if nuevo_premio not in self.premios:
            self.premios.append(nuevo_premio)
            return True
        return False

    def eliminar_participante(self, nombre_participante):
        self.participantes.remove(nombre_participante)

    def eliminar_premio(self, nombre_premio):
        self.premios.remove(nombre_premio)

    def listar_participantes(self):
        print("*****Participantes*****")
        for p in self.participantes:
            print(p)

    def listar_premios(self):
        print("*****Premios*****")
        for p in self.premios:
            print(p)

    def sortear(self):

        import random

        diccionario_premios = {}
        if self.sorteo_realizado == False:

            if len(self.participantes) > len(self.premios) and len(self.premios) > 0:
                # Sorteo
                for premio in self.premios:
                    random.shuffle(self.participantes)  # barajar participantes
                    numero_azar = random.randint(
                        0, len(self.participantes) - 1
                    )  # indice para la lista partic
                    partipante_premiado = self.participantes[numero_azar]
                    # print(f"{partipante_premiado} ---> {premio}")
                    # Introducir pareja participante:premio
                    diccionario_premios[partipante_premiado] = premio
                    self.eliminar_participante(partipante_premiado)
                self.sorteo_realizado = True
                return diccionario_premios
            else:
                return diccionario_premios
        else:
            return -1  # sorteo ya realizado


class Menu:

    def __init__(self, lista_opciones):
        self.lista_opciones = lista_opciones

    def mostrar_menu(self):
        for opcion in self.lista_opciones:
            print(opcion)
        opcion = input("Elige opción: ")
        return opcion
