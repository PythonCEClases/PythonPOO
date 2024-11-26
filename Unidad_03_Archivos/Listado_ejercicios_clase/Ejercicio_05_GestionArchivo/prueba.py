import os

from clases import GestionArchivo

ruta_archivo = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_archivo)
archivo_ent = os.path.join(directorio, "operaciones.txt")

# Buscar la cadena 'insert' en el archivo 'operaciones.txt'
cadena_buscada = "insert"
result = GestionArchivo.buscar_cadena_archivo(cadena_buscada, archivo_ent)
if result == -1:
    print(f'Error al leer el archivo "{archivo_ent}"')
else:
    print(
        f"La cadena '{cadena_buscada}' {'sí' if result else 'no'} se encuentra en el archivo."
    )

# Contar las repeticiones de la cadena 'update' en el archivo 'operaciones.txt'
cadena_buscada = "update"
result = GestionArchivo.contar_repeticiones(cadena_buscada, archivo_ent)
if result == -1:
    print(f'Error al leer el archivo "{archivo_ent}"')
else:
    print(f"La cadena '{cadena_buscada}' se repite {result} veces en el archivo.")

# Mostrar las líneas que contienen la cadena 'update' en el archivo 'operaciones.txt'
cadena_buscada = "update"
result = GestionArchivo.mostrar_cadena_archivo(cadena_buscada, archivo_ent)
if result == -1:
    print(f'Error al leer el archivo "{archivo_ent}"')
else:
    print(f"Las líneas que contienen la cadena '{cadena_buscada}' son: {result}")
