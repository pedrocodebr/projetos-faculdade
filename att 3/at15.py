valores = []

while True:
    tarefas = int(input("Tarefas: "))
    
    if tarefas < 0:
        break
    if tarefas == 0:
        continue
    
    valores.append(tarefas)

if len(valores) > 0:
    media = sum(valores) / len(valores)
    acima = sum(1 for v in valores if v > media)
    
    print("Média:", media)
    print("Acima da média:", acima)
else:
    print("Nenhum valor válido")