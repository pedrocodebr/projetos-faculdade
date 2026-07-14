def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

operacoes = [(10, 2), (20, 0), (30, 5)]

resultados = [dividir(a, b) for a, b in operacoes]
print(resultados)