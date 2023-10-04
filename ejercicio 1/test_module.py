import unittest
import read_palindromo
import os
class UnitTests(unittest.TestCase):
    
    def test_palindromo_minusculas(self):
        resultado = read_palindromo.boolean_palindromo("llorar")
        self.assertFalse(resultado)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output1.txt', 'w') as output:
            output.write(f"Resultado de la prueba test_palindromo_minusculas: {resultado}\n")

if __name__ == '__main__':
    unittest.main()