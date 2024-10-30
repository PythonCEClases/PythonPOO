# JuaJuego Amigo Invisible con Python
# Clases Persona y AmigoInvisible


class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"{self.nombre} <{self.email}>"

    def __eq__(self, otra_persona):
        return (
            self.email == otra_persona.email
            or self.nombre.lower() == otra_persona.nombre.lower()
        )

    def __hash__(self):
        return hash(self.email)


class AmigoInvisible:
    def __init__(self, descripcion, fecha_evento):
        self.descripcion = descripcion
        self.fecha_evento = fecha_evento
        self.personas = []

    def agregar_persona(self, nombre_persona, email_persona):
        persona = Persona(nombre_persona, email_persona)
        if persona in self.personas:
            return False
        self.personas.append(persona)
        return True

    def mostrar_personas(self):
        print("Lista de personas:")
        print(*self.personas, sep="\n")

    def sortear(self):

        import random

        random.shuffle(self.personas)

        parejas = {}
        for i in range(len(self.personas)):
            if i == len(self.personas) - 1:
                parejas[self.personas[i]] = self.personas[0]
            else:
                parejas[self.personas[i]] = self.personas[i + 1]
        return parejas
