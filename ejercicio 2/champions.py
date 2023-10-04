def world_champions(pilotos, tabla_resultados, sistema_puntuacion):
    puntaje = [0] * pilotos
    for prix in tabla_resultados:
        for i, posicion in enumerate(prix[:]):
            if posicion <= sistema_puntuacion[0]:
                puntaje[i] += sistema_puntuacion[posicion]
    lideres = max(puntaje)
    campeones = []
    for i, puntos_piloto in enumerate(puntaje):
        if puntos_piloto == lideres:
            campeones.append(i + 1)
            
    return campeones