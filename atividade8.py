renda_familiar = float(input("Digite a renda familiar mensal: R$ "))
media = float(input("Digite a média das notas do aluno: "))

if media >= 9 and renda_familiar <= 5000:
    print("O aluno é elegível para a bolsa de estudos.")

elif media >= 8 and renda_familiar < 3000:
    print("O aluno é elegível para a bolsa de estudos.")

elif 7 <= media < 7.9 and renda_familiar < 2000:
    print("O aluno é elegível para a bolsa de estudos.")

else:
    print("O aluno não é elegível para a bolsa de estudos.")