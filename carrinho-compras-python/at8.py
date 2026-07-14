total = 0
qtd_descontos = 0

while True:
    valor = float(input("Digite o valor da compra: "))
    
    if valor == -1:
        break
    
    if valor > 100:
        desconto = valor * 0.10
        valor -= desconto
        qtd_descontos += 1
    
    total += valor

print("Total:", total)
print("Compras com desconto:", qtd_descontos)