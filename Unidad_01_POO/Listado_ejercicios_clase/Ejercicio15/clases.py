class Ciudad:
    def __init__(self, nombre, poblacion, pais, continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.pais = pais
        self.continente = continente

    def __str__(self):
        return (
            self.nombre
            + "-"
            + str(self.poblacion)
            + "-"
            + self.pais
            + "-"
            + self.continente
        )

    def __eq__(self, otra_ciudad):
        return self.nombre == otra_ciudad.nombre and self.pais == otra_ciudad.pais


class ListaCiudades:
    lista_ciudades = [
        Ciudad("Bogotá", 8000000, "Colombia", "América"),
        Ciudad("Lima", 10000000, "Peru", "America"),
        Ciudad("Paris", 5000000, "Francia", "Europa"),
        Ciudad("Berlin", 4000000, "Alemania", "Europa"),
        Ciudad("Tokio", 9000000, "Japón", "Asia"),
        Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
        Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
        Ciudad("Moscú", 10000000, "Rusia", "Europa"),
        Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
        Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
        Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
        Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
        Ciudad("Roma", 4000000, "Italia", "Europa"),
        Ciudad("Pekín", 20000000, "China", "Asia"),
        Ciudad("Delhi", 15000000, "India", "Asia"),
        Ciudad("El Cairo", 7000000, "Egipto", "África"),
        Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
        Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
        Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
        Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
        Ciudad("Madrid", 6000000, "España", "Europa"),
        Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
    ]

    @classmethod
    def mostrar_ciudades_continente(cls, continente):
        for c in cls.lista_ciudades:
            if c.continente.lower() == continente.lower():
                print(c)

    @classmethod
    def ciudades_poblacion_mayor(cls, poblacion):
        for c in cls.lista_ciudades:
            if c.poblacion > poblacion:
                print(c)

    @classmethod
    def contar_ciudades_pais(cls, pais):
        contador = 0
        for c in cls.lista_ciudades:
            if c.pais.lower() == pais.lower():
                contador += 1
        return contador

    @classmethod
    def contar_ciudades_patron(cls, patron):
        contador = 0
        for c in cls.lista_ciudades:
            if patron in c.nombre:
                contador += 1
        return contador

    @classmethod
    def media_poblacion_ciudades_pais(cls, pais):
        cuenta_ciudades = cls.contar_ciudades_pais(pais)
        suma_poblacion = 0
        for c in cls.lista_ciudades:
            if c.pais == pais:
                suma_poblacion += c.poblacion
        return suma_poblacion / cuenta_ciudades

    @classmethod
    def ciudades_pais(cls, pais):
        return [c for c in cls.lista_ciudades if c.pais == pais]

    @classmethod
    def ciudades_continente(cls, continente):
        return [c for c in cls.lista_ciudades if c.continente == continente]

    @classmethod
    def suma_total_habitantes(cls):
        return sum([c.poblacion for c in cls.lista_ciudades])

    @classmethod
    def add_ciudad(cls, ciudad):
        if ciudad not in cls.lista_ciudades:
            cls.lista_ciudades.append(ciudad)
            return True
        else:
            return False
