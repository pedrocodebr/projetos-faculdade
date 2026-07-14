cand1 = cand2 = nulos = 0

while True:
    voto = int(input("Digite seu voto: "))
    
    if voto == 0:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        nulos += 1

if cand1 > cand2:
    print("Candidato 1 venceu")
elif cand2 > cand1:
    print("Candidato 2 venceu")
else:
    print("Empate")