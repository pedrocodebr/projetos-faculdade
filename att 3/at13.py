maior = None

while True:
    num = int(input("Digite um número: "))
    
    if num == 0:
        break
    
    if maior is None or num > maior:
        maior = num

print("Maior:", maior)