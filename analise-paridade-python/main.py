pares = 0
impares = 0

while True:
    num = int(input("Digite um número: "))
    
    if num < 0:
        break
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)