import unittest
import read_palindromo
import os

class UnitTests(unittest.TestCase):
    
    def test_palindromo_frase_negativo(self):
        resultado = read_palindromo.boolean_palindromo("casa de locos")
        self.assertFalse(resultado)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output4.txt', 'w') as output:
            output.write(f"Resultado de la prueba test_palindromo_minusculas: {resultado}\n")

if __name__ == '__main__':
    unittest.main()