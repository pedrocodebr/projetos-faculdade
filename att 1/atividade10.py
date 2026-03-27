peso = float(input("Digite o peso da encomenda em kg: "))
distancia = float(input("Digite a distância em km: "))

if peso > 50:
    print("A encomenda não pode ser transportada.")
else:
    if peso <= 5:
        custo = 10
    elif peso <= 20:
        custo = 20
    else:
        custo = 40

    if distancia > 50:
        custo += 15

    print(f"Custo final da entrega: R$ {custo:.2f}")