import json, csv

def obtener_datos_pais(archivo, codigo_pais):
    todos = leer_archivo(archivo)
    dict_pais = {resultado[0]: list(map(int, resultado[5:])) 
                 for resultado in todos if resultado[4] == codigo_pais}
    return dict_pais
    
    
def leer_archivo(archivo):
    with open(archivo, "r") as archivo:
        lector = csv.reader(archivo)
        cabeceras = next(lector)  # Ignorar cabeceras
        lista = list(lector)
        return lista

def crear_json_pais(archivo_entrada, archivo_json_salida, codigo_pais):
    datos_pais = obtener_datos_pais(archivo_entrada, codigo_pais)
    
    try:
        with open(archivo_json_salida, 'w') as archivo:
            json.dump(datos_pais, archivo, indent=4)
    except IOError as e:
        return False    
    else:
        return True
        