import unittest
import os
import jumps

class UnitTests(unittest.TestCase):

    def test_case_1(self):
        resultado = jumps.minimum_jumps(11)
        self.assertEqual(resultado, 5)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output1.txt', 'w') as output:
            output.write(f"Resultado de la prueba si X es 11: {resultado}\n")    

if __name__ == '__main__':
    unittest.main()
