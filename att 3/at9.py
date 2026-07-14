def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador = 0

while True:
    num = int(input("Digite um número: "))
    
    if num == 1:
        break
    
    if eh_primo(num):
        contador += 1

print("Quantidade de primos:", contador)