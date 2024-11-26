from datetime import date

from clases import *

# Añadir
# sorteo_navidad.anadir_participante('Lebron James')
# sorteo_navidad.anadir_premio('Cesta fruta')
# sorteo_navidad.anadir_premio('Cesta Navidad')

# Eliminar
# sorteo_navidad.eliminar_participante('Ana')
# sorteo_navidad.eliminar_premio('Cesta fruta')

# # Listar
# sorteo_navidad.listar_participantes()
# sorteo_navidad.listar_premios()

# dicc = sorteo_navidad.sortear()

# if len(dicc) > 0:
#     for participante,premio in dicc.items():
#         print(f"{participante} ---> {premio}")
# else:
#     print("Error")
opciones = [
    "Menu",
    "1. Añadir participante",
    "2. Añadir premio",
    "3. Eliminar participante",
    "4. Eliminar premio",
    "5. Lista parcipante",
    "6. Listar premios",
    "7. Sortear",
    "8. Fin",
]

menu = Menu(opciones)
sorteo_navidad = Sorteo("Sorteo Navidad", date(2024, 12, 12))

while True:
    opcion = menu.mostrar_menu()
    match opcion:
        case "1":
            # Añadir parti.
            nuevo_par = input("Teclee nombre participante")
            result = sorteo_navidad.anadir_participante(nuevo_par)
            if result:
                print("Añadido.")
            else:
                print("No se pudo añadir.")
        case "2":
            # Añadir premio
            nuevo_premio = input("Teclee premio")
            result = sorteo_navidad.anadir_premio(nuevo_premio)
            if result:
                print("Añadido.")
            else:
                print("No se pudo añadir.")
        case "3":
            # Eliminar participante
            nombre_participante = input("Teclee nombre de particpante a eliminar")
            sorteo_navidad.eliminar_participante(nombre_participante)
        case "4":
            # Eliminar premio
            nombre_premio = input("Teclee nombre de premio a eliminar")
            sorteo_navidad.eliminar_premio(nombre_premio)
        case "5":
            # Listar participantes.
            sorteo_navidad.listar_participantes()
        case "6":
            # Listar premios
            sorteo_navidad.listar_premios()
        case "7":
            # Sortear
            result = sorteo_navidad.sortear()
            print("*********Resultado del sorteo***********")
            if result == -1:  # sorteo ya realizado
                print("Sorteo ya realizado")
            else:
                for participante, premio in result.items():
                    print(f"{participante} ---> {premio}")
        case "8":
            print("Has pulsado fin")
            break
        case _:  # en caso de teclear algo no sea 1..8
            print("Error en la opción")
