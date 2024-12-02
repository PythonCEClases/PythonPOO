import csv
import os

class GestionCsv:
    
    @staticmethod
    def obtener_csv_por_dispositivo(archivo_entrada, dispositivo):
        
        try:
            with open(archivo_entrada, 'r') as entrada:
        
                lector = csv.reader(entrada)
                cabeceras = next(lector)
                
                archivo_salida = os.path.abspath(
                    os.path.join(os.path.dirname(archivo_entrada), 
                    dispositivo + '.csv'))
                
                with open(archivo_salida, 'w') as salida:
                    escritor = csv.writer(salida, delimiter=',', lineterminator='\n')        
                    escritor.writerow(cabeceras)
                    for linea in lector:
                        if linea[1] == dispositivo:
                            escritor.writerow(linea)
                        
        except IOError as e:
            return False
        else:
            return  True
    
    def contar_por_sistema_operativo(archivo_entrada):
        try:
            with open(archivo_entrada, 'r') as entrada:
                
                lector = csv.reader(entrada)
                cabeceras = next(lector)
                diccionario = {}
                lista = list(lector)
                for linea in lista:
                    if linea[2] in diccionario:
                        diccionario[linea[2]] += 1
                    else:
                        diccionario[linea[2]] = 1
        except IOError as e:
            return False
        else:
            return diccionario        
 
    def obtener_csv_time_gender(archivo_entrada):
        
        try:
                
            archivo_salida = os.path.abspath(
                os.path.join(os.path.dirname(archivo_entrada), 
                'time_gender.csv'))
            
            with open(archivo_salida, 'w') as salida:
                csv_writer = csv.writer(salida, delimiter=',', lineterminator='\n')
                
                with open(archivo_entrada, 'r', encoding='utf8') as entrada:
                    csv_reader = csv.DictReader(entrada)
                    csv_writer.writerow(['App Usage Time (min/day)', 'Gender'])
                    for linea in csv_reader:
                        csv_writer.writerow([linea['App Usage Time (min/day)'], linea['Gender']])
                    
        except IOError:
            return False
        else:
            return True       
    
    