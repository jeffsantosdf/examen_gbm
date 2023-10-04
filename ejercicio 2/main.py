import os
import champions

dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(dir + '/input.txt', "r") as input, open(dir + "/output.txt", "w") as output:
    while True:
        prix, pilotos = map(int, input.readline().split())
        if prix == 0 and pilotos == 0:
            break
        
        tabla_resultados = []
        contador = 0
        while contador < prix:
            tabla_resultados.append(list(map(int, input.readline().split())))
            contador += 1

        carrera = int(input.readline())
        campeones = []
        contador = 0

        while contador < carrera:
            sistema_puntuacion = list(map(int, input.readline().split()))
            campeones_sistema = champions.world_champions(pilotos, tabla_resultados, sistema_puntuacion)
            resultado = " ".join(map(str, campeones_sistema))
            output.write(resultado + "\n")
            contador += 1