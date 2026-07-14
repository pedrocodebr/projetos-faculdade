 vendas = [120, 250, 80, 500, 210, 450, 30, 1000, 90]

soma = 0
contador = 0
maiores_300 = 0

for venda in vendas:
    if venda > 900:
        print("Venda suspeita encontrada! Encerrando análise.")
        break
    
    if venda < 100:
        continue
    
    soma += venda
    contador += 1
    
    if venda > 300:
        maiores_300 += 1

if contador > 0:
    media = soma / contador
    print("Média:", media)
    print("Vendas maiores que 300:", maiores_300)