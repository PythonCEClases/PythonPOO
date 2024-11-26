from datetime import date

from clases import *

juego = Sorteo("Navidad", date(2024, 12, 12))
juego.add_participante(Participante("Juan", "Perez", "juan@gmail.com"))
juego.add_participante(Participante("Maria", "Gomez", "maria@gmail.com"))
juego.add_participante(Participante("Eva", "Casas", "eva@gmail.com"))
juego.add_participante(Participante("Mari", "Robles", "mari@gmail.com"))

juego.add_premio(Premio("Viaje a Cancun", 1000))
juego.add_premio(Premio("Cena en Restaurante", 100))

resultado = juego.sortear()
print(resultado)
