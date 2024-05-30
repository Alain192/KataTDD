import unittest
from src.logica.Conjunto import Conjunto

class MyTestCase(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto ([])
        self.assertIsNone(conjunto.promedio())  # add assertion here


if __name__ == '__main__':
    unittest.main()
