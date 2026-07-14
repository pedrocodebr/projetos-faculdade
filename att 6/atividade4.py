palavra = "programacao"

contagem = {}

for letra in palavra:
    contagem[letra] = contagem.get(letra, 0) + 1

unicas = []
repetidas = []

for letra, qtd in contagem.items():
    if qtd == 1:
        unicas.append(letra)
    else:
        repetidas.append(letra)

print("Letras únicas:", unicas)
print("Letras repetidas:", repetidas)