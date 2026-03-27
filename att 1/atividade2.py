

distancia = float(input("Digite a distância percorrida em km: "))
hora = int(input("Digite a hora da viagem (0 a 23): "))

if hora >= 22 or hora < 6:
    valor_por_km = 3.50
else:
    valor_por_km = 2.50

valor_total = distancia * valor_por_km

if distancia > 20:
    desconto = valor_total * 0.10
    valor_total -= desconto

print(f"Valor final da corrida: R$ {valor_total:.2f}")