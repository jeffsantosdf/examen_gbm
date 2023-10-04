import read_palindromo
from unittest import main

#Haciendo pruebas a la funcion.
frase = "A luna ese anula" 
print(read_palindromo.boolean_palindromo(frase))
frase = "nada de nada" 
print(read_palindromo.boolean_palindromo(frase))

#Correr pruebas unitarias automaticamente.
main(module='test_module', exit=False)
main(module='test_module2', exit=False)
main(module='test_module3', exit=False)
main(module='test_module4', exit=False)

