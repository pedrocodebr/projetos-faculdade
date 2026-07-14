def gerar_saudacao(nome, mensagem=None):
    if mensagem:
        return f"{mensagem}, {nome}!"
    return f"Bem-vindo, {nome}!"

clientes = ["Ana", "Bruno", "Carla"]

for cliente in clientes:
    print(gerar_saudacao(cliente))