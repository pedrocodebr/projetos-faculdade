soma = 0

while True:
    num = int(input("Digite um número: "))
    
    if num == 0:
        break
    
    if num % 3 != 0:
        continue
    
    soma += num

print("Soma:", soma)