senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print("Senha incorreta!")

if tentativas == 3:
    print("Conta bloqueada!")