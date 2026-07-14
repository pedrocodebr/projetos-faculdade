abaixo = normal = acima = 0

while True:
    peso = float(input("Peso: "))
    
    if peso < 0:
        break
    
    altura = float(input("Altura: "))
    
    if altura <= 0:
        continue
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        abaixo += 1
    elif imc < 25:
        normal += 1
    else:
        acima += 1

print("Abaixo:", abaixo)
print("Normal:", normal)
print("Acima:", acima)