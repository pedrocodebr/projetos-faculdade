maior = None
menor = None

while True:
    valor = input("Digite um número ou 'fim' para encerrar: ")

    if valor.lower() == "fim":
        break

    numero = float(valor)

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

if maior is None and menor is None:
    print("Nenhum número foi digitado.")
else:
    print("Maior valor digitado:", maior)
    print("Menor valor digitado:", menor)