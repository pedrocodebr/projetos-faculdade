voto1 = 0
voto2 = 0
voto3 = 0

while True:
    voto = int(input("Vote (1, 2, 3 ou 0 para sair): "))

    if voto == 0:
        break

    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    else:
        print("Voto inválido!")

print("Candidato 1:", voto1)
print("Candidato 2:", voto2)
print("Candidato 3:", voto3)


if voto1 > voto2 and voto1 > voto3:
    print("Candidato 1 venceu!")
elif voto2 > voto1 and voto2 > voto3:
    print("Candidato 2 venceu!")
elif voto3 > voto1 and voto3 > voto2:
    print("Candidato 3 venceu!")
else:
    print("Empate!")