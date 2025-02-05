import os, json
from funciones import *

# Pais y archivo de salida
codigo_pais = 'ESP'
nombre_archivo_salida = codigo_pais +'_medallas.json'

# Ruta archivos csv entrada y salida
directorio = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_ent = os.path.join(directorio, 'summer_olympic_medals.csv')
ruta_archivo_sal = os.path.join(directorio, nombre_archivo_salida)

# diccionario con los datos del pais
datos_pais = obtener_datos_pais(ruta_archivo_ent, codigo_pais)

# Imprimir datos del pais
for k,v in datos_pais.items():
    print(f"{k}: {v}")

# Guardar datos del pais en archivo json
result = crear_json_pais(ruta_archivo_ent, ruta_archivo_sal, codigo_pais)
if result:
    print(f"Datos guardados en {os.path.basename(ruta_archivo_sal)}")
else:
    print(f"Error al guardar datos en {os.path.basename(ruta_archivo_sal)}")



