
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media_inicial = (nota1 + nota2) / 2

if media_inicial >= 7:
    print(f"Média inicial: {media_inicial:.2f}")
    print("Situação: Aprovado diretamente.")
elif media_inicial < 4:
    print(f"Média inicial: {media_inicial:.2f}")
    print("Situação: Reprovado.")
else:
    print(f"Média inicial: {media_inicial:.2f}")
    print("Situação: Recuperação.")
    
    recuperacao = float(input("Digite a nota da recuperação: "))
    media_final = (media_inicial + recuperacao) / 2

    print(f"Média final: {media_final:.2f}")

    if media_final >= 6:
        print("Situação final: Aprovado após recuperação.")
    else:
        print("Situação final: Reprovado após recuperação.")