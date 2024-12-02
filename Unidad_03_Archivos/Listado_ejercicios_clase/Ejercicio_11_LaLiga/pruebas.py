import os

from clases import Liga, Partido

ruta_abs = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_abs)
archivo = os.path.join(directorio, "LaLiga2324.csv")

try:
    liga = Liga(archivo)

    clasificacion = liga.clasificacion_liga_2324()
    for equipo, puntos in clasificacion.items():
        print(f'{equipo} - {puntos}')
    #liga.partidos_visitante_csv("Real Madrid")
    # result = liga.partido_equipo_json("Real Madrid")
    # result = liga.partido_equipo_json("Real Madrid")
    # if result:
    #     print("Archivo creado")

except FileNotFoundError:
    print("No se ha encontrado el archivo")
