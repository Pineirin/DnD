from Jugador import Jugador
import Clases
import Razas
import Monstruos


class Program:

    jugador1 = ...  # type: object
    monsterCounter = ...  # type: int
    monstruos = ...  # type: list

    def __init__(self):
        self.jugador1 = None
        self.monsterCounter = 0
        self.monstruos = []
        self.crearZombies(1)

    def start(self):
        print("Bienvenido al interprete interactivo de D&D")
        self.interprete()

    def interprete(self):
        while True:
            if self.jugador1 is not None:
                if self.jugador1.vida <= 0:
                    print("Jugador reducido a " + str(self.jugador1.vida) + " puntos de vida")
                    print("El jugador a muerto")
                    print("Cerrando el interprete")
                    break
                self.realizarComprobaciones()
                print("En estos momento se enfrenta a:")
                for monstruo in self.monstruos:
                    print(" " + str(monstruo.id) + ": " + type(monstruo).__name__ + " con " + str(monstruo.vida) + " puntos de vida")
                print("El jugador tiene " + str(self.jugador1.vida) + " puntos de vida")
            print("Introduzca un comando:")
            if self.jugador1 is None:
                print("- Crear personaje")
            else:
                for action in self.jugador1.actions():
                    print("- " + action)
                for action in self.jugador1.raza.actions():
                    print("- " + action)
                for action in self.jugador1.clase.actions():
                    print("- " + action)
                print("- Pasar turno")
            print("- Fin")
            entrada_usuario = input()
            if entrada_usuario == "Fin":
                print("Cerrando interprete")
                break
            elif entrada_usuario == "Crear personaje":
                self.jugador1 = self.crear_personaje()
            elif entrada_usuario == "Pasar turno":
                for monstruo in self.monstruos:
                    monstruo.atacar_fuerza(self.jugador1)
                    self.jugador1.pasar_turno()
            else:
                if self.jugador1 is not None:
                    self.ejecutar(entrada_usuario)

    def crear_personaje(self) -> object:
        while (True):
            print("Seleccione la raza")
            for raza in Razas.__dir__():
                if "Raza" in raza:
                    print("- " + raza.replace("Raza_", ""))
            try:
                entrada_usuario = input()
                raza = getattr(Razas, "Raza_" + entrada_usuario)()
                break
            except AttributeError:
                print("Por favor elija una raza válida")

        while (True):
            print("Seleccione la clase")
            for clase in Clases.__dir__():
                if "Clase" in clase:
                    print("- " + clase.replace("Clase_", ""))
            try:
                entrada_usuario = input()
                clase = getattr(Clases, "Clase_" + entrada_usuario)()
                break
            except AttributeError:
                print("Por favor elija una clase válida")
        return Jugador(raza, clase)

    def ejecutar(self, input: str):
        if input in self.jugador1.actions():
            self.jugador1.execute(input, self.jugador1, [], self.monstruos)
        elif input in self.jugador1.raza.actions():
            self.jugador1.raza.execute(input, self.jugador1, [], self.monstruos)
        elif input in self.jugador1.clase.actions():
            self.jugador1.clase.execute(input, self.jugador1, [], self.monstruos)

    def comprobarMonstruos(self):
        monstruosSupervivientes = []
        for monstruo in self.monstruos:
            if monstruo.vida > 0:
                monstruosSupervivientes.append(monstruo)
            else:
                print(type(monstruo).__name__ + " " + str(monstruo.id) + " ha sido derrotado")
                self.jugador1.xp += monstruo.xp
        self.monstruos = monstruosSupervivientes

    def crearZombies(self, n:int):
        for i in range(0, n):
            self.monsterCounter += 1
            self.monstruos.append(Monstruos.Zombie(self.monsterCounter))

    def realizarComprobaciones(self):
        self.comprobarMonstruos()
        if len(self.monstruos) == 0:
            self.crearZombies(2)
        if self.jugador1.xp >= 50 and self.jugador1.clase.nivel == 1:
            self.jugador1.subir_nivel()

if __name__ == "__main__":
    p = Program()
    p.start()
