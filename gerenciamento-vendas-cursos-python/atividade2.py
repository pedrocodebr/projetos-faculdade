participantes = [("Ana", 22, True), ("Bruno", 17, True), ("Carla", 30, False), ("Diego", 19, True)]

for nome, idade, confirmado in participantes:
    if idade >= 18 and confirmado:
        print(nome)