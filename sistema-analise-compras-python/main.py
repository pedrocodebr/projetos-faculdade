valores = []

while True:
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra < 0:
        break

    if valor_compra == 0:
        continue

    valores.append(valor_compra)

if len(valores) > 0:
    media = sum(valores) / len(valores)

    acima = 0
    for v in valores:
        if v > media:
            acima += 1

    print(f"Média: {media:.2f}")
    print(f"Compras acima da média: {acima}")
else:
    print("Nenhuma compra válida.")