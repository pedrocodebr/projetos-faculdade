saldo = 1000.0
opcao = 0

while opcao != 4:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: R$ "))

        if valor_saque <= 0:
            print("Valor inválido.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso. Novo saldo: R$ {saldo:.2f}")

    elif opcao == 3:
        valor_deposito = float(input("Digite o valor do depósito: R$ "))

        if valor_deposito <= 0:
            print("Valor inválido.")
        else:
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso. Novo saldo: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Encerrando o sistema...")

    else:
        print("Opção inválida. Tente novamente.")