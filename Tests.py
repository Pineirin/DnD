import unittest
from Jugador import Jugador
import Clases
import Razas
import Monstruos

class TestUM(unittest.TestCase):

    def setUp(self):
        print("Starting test")

    def tearDown(self):
        print("Finishing test")

    def test_Jugador(self):
        jugador = Jugador(Razas.Raza_Humano(), Clases.Clase_Guerrero())
        self.assertTrue(hasattr(jugador, "raza"))
        self.assertTrue(hasattr(jugador, "clase"))
        self.assertTrue(hasattr(jugador, "accion"))
        self.assertTrue(hasattr(jugador, "accion_bonus"))
        self.assertTrue(hasattr(jugador, "fuerza"))
        self.assertTrue(hasattr(jugador, "destreza"))
        self.assertTrue(hasattr(jugador, "constitucion"))
        self.assertTrue(hasattr(jugador, "inteligencia"))
        self.assertTrue(hasattr(jugador, "sabiduria"))
        self.assertTrue(hasattr(jugador, "carisma"))
        self.assertTrue(hasattr(jugador, "armadura"))
        self.assertTrue(hasattr(jugador, "vidaMaxima"))
        self.assertTrue(hasattr(jugador, "vida"))
        self.assertTrue(hasattr(jugador, "xp"))
        self.assertTrue(hasattr(jugador, "arma"))
        self.assertTrue(hasattr(jugador, "pasar_turno"))
        self.assertTrue(hasattr(jugador, "subir_nivel"))
        self.assertTrue(hasattr(jugador, "action_atacar"))
        self.assertTrue(jugador.accion)
        self.assertTrue(jugador.accion_bonus)
        self.assertEqual(jugador.armadura, 10 + jugador.destreza)
        self.assertEqual(jugador.vidaMaxima, jugador.clase.vida)
        self.assertEqual(jugador.vida, jugador.vidaMaxima)
        self.assertEqual(jugador.xp, 0)
        jugador.subir_nivel()
        self.assertEqual(jugador.vidaMaxima, jugador.clase.vida)
        self.assertEqual(jugador.vida, jugador.vidaMaxima)

    def test_Humano(self):
        jugador = Jugador(Razas.Raza_Humano(), Clases.Clase_Guerrero())
        self.assertTrue(hasattr(jugador.raza, "fuerza"))
        self.assertTrue(hasattr(jugador.raza, "destreza"))
        self.assertTrue(hasattr(jugador.raza, "constitucion"))
        self.assertTrue(hasattr(jugador.raza, "inteligencia"))
        self.assertTrue(hasattr(jugador.raza, "sabiduria"))
        self.assertTrue(hasattr(jugador.raza, "carisma"))
        self.assertEqual(jugador.raza.fuerza, 1)
        self.assertEqual(jugador.raza.destreza, 1)
        self.assertEqual(jugador.raza.constitucion, 1)
        self.assertEqual(jugador.raza.inteligencia, 1)
        self.assertEqual(jugador.raza.sabiduria, 1)
        self.assertEqual(jugador.raza.carisma, 1)

    def test_Enano_Colinas(self):
        jugador = Jugador(Razas.Raza_Enano_Colinas(), Clases.Clase_Guerrero())
        self.assertTrue(hasattr(jugador.raza, "fuerza"))
        self.assertTrue(hasattr(jugador.raza, "destreza"))
        self.assertTrue(hasattr(jugador.raza, "constitucion"))
        self.assertTrue(hasattr(jugador.raza, "inteligencia"))
        self.assertTrue(hasattr(jugador.raza, "sabiduria"))
        self.assertTrue(hasattr(jugador.raza, "carisma"))
        self.assertEqual(jugador.raza.fuerza, 0)
        self.assertEqual(jugador.raza.destreza, 0)
        self.assertEqual(jugador.raza.constitucion, 4)
        self.assertEqual(jugador.raza.inteligencia, 0)
        self.assertEqual(jugador.raza.sabiduria, 1)
        self.assertEqual(jugador.raza.carisma, 0)

    def test_Guerrero(self):
        jugador = Jugador(Razas.Raza_Humano(), Clases.Clase_Guerrero())
        self.assertTrue(hasattr(jugador.clase, "vida"))
        self.assertTrue(hasattr(jugador.clase, "nivel"))
        self.assertTrue(hasattr(jugador.clase, "arma"))
        self.assertTrue(hasattr(jugador.clase, "tipo_arma"))
        self.assertTrue(hasattr(jugador.clase, "pasar_turno"))
        self.assertTrue(hasattr(jugador.clase, "action_segundo_viento"))
        self.assertTrue(hasattr(jugador.clase, "subir_nivel"))
        self.assertFalse(hasattr(jugador.clase, "action_accion_adicional"))
        self.assertEqual(jugador.clase.vida, 10)
        self.assertEqual(jugador.clase.nivel, 1)
        self.assertEqual(jugador.clase.arma, 12)
        self.assertEqual(jugador.clase.tipo_arma, "fuerza")
        jugador.subir_nivel()
        self.assertEqual(jugador.clase.nivel, 2)
        self.assertTrue(hasattr(jugador.clase, "action_accion_adicional"))
        self.assertTrue(jugador.clase.vida > 10)

    def test_Monje(self):
        jugador = Jugador(Razas.Raza_Humano(), Clases.Clase_Monje())
        self.assertTrue(hasattr(jugador.clase, "vida"))
        self.assertTrue(hasattr(jugador.clase, "nivel"))
        self.assertTrue(hasattr(jugador.clase, "arma"))
        self.assertTrue(hasattr(jugador.clase, "tipo_arma"))
        self.assertTrue(hasattr(jugador.clase, "pasar_turno"))
        self.assertTrue(hasattr(jugador.clase, "action_ataque_adicional"))
        self.assertTrue(hasattr(jugador.clase, "subir_nivel"))
        self.assertEqual(jugador.clase.vida, 8)
        self.assertEqual(jugador.clase.nivel, 1)
        self.assertEqual(jugador.clase.arma, 8)
        self.assertEqual(jugador.clase.tipo_arma, "destreza")
        jugador.subir_nivel()
        self.assertEqual(jugador.clase.nivel, 2)
        self.assertTrue(jugador.clase.vida > 8)

