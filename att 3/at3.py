soma = 0
contador = 0
notas = []

while True:
    nota = float(input("Digite a nota (ou -1 para encerrar): "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida!")
        continue

  
    soma += nota
    contador += 1
    notas.append(nota)


if contador > 0:
    media = soma / contador

    acima = 0
    for n in notas:
        if n > media:
            acima += 1

    print(f"Média: {media:.2f}")
    print(f"Alunos acima da média: {acima}")
else:
    print("Nenhuma nota válida.")