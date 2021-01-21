import random


class Monstruo:

    def atacar_fuerza(self, jugador: object):
        if random.randrange(1, 20) + self.fuerza + 2 > jugador.armadura:
            golpe = self.arma() + self.fuerza
            if golpe <= 0:
                golpe = 1
            print(type(self).__name__ + " " + str(self.id) + " infringió " + str(golpe) + " puntos de daño")
            jugador.vida = jugador.vida - golpe
        else:
            print(type(self).__name__ + " " + str(self.id) +" atacó y falló")

    def atacar_destreza(self, jugador: object):
        if random.randrange(1, 20) + self.destreza + 2 > jugador.armadura:
            golpe = self.arma() + self.destreza
            if golpe <= 0:
                golpe = 1
            print(type(self).__name__ + " infringió " + str(golpe) + " puntos de daño")
            jugador.vida = jugador.vida - golpe
        else:
            print(type(self).__name__ + " " + str(self.id) +" atacó y falló")

class Zombie(Monstruo):
    id = ...  # type: int
    fuerza = ...  # type: int
    destreza = ...  # type: int
    constitucion = ...  # type: int
    inteligencia = ...  # type: int
    sabiduria = ...  # type: int
    carisma = ...  # type: int
    vida = ...  # type: int
    xp = ...  # type: int
    
    def __init__(self, id: int):
        self.id = id
        self.fuerza = 1
        self.destreza = -2
        self.constitucion = 3
        self.inteligencia = -4
        self.sabiduria = -2
        self.carisma = -3
        self.armadura = 8
        self.vida = random.randrange(1, 8) + random.randrange(1, 8) + random.randrange(1, 8) + 9
        self.xp = 50

    def arma(self) -> int:
        return random.randrange(1, 6)
