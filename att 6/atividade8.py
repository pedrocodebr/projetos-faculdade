pedidos = [("hamburguer", 2, 18.0), ("suco", 0, 7.0), ("pizza", 1, 42.0), ("batata", 3, 12.0)]

total_dia = 0

for produto, qtd, preco in pedidos:
    if qtd == 0:
        continue
    
    subtotal = qtd * preco
    total_dia += subtotal
    
    print(f"{produto}: R$ {subtotal}")
    
    if subtotal > 30:
        print(f" -> {produto} teve subtotal alto")

print("Total do dia:", total_dia)