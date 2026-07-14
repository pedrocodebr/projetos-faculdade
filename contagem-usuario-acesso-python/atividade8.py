acessos = ["ana", "bruno", "ana", "carla", "ana", "bruno"]

contagem = {}

for usuario in acessos:
    if usuario in contagem:
        contagem[usuario] += 1
    else:
        contagem[usuario] = 1

print(contagem)