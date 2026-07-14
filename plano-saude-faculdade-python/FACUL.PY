def escolher_plano():
    while True:
        try:
            print("\n=== PLANOS DISPONÍVEIS ===")
            print("1 - Ouro: R$300,00")
            print("2 - Diamante: R$400,00")
            print("3 - Prata: R$200,00")
            print("4 - Esmeralda: R$500,00")

            opcao = int(input("Escolha o tipo do plano: "))

            if opcao == 1:
                return "Ouro", 300

            elif opcao == 2:
                return "Diamante", 400

            elif opcao == 3:
                return "Prata", 200

            elif opcao == 4:
                return "Esmeralda", 500

            else:
                print("Esse tipo de plano não existe. Tente novamente.")

        except ValueError:
            print("Digite um número equivalente aos planos.")


def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))

            if idade < 0:
                print("A idade não pode ser negativa.")
            else:
                return idade

        except ValueError:
            print("Digite apenas números para a idade.")


def ler_sexo():
    while True:
        sexo = input("Digite o sexo do cliente (M/F): ").upper()

        if sexo == "M" or sexo == "F":
            return sexo

        else:
            print("Sexo inválido. Digite apenas M ou F.")


def ler_dependentes():
    while True:
        try:
            dependentes = int(input("Digite a quantidade de dependentes: "))

            if dependentes < 0:
                print("A quantidade de dependentes não pode ser negativa.")
            else:
                return dependentes

        except ValueError:
            print("Digite apenas números para dependentes.")


def calcular_plano_saude():

    print("===== SISTEMA DE PLANO DE SAÚDE =====")

    plano, valor_base = escolher_plano()

    idade = ler_idade()

    sexo = ler_sexo()

    dependentes = ler_dependentes()

    valor_total = valor_base

    # Mulher entre 13 e 35 anos
    if sexo == "F" and idade >= 13 and idade < 35:
        valor_total += valor_base * 0.30

    # Mais de 1 dependente
    if dependentes > 1:
        valor_total -= valor_total * 0.20

    # Menor de 13 anos
    if idade < 13:
        valor_total -= valor_total * 0.30

    # Idoso
    if idade >= 60:
        valor_total += valor_base * 0.40

    print("\n===== RESULTADO =====")
    print(f"Plano escolhido: {plano}")
    print(f"Valor base do plano: R$ {valor_base:.2f}")
    print(f"Idade do cliente: {idade}")
    print(f"Sexo do cliente: {sexo}")
    print(f"Quantidade de dependentes: {dependentes}")
    print(f"Valor total do plano: R$ {valor_total:.2f}")

    return {
        "plano": plano,
        "valor_base": valor_base,
        "idade": idade,
        "sexo": sexo,
        "dependentes": dependentes,
        "valor_total": valor_total
    }