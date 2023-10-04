import unittest
import os
import jumps

class UnitTests(unittest.TestCase):

    def test_case_2(self):
        resultado = jumps.minimum_jumps(10)
        self.assertEqual(resultado, 4)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output2.txt', 'w') as output:
            output.write(f"Resultado de la prueba si X es 10: {resultado}\n")    

if __name__ == '__main__':
    unittest.main()
