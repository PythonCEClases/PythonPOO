import os
from clases import GestionCsv

ruta_absoluta = os.path.abspath(__file__ )
ruta_directorio = os.path.dirname(ruta_absoluta)
archivo_entrada = os.path.join(ruta_directorio, 'user_behavior_dataset.csv')

# Obtner csv de la marca Xiaomi Mi 11
# movil_device = 'Xiaomi Mi 11'
# result = GestionCsv.obtener_csv_por_dispositivo(archivo_entrada, movil_device)
# if result:
#     print(f'Archivo "{movil_device}.csv" creado con éxito.')
# else:
#     print('Error al crear el archivo.')

# Obtener diccionario con cuenta x marca SO
# result = GestionCsv.contar_por_sistema_operativo(archivo_entrada)
# if result:
#     print(result)

# Obtener csv time y gender
# result = GestionCsv.obtener_csv_time_gender(archivo_entrada)
# if result:
#     print(f'Archivo generado.')
# else:
#     print(f'Error al crear el archivo')

GestionCsv.generar_csv_por_marca(archivo_entrada)