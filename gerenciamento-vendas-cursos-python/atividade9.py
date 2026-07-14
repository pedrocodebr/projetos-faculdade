acessos = ["ana", "bruno", "ana", "carla", "diego", "bruno", "ana"]

contagem = {}

for usuario in acessos:
    contagem[usuario] = contagem.get(usuario, 0) + 1

print(contagem)