import os
import jumps
from unittest import main

# Abrir el archivo de entrada para lectura
dir= os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(dir + "/input.txt", "r") as input:
    numero = int(input.readline().strip())

    with open(dir + "/output.txt", "w") as output:
        contador = 0
        while contador < numero:
            x = int(input.readline().strip())
            min = jumps.minimum_jumps(x)
            output.write(str(min) + "\n")
            contador += 1

print("Las salidas se han guardado en el archivo 'output.txt'.")

main(module='test_module', exit=False)
main(module='test_module2', exit=False)
main(module='test_module3', exit=False)