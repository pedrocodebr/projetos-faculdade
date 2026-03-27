
valor_compra = float(input("Digite o valor da compra: R$ "))
categoria = input("Digite a categoria do cliente (premium/comum): ").strip().lower()

desconto = 0

if categoria == "premium":
    if valor_compra > 500:
        desconto = 0.20
    else:
        desconto = 0.10
elif categoria == "comum":
    if valor_compra > 500:
        desconto = 0.10

valor_final = valor_compra - (valor_compra * desconto)

print(f"Valor final da compra: R$ {valor_final:.2f}")