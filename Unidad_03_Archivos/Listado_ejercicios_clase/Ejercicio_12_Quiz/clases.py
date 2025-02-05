import json
import os
import random


class Menu:

    def __init__(self, opciones):
        self.opciones = opciones

    def mostrar(self):
        for opcion in self.opciones:
            print(opcion)
        opcion = input("Elige una opción: ")
        return opcion


class Config:

    def __init__(self, archivo):
        self.archivo = archivo
        self.dict_config = self.__cargar_configuracion()
            
    def __cargar_configuracion(self):
        dict_config = {
            "numero_preguntas": 5, 
            "puntuacion_pregunta": 1,
            "archivo_preguntas": "questions.json",
            "archivo_top3": "top3.json"
        }               
        
        try:
            with open(archivo, "r") as archivo:
                dict_config = json.load(archivo)
        finally:
            return dict_config

    def guardar_configuracion(self):
        try:
            with open(archivo, "w") as archivo:
                json.dump(self.dict_config, archivo)
        except IOError as e:
            return False
        else:
            return True
        
    def mostrar_configuracion(self):
        print("\n\nConfiguración actual:")
        for key, value in self.dict_config.items():
            print(f"{key}: {value}")
            
    def cambiar_configuracion(self):
        self.mostrar_configuracion()
        print("\n\nIntroduce los nuevos valores:")
        for key in self.dict_config.keys():
            value = input(f"{key}: ")
            self.dict_config[key] = value
        self.guardar_configuracion()
            

class Preguntas:
    
    def __init__(self, archivo):
        self.dict_preguntas = self.__cargar_preguntas(archivo)
        
    def __cargar_preguntas(self, archivo):
        try:
            with open(archivo, "r") as archivo:
                self.dict_preguntas = json.load(archivo)
                return self.dict_preguntas
        except IOError as e:
            return None
        
    def obtener_lista_preguntas(self, numero_preguntas):
        lista_preguntas = random.sample(self.dict_preguntas, numero_preguntas)
        return lista_preguntas
    
class Jugar:
    
    def __init__(self, numero_preguntas, puntuacion_pregunta, preguntas):
        self.las_preguntas = preguntas.obtener_lista_preguntas(numero_preguntas)
        self.puntuacion = 0
        self.jugador = ""
        self.puntuacion_pregunta = puntuacion_pregunta
        
    def jugando(self):
        self.jugador = input("Introduce tu nombre: ")
        for pregunta in self.las_preguntas:
            print(pregunta["question"])
            print(pregunta["A"])
            print(pregunta["B"])
            print(pregunta["C"])
            print(pregunta["D"])
            
            respuesta = input("Introduce tu respuesta: ")
            if respuesta.upper() == pregunta['answer']:
                self.puntuacion += self.puntuacion_pregunta
        

class Top3:
        
    def __init__(self, archivo):
        self.archivo = archivo
        self.top3 = self.__cargar_top3()
        
    def __cargar_top3(self):
        try:
            with open(self.archivo, "r") as top3_file:
                self.top3 = json.load(top3_file)
                return self.top3
        except IOError as e:
            return {
                "top3":[
                    {
                        "name": "x",
                        "score": 0
                    },
                    {
                        "name": "y",
                        "score": 0
                    },
                    {
                        "name": "z",
                        "score": 0
                    }                    
                ]
            }
        
    def comprobar_top3(self, jugador, puntuacion):
        los_top3 = self.top3["top3"]
         
        if puntuacion > los_top3[2]["score"]:
            los_top3[2]["name"] = jugador
            los_top3[2]["score"] = puntuacion
            los_top3 = sorted(los_top3, key=lambda x: x["score"], reverse=True)
            self.top3["top3"] = los_top3
            return True
        else:
            return False
        
    def guardar_top3(self):
        try:
            with open(self.archivo, "w") as top3_file:
                json.dump(self.top3, top3_file, indent=4)
        except IOError as e:
            return False
        else:
            return True        
        
    def mostrar_top3(self):
        datos_top3 = self.top3["top3"]
        print("\n\nTop 3:")
        for elemento in datos_top3:
            print(f"{elemento['name']}: {elemento['score']}")
        