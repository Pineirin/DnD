import EntidadControlable


class Raza_Humano(EntidadControlable.EntidadControlable):
    fuerza = ...  # type: int
    destreza = ...  # type: int
    constitucion = ...  # type: int
    inteligencia = ...  # type: int
    sabiduria = ...  # type: int
    carisma = ...  # type: int

    def __init__(self):
        self.fuerza = 1
        self.destreza = 1
        self.constitucion = 1
        self.inteligencia = 1
        self.sabiduria = 1
        self.carisma = 1


class Raza_Enano_Colinas(EntidadControlable.EntidadControlable):
    fuerza = ...  # type: int
    destreza = ...  # type: int
    constitucion = ...  # type: int
    inteligencia = ...  # type: int
    sabiduria = ...  # type: int
    carisma = ...  # type: int

    def __init__(self):
        self.fuerza = 0
        self.destreza = 0
        self.constitucion = 4
        self.inteligencia = 0
        self.sabiduria = 1
        self.carisma = 0
