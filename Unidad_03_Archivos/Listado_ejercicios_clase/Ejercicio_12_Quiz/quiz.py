import os
from clases import *

# Archivo configuración: config.json 
archivo_config_json = os.path.join(os.path.dirname(__file__), "config.json")

# Cargar configuración
config = Config(archivo_config_json)
archivo_preguntas = config.dict_config.get("archivo_preguntas", None)
archivo_top3 = config.dict_config.get("archivo_top3", None)
numero_preguntas = config.dict_config.get("numero_preguntas", None)
puntuacion_pregunta = config.dict_config.get("puntuacion_pregunta", None)

archivo_preguntas_json = os.path.join(os.path.dirname(__file__), archivo_preguntas)
archivo_top3_json = os.path.join(os.path.dirname(__file__), archivo_top3)

# Cargar preguntas
preguntas = Preguntas(archivo_preguntas_json)

# Cargar Top 3
top3 = Top3(archivo_top3_json)


# Menú opciones
opciones = ["1. Jugar", "2. Configuración", "3. Top 3", "4. Salir"]
menu = Menu(opciones)

while True:
    opcion = menu.mostrar()
    if opcion == "1":
        # Jugar
        jugar = Jugar(numero_preguntas, puntuacion_pregunta, preguntas)
        jugar.jugando()
        puntos = jugar.puntuacion
        jugador = jugar.jugador
        # Comprobar si es Top 3.
        result = top3.comprobar_top3(jugador, puntos)
        if result:
            # Guardar Top 3
            print("¡Felicidades! Has entrado en el Top 3")
            top3.guardar_top3()
    elif opcion == "2":
        # Configuración
        print("Configuración")
        config.mostrar_configuracion()
        
    elif opcion == "3":
        top3.mostrar_top3()
        
    elif opcion == "4":
        # Salir
        break
    else:
        print("Opción no válida")    

