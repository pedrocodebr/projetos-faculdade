numeros = [10, 15, 20, 25, 30, 35]

pares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1

print("Quantidade de números pares:", pares)