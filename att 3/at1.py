soma = 0
contador = 0

while True:
    idade = int(input("Digite a idade (ou 0 para encerrar): "))

    if idade == 0:
        break

    if idade < 10 or idade > 100:
        print("Idade inválida! Digite uma idade entre 10 e 100.")
        continue
    else:
        print("Idade válida! Idade registrada.")
        soma += idade
        contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhuma idade válida foi digitada.")