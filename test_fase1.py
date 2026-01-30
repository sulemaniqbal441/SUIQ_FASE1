import unittest
from future_motors import Vehicle

class TestFase1(unittest.TestCase):
    def test_privacitat(self):
        v = Vehicle("1234-ABC", "Tesla", 1000)
        self.assertFalse(hasattr(v, "__kms"), "Els Kms han de ser privats (__)")
        self.assertFalse(hasattr(v, "kms"), "No facis la variable pública!")

    def test_anti_frau(self):
        v = Vehicle("9999-ZZZ", "Ford", 5000)
        resultat = v.actualitzar_kms(4000)  # Intentem baixar kms
        self.assertFalse(resultat, "Hauria de donar False si intentem baixar Kms")
        self.assertEqual(v.llegir_kms(), 5000, "Els km no haurien d'haver canviat")

    def test_actualitzacio_correcta(self):
        v = Vehicle("1111-AAA", "Seat", 100)
        v.actualitzar_kms(200)
        self.assertEqual(v.llegir_kms(), 200)

if __name__ == '__main__':
    unittest.main()

