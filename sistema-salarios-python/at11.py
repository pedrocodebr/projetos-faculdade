soma = 0
qtd = 0

while True:
    salario = float(input("Digite o salário: "))
    
    if salario < 0:
        break
    if salario == 0:
        continue
    
    soma += salario
    qtd += 1

if qtd > 0:
    media = soma / qtd
    print("Média:", media)
else:
    print("Nenhum salário válido")