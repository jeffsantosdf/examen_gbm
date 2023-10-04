
def boolean_palindromo(frase):
    frase = frase.upper().replace(" ", "")
    return frase == frase[::-1]