import unittest
import read_palindromo
import os
class UnitTests(unittest.TestCase):

    def test_palindromo_mayusculas(self):
        resultado = read_palindromo.boolean_palindromo("SEDES")
        self.assertTrue(resultado)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output2.txt', 'w') as output:
            output.write(f"Resultado de la prueba test_palindromo_minusculas: {resultado}\n")
            
if __name__ == '__main__':
    unittest.main()