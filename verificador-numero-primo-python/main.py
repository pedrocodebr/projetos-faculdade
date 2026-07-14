numero = int(input("Digite um número: "))

if numero <= 1:
    print("Não é primo.")
else:
    i = 2
    primo = True

    while i < numero:
        if numero % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print("É primo.")
    else:
        print("Não é primo.")