notas = [7.5, 8.0, 6.5, 9.0, 5.5]

soma = 0
aprovados = 0

for nota in notas:
    soma += nota
    if nota >= 7:
        aprovados += 1

media = soma / len(notas)

print("Média:", media)
print("Aprovados:", aprovados)