def soma_positivos(valores):
    return sum(v for v in valores if v >= 0)

pedidos = [120, -30, 250, 400, -10, 90]

print(soma_positivos(pedidos))