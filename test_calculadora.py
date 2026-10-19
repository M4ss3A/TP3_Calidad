import unittest

from calculadora import calcular_total, dividir, sumar


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_calcular_total(self):
        self.assertEqual(calcular_total(100, 2), 200)

    def test_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            calcular_total(100, -1)


if __name__ == "__main__":
    unittest.main()
