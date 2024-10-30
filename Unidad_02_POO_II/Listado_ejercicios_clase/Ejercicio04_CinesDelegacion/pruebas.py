from clases import Cine, CinesListado, Sala

# Crear un cine y añadir dos salas
nuevo_cine = Cine(
    5, "Cine de la esquina", "Calle de la esquina 123", "924000001", "esquina@cines.es"
)
nuevo_cine.agregar_sala(4, 100, True)
nuevo_cine.agregar_sala(5, 200, False)
nuevo_cine.agregar_sala(5, 200, False)  # esta sala ya existe

# Añadir el cine a la lista de cines
CinesListado.agregar_cine(nuevo_cine)

# Mostrar los nombres de los cines
print(CinesListado.lista_nombres_cines())

# Mostrar dicc cine-telefono
dicc = CinesListado.dicc_cine_telefono()
print(dicc)

# Mostrar dicc cine-numero_salas
dicc = CinesListado.dicc_cine_num_salas()
print(dicc)

# Mostrar la capacidad total de un cine
print(CinesListado.capacidad_total_cine(5))
