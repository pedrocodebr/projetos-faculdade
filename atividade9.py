saldo = float(input("Digite o saldo da conta: R$ "))
saque = float(input("Digite o valor do saque: R$ "))

if saque > saldo:
    print("Saldo insuficiente para realizar o saque.")

elif saque <= 0:
    print("Valor de saque inválido.")

elif saque > 1000:
    print("Valor de saque excede o limite permitido, solicite uma confirmação adicional.")
    
    confirmacao_adicional = input("Possui confirmação adicional? (sim/nao): ").strip().lower()

    if confirmacao_adicional == "sim":
        print("Saque autorizado com confirmação adicional.")
    else:
        print("Saque não autorizado sem confirmação adicional.")

else:
    print("Saque realizado com sucesso.")