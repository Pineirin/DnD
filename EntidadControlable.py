import random


class EntidadControlable:

    def atacar_fuerza(self, monstruo: object, arma: int):
        if random.randrange(1, 20) + self.fuerza + 2> monstruo.armadura:
            golpe = arma + self.fuerza
            if golpe <= 0:
                golpe = 1
            print("Jugador infringió a " + type(monstruo).__name__ + " " + str(golpe) + " puntos de daño")
            monstruo.vida = monstruo.vida - golpe
        else:
            print("Jugador atacó y falló")

    def atacar_destreza(self, monstruo: object, arma: int):
        if random.randrange(1, 20) + self.destreza + 2 > monstruo.armadura:
            golpe = arma + self.destreza
            if golpe <= 0:
                golpe = 1
            print("Jugador infringió a " + type(monstruo).__name__ + " " + str(golpe) + " puntos de daño")
            monstruo.vida = monstruo.vida - golpe
        else:
            print("Jugador atacó y falló")

    def pasar_turno(self):
        pass

    def actions(self) -> list:
        actions = []
        methods = self.__dir__()
        for method in methods:
            if "action_" in method:
                actions.append(method.replace("action_", ""))
        return actions

    def execute(self, string: str, jugador: object, aliados: list, monstruos: list):
        result = getattr(self, "action_" + string)
        result(jugador, aliados, monstruos)