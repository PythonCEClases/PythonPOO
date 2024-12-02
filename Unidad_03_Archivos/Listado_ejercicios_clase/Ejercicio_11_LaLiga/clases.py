# Clases del proyecto.
import csv
import json
import os
from collections import defaultdict


class Partido:
    def __init__(
        self,
        jornada,
        fecha,
        local,
        visitante,
        goles_local,
        goles_visitante,
        total_goles,
        ganador,
    ):
        self.jornada = jornada
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.total_goles = total_goles
        self.ganador = ganador

    def __str__(self):
        return (
            f"{self.local} {self.goles_local} - {self.goles_visitante} {self.visitante}"
        )


class Liga:

    def __init__(self, archivo):
        self.partidos = []
        datos_partidos = self.__leer_archivo(archivo)
        for dato in datos_partidos:
            (
                jornada,
                fecha,
                local,
                visitante,
                goles_local,
                goles_visitante,
                total_goles,
                ganador,
            ) = dato
            partido = Partido(
                jornada,
                fecha,
                local,
                visitante,
                goles_local,
                goles_visitante,
                total_goles,
                ganador,
            )
            self.partidos.append(partido)

    def __leer_archivo(self, archivo):

        try:
            with open(archivo, "r") as archivo:
                csv_reader = csv.reader(archivo)
                next(csv_reader)
                return list(csv_reader)

        except IOError as error:
            raise error

    def partidos_local_csv(self, equipo):
        ruta_abs = os.path.abspath(__file__)
        directorio = os.path.dirname(ruta_abs)

        # archivo de salida: equipo_local_2324.csv
        nombre_archivo_salida = f"{equipo}_local_2324.csv"
        archivo_salida = os.path.join(directorio, nombre_archivo_salida)

        try:
            with open(archivo_salida, "w", encoding="utf8") as file:
                csv_writer = csv.writer(file, delimiter=",", lineterminator="\n")
                lista = []
                for partido in self.partidos:
                    if partido.local.lower() == equipo.lower():
                        # Obtenemos una lista con los valores del objeto
                        lista.append(partido)
                lista = sorted(lista, key=lambda p: int(p.jornada))
                for p in lista:
                    csv_writer.writerow(p.__dict__.values())

            return archivo_salida
        except IOError:
            return None

    def partido_equipo_json(self, equipo):
        ruta_abs = os.path.abspath(__file__)
        directorio = os.path.dirname(ruta_abs)

        # archivo de salida: equipo_local_2324.csv
        nombre_archivo_salida = f"{equipo}_2324.json"
        archivo_salida = os.path.join(directorio, nombre_archivo_salida)

        try:
            with open(archivo_salida, "w", encoding="utf8") as file:
                partidos = {}
                for partido in self.partidos:
                    if (
                        partido.local.lower() == equipo.lower()
                        or partido.visitante.lower() == equipo.lower()
                    ):
                        partidos[partido.jornada] = partido.__dict__

                # Ordenar el dicc por key. Al ser str convertirmos a int.
                partidos = dict(sorted(partidos.items(), key=lambda item: int(item[0])))
                print(partidos)
                json.dump(partidos, file, indent=4)

            return archivo_salida
        except IOError:
            return None

    def clasificacion_liga_2324(self):
        # Diccionario para guardar la clasif. equipo:puntos.
        # En este caso utilizo un objeto defaultdict, ya que 
        # podemos acumular de forma más ágil los puntos. Líneas 142 y 143
        
        clasificacion = defaultdict(int)        
        for partido in self.partidos:
            puntos_local = 0
            puntos_visitante = 0
            if partido.ganador == "Home":
                puntos_local = 3
            elif partido.ganador == "Away":
                puntos_visitante = 3
            else:
                puntos_local = 1
                puntos_visitante = 1

            clasificacion[partido.local] += puntos_local
            clasificacion[partido.visitante] += puntos_visitante

            # Ordenar el dicconario x valor (posición 1)
            ordenado = dict(sorted(clasificacion.items(),
                                   key= lambda x: x[1],
                                   reverse=True))
        return ordenado
