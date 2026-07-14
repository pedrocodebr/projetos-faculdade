estoque = {"teclado": [10, 50.0], "mouse": [0, 25.0], "monitor": [5, 800.0], "cadeira": [2, 1200.0]}

total_geral = 0

for produto, dados in estoque.items():
    quantidade, preco = dados
    
    if quantidade == 0:
        continue
    
    total = quantidade * preco
    total_geral += total
    
    print(f"{produto}: R$ {total}")
    
    if total > 2000:
        print(f" -> {produto} tem valor alto em estoque!")

print("Total geral:", total_geral)