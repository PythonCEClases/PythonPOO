import datetime

from clases import *

juego = AmigoInvisible("Amigo invisible 2024", datetime.date(2024, 12, 24))
juego.agregar_persona("Juan", "juan@ggmail.com")
juego.agregar_persona("Ana", "ana@ggmail.net")
juego.agregar_persona("Luis", "luis@gggmail.com")
juego.agregar_persona("Maria", "maria@gggmail.com")
juego.agregar_persona("Juan", "juan@ggmail.com")
juego.agregar_persona("Elena", "elena@ggmail.com")

juego.mostrar_personas()

parejas = juego.sortear()
for key in parejas.keys():
    print(f"{key} regala a  -> {parejas[key]}")
