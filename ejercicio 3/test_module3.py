import unittest
import os
import jumps

class UnitTests(unittest.TestCase):

    def test_case_3(self):
        resultado = jumps.minimum_jumps(9)
        self.assertNotEqual(resultado, 4)
        dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(dir + '/output3.txt', 'w') as output:
            output.write(f"Resultado verdadero de la prueba si X es 9 (En la prueba tenemos NOt Equal = 4): {resultado}\n")
    
if __name__ == '__main__':
    unittest.main()
