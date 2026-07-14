notas = [8.5, 6.0, 7.2, 4.5, 9.0, 5.8, 7.0]

resultado = {
    "aprovados": [],
    "recuperacao": [],
    "reprovados": []
}

for nota in notas:
    if nota >= 7:
        resultado["aprovados"].append(nota)
    elif nota >= 5:
        resultado["recuperacao"].append(nota)
    else:
        resultado["reprovados"].append(nota)

for categoria, lista in resultado.items():
    print(categoria, ":", len(lista))