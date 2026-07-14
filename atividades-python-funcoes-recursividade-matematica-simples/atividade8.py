produtos = [(1, "Teclado"), (3, "Mouse"), (2, "Monitor")]

ordenados = sorted(produtos, key=lambda x: x[1])
print(ordenados)