

idade = int(input("Digite a idade do usuário: "))
matriculado = input("O usuário está matriculado? (sim/nao): ").strip().lower()

if matriculado != "sim":
    print("Acesso negado.")
else:
    if idade >= 18:
        print("Acesso permitido.")
    else:
        autorizacao = input("Possui autorização especial? (sim/nao): ").strip().lower()

        if autorizacao == "sim":
            print("Acesso permitido.")
        else:
            print("Acesso negado.")