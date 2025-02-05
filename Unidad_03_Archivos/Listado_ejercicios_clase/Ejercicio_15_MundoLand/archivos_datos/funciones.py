# Cargar datos de mamíferos
import json
import os


def cargar_mamiferos():
    archivo_mamiferos = os.path.join(os.path.dirname(__file__), "mamiferos.json")
    with open(archivo_mamiferos, "r", encoding="utf8") as archivo:
        mamiferos = json.load(archivo)
    return mamiferos


def cargar_plantas():
    archivo_plantas = os.path.join(os.path.dirname(__file__), "plantas.json")
    with open(archivo_plantas, "r", encoding="utf8") as archivo:
        plantas = json.load(archivo)
    return plantas
