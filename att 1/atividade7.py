idade = int(input("Digite a idade do usuário: "))
sintomas = input("Qual a gravidade dos sintomas? (leve/moderada/grave): ").strip().lower()

if sintomas == "grave":
    print("O paciente deve ser atendido imediatamente.")

elif sintomas == "moderada":
    if idade > 60:
        print("O paciente tem prioridade.")
    else:
        print("O paciente deve aguardar atendimento normal.")

elif sintomas == "leve":
    if idade < 12 or idade > 65:
        print("O paciente deve receber prioridade moderada.")
    else:
        print("O paciente deve aguardar atendimento comum.")

else:
    print("Entrada inválida.")