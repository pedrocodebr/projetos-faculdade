nome = input("Digite o nome do aluno: ")
while not nome.strip():
    nome = input("Nome não pode estar vazio. Digite novamente: ")

matriculado = input("O aluno está matriculado? (s/n): ").lower()

if matriculado not in ["s", "sim"]:
    print("Aluno não matriculado. Encerrando o programa.")
else:
    notas = []

    for i in range(1, 4):
        while True:
            nota = float(input(f"Digite a {i}ª nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite uma nota entre 0 e 10.")

    media = sum(notas) / len(notas)

    print("\n----- RESULTADO FINAL -----")
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média final: {round(media, 2)}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5 and media < 7:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")