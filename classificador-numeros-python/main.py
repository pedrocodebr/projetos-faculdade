pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))

    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

   
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Pares:", pares)
print("Ímpares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)