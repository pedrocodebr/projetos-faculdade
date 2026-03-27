numeros = [3, 8, 5, 11, 14, 9, 21, 4, 13]

for numero in numeros:
    if numero % 2 == 0:
        continue

    if numero % 7 == 0:
        print("Número divisível por 7 encontrado:", numero)
        break

    print("Número processado:", numero)