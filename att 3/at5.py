maior = None
menor = None

while True:
    num = int(input("Digite um número: "))
    
    if num == 0:
        break
    if num < 0:
        continue
    
    if maior is None:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("Maior:", maior)
print("Menor:", menor)