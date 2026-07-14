soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (negativo para parar): "))

    if numero < 0:
        break

    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"Média dos números positivos: {media}")
else:
    print("Nenhum número positivo foi digitado.")