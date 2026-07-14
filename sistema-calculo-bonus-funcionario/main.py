salario = float(input("Digite o salário do funcionário: R$ "))

avaliacao = input("Digite a avaliação do funcionário (excelente/boa/regular): ").strip().lower()

bonus = 0

if avaliacao == "excelente":
    bonus = salario * 0.20

elif avaliacao == "boa":
    if salario < 5000:
        bonus = salario * 0.10
    else:
        bonus = salario * 0.05

elif avaliacao == "regular":
    if salario < 3000:
        bonus = salario * 0.05
    else:
        bonus = 0

else:
    print("Avaliação inválida.")

print(f"Bônus do funcionário: R$ {bonus:.2f}")