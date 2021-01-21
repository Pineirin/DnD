import random

import  EntidadControlable


class Jugador(EntidadControlable.EntidadControlable):

    raza = ...  # type: object
    clase = ...  # type: object
    fuerza = ...  # type: int
    destreza = ...  # type: int
    constitucion = ...  # type: int
    inteligencia = ...  # type: int
    sabiduria = ...  # type: int
    carisma = ...  # type: int
    accion_bonus = ...  # type: bool
    accion = ...  # type: bool
    armadura = ...  # type: int
    vidaMaxima = ...  # type: int
    vida = ...  # type: int
    xp = ...  # type: int

    def __init__(self, raza: object, clase: object):
        print ("Ha creado un " + type(raza).__name__.replace("Raza_", "") + " " + type(clase).__name__.replace("Clase_", ""))
        self.raza = raza
        self.clase = clase
        self.accion = True
        self.accion_bonus = True
        self.fuerza = int((random.randrange(15) + 3 + raza.fuerza)/2)-5
        print("Puntuación de fuerza: " + str(self.fuerza))
        self.destreza = int((random.randrange(15) + 3 + raza.destreza)/2)-5
        print("Puntuación de destreza: " + str(self.destreza))
        self.constitucion = int((random.randrange(15) + 3 + raza.constitucion)/2)-5
        print("Puntuación de constitución: " + str(self.constitucion))
        self.inteligencia = int((random.randrange(15) + 3 + raza.inteligencia)/2)-5
        print("Puntuación de inteligencia: " + str(self.inteligencia))
        self.sabiduria = int((random.randrange(15) + 3 + raza.sabiduria)/2)-5
        print("Puntuación de sabiduría: " + str(self.sabiduria))
        self.carisma = int((random.randrange(15) + 3 + raza.carisma)/2)-5
        print("Puntuación de carisma: " + str(self.carisma))
        self.armadura = 10 + self.destreza
        self.vidaMaxima = self.clase.vida
        self.vida = self.vidaMaxima
        self.xp = 0

    def arma(self) -> int:
        return random.randrange(1, self.clase.arma)

    def pasar_turno(self):
        self.accion = True
        self.accion_bonus = True
        self.clase.pasar_turno()
        self.raza.pasar_turno()

    def subir_nivel(self):
        self.clase.subir_nivel(self)
        self.vidaMaxima = self.clase.vida
        self.vida = self.vidaMaxima

    def action_atacar(self, jugador: object, aliados: list, monstruos: list):
        if jugador.accion:
            while(True):
                if len(monstruos) == 0 :
                    break
                print("Elija el id del enemigo al que desea atacar:")
                for monstruo in monstruos:
                    print(" " + str(monstruo.id) + ": " + type(monstruo).__name__)
                entrada_usuario = input()
                for monstruo in monstruos:
                    if str(monstruo.id) == str(entrada_usuario):
                        if self.clase.tipo_arma == "fuerza":
                            self.atacar_fuerza(monstruo, self.arma())
                            jugador.accion = False
                        if self.clase.tipo_arma == "destreza":
                            self.atacar_destreza(monstruo, self.arma())
                            jugador.accion = False
                        return
        else:
            print("El jugador no puede realizar más acciones este turno, pase turno para realizar acciones de nuevo")