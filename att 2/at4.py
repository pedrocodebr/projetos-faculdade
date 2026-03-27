limite = int(input("Digite o limite: "))

a = 0
b = 1

while a <= limite:
    print(a, end=" ")

    proximo = a + b
    a = b
    b = proximo