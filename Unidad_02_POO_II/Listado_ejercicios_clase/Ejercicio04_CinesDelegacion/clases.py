# Clases Cine y Salas


class Cine:
    def __init__(self, id, nombre, direccion, telefono, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.salas = [Sala(1, 100, True), Sala(2, 200, False), Sala(3, 150, True)]

    def __str__(self):
        return f"{self.nombre}"

    def __eq__(self, otro):
        return self.id == otro.id

    def agregar_sala(self, numero_sala, capacidad, tres_d):
        sala = Sala(numero_sala, capacidad, tres_d)
        if sala not in self.salas:
            self.salas.append(sala)
            return True
        else:
            return False


class Sala:
    def __init__(self, numero, capacidad, tres_d):
        self.numero = numero
        self.capacidad = capacidad
        self.tres_d = tres_d


class CinesListado:

    lista_cines = [
        Cine(1, "Cinepolis", "Av. Warner Sur 123", "924334949", "cinepolis@cine.es"),
        Cine(
            2,
            "Cine y palomitas",
            "Av. Hitchcock 456",
            "924004949",
            "cinepalomitas@cines.es",
        ),
        Cine(3, "Cine Tonalá", "Tonalá 123", "924004949", "cinetonalá@cines.es"),
        Cine(4, "Ramoncine", "Ramonción 123", "924000001", "ramoncine@abc.es"),
    ]

    @classmethod
    def agregar_cine(cls, cine):
        if cine not in cls.lista_cines:
            cls.lista_cines.append(cine)
            return True
        return False

    @classmethod
    def lista_nombres_cines(cls):
        return [cine.nombre for cine in cls.lista_cines]

    @classmethod
    def dicc_cine_telefono(cls):
        return {cine.nombre: cine.telefono for cine in cls.lista_cines}

    @classmethod
    def dicc_cine_num_salas(cls):
        return {cine.nombre: len(cine.salas) for cine in cls.lista_cines}

    @classmethod
    def capacidad_total_cine(cls, id_cine):
        cine = cls.buscar_cine_id(id_cine)
        return sum([sala.capacidad for sala in cine.salas])

    @classmethod
    def buscar_cine_id(cls, id_cine):
        for cine in cls.lista_cines:
            if cine.id == id_cine:
                return cine
        return None
