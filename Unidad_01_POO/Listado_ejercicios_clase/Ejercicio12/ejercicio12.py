# Importamos las clases
from clases import Partido, GestionPartidos
from datetime import datetime

# Mostramos los partidos del Real Madrid
print("Partidos del Real Madrid")
GestionPartidos.filtrar_por_equipo_local("Real Madrid")
print()

# Mostramos los partidos ganados por el Real Madrid
print("Ganados por el Real Madrid " + str(GestionPartidos.ganados_del_equipo("Real Madrid")))
print()

# Filtrar los partidos por año
print("Partidos del 2022")
GestionPartidos.partidos_anio(2022)
print()

# Filtrar los partidos por fecha
print("Partidos del 20 de octubre de 2021")
GestionPartidos.partidos_fecha(datetime(2021, 10, 20))
print()

# Mostramos el número de partidos
print("Número de partidos: " + str(GestionPartidos.cuenta_partidos()))
print()

# Añadir un nuevo partido
# Observa como el método recibe un objeto partido como argumento
GestionPartidos.anadir_partido(Partido("Betis", "Alavés", 3, 1, "Copa", datetime(2023, 10, 30)))

# Filtrar por año
print("Partidos del 2023")
GestionPartidos.partidos_anio(2023)
