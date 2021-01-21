import random

import EntidadControlable

class Clase_Guerrero(EntidadControlable.EntidadControlable):
    vida = ...  # type: int
    nivel = ...  # type: int
    arma = ...  # type: int
    accion_especial_1 = ...  # type: bool
    tipo_arma = ...  # type: str

    def __init__(self):
        self.vida = 10
        self.nivel = 1
        self.arma = 12
        self.accion_especial_1 = True
        self.tipo_arma = "fuerza"

    def accion_adicional(self, jugador: object, aliados: list, monstruos: list):
        if self.accion_especial_1:
            while (True):
                if len(monstruos) == 0:
                    break
                print("Elija el id del enemigo al que desea atacar:")
                for monstruo in monstruos:
                    print(" " + str(monstruo.id) + ": " + type(monstruo).__name__)
                entrada_usuario = input()
                for monstruo in monstruos:
                    if str(monstruo.id) == str(entrada_usuario):
                        jugador.atacar_fuerza(monstruo, random.randrange(1, self.arma))
                        self.accion_especial_1 = False
                        return
        else:
            print(
                "El jugador no puede realizar más acciones especiales, pase turno para realizar acciones especiales de nuevo")

    def pasar_turno(self):
        self.accion_especial_1 = True

    def action_segundo_viento(self, jugador: object, aliados: list, monstruos: list):
        if jugador.accion_bonus:
            recuperacion = jugador.vida + random.randrange(1, 10) + jugador.constitucion
            jugador.vida += recuperacion
            print ("Jugador recuperó " + str(recuperacion) + " puntos de vida")
            if jugador.vida > jugador.vidaMaxima:
                jugador.vida = jugador.vidaMaxima
            jugador.accion_bonus = False
        else:
            print("El jugador no puede realizar más acciones adicionales, pase turno para realizar acciones adicionales de nuevo")

    def subir_nivel(self, jugador: object):
        vidaAdicional = random.randrange(1, 10) + jugador.constitucion
        if vidaAdicional <= 0:
            vidaAdicional = 1
        self.vida += vidaAdicional
        self.nivel += 1
        print("El jugador sube un nivel en la clase guerrero y gana " + str(vidaAdicional) + " puntos de vida")
        setattr(self, "action_accion_adicional", self.accion_adicional)

class Clase_Monje(EntidadControlable.EntidadControlable):
    vida = ...  # type: int
    nivel = ...  # type: int
    arma = ...  # type: int
    accion_especial_1 = ...  # type: bool
    tipo_arma = ...  # type: str

    def __init__(self):
        self.vida = 8
        self.nivel = 1
        self.arma = 8
        self.tipo_arma = "destreza"

    def action_ataque_adicional(self, jugador: object, aliados: list, monstruos: list):
        if jugador.accion_bonus:
            while (True):
                if len(monstruos) == 0:
                    break
                print("Elija el id del enemigo al que desea atacar:")
                for monstruo in monstruos:
                    print(" " + str(monstruo.id) + ": " + type(monstruo).__name__)
                entrada_usuario = input()
                for monstruo in monstruos:
                    if str(monstruo.id) == str(entrada_usuario):
                        jugador.atacar_destreza(monstruo, random.randrange(1, 4))
                        jugador.accion_bonus = False
                        return
        else:
            print("El jugador no puede realizar más acciones adicionales, pase turno para realizar acciones adicionales de nuevo")

    def subir_nivel(self, jugador:object):
        vidaAdicional = random.randrange(1, 8) + jugador.constitucion
        if vidaAdicional <= 0:
            vidaAdicional = 1
        self.vida += vidaAdicional
        self.nivel += 1
        print("El jugador sube un nivel en la clase monje y gana " + str(vidaAdicional) + " puntos de vida")