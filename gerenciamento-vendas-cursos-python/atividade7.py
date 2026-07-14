sensores = [[12, 7, 5], [20, 15, 8], [3, 18, 25]]

contador_maior_10 = 0

for i in range(len(sensores)):
    for j in range(len(sensores[i])):
        if (i + j) % 2 == 0:
            valor = sensores[i][j]
            print(valor)
            
            if valor > 10:
                contador_maior_10 += 1

print("Sensores > 10:", contador_maior_10)