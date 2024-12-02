import json, csv

def obtener_datos_pais(archivo, codigo_pais):
    todos = leer_archivo(archivo)
    dict_pais = {resultado[0]: list(map(int, resultado[5:])) for resultado in todos if resultado[4] == codigo_pais}
    return dict_pais
    
    
def leer_archivo(archivo):
    with open(archivo, "r") as archivo:
        lector = csv.reader(archivo)
        cabeceras = next(lector)  # Ignorar cabeceras
        lista = list(lector)
        return lista