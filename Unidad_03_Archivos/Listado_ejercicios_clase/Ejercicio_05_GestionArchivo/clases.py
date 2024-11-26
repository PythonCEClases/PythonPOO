class GestionArchivo:

    def buscar_cadena_archivo(cadena, archivo):
        try:
            with open(archivo, "r") as file:
                contenido = file.read()
                return cadena in contenido

        except FileNotFoundError:
            return -1  # Archivo no encontrado

    def contar_repeticiones(cadena, archivo):
        try:
            with open(archivo, "r") as file:
                contenido = file.read()
                return contenido.count(cadena)

        except FileNotFoundError:
            return -1

    def mostrar_cadena_archivo(cadena, archivo):

        try:
            numero_linea = 1
            result = {}
            with open(archivo, "r") as file:
                for linea in file:
                    if cadena in linea:
                        result[numero_linea] = linea.strip()
                    numero_linea += 1
            return result
        except FileNotFoundError:
            return -1  # Archivo no encontrado
