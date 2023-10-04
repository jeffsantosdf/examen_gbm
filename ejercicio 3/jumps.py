def minimum_jumps(input):
    y = contador = 0

    while y < input:
        contador += 1
        y += contador 

    if y == input:
        return contador
    else:
        if (y - input) % 2 == 0:
            return contador
        else:
            return contador + 1