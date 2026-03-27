temperatura = float(input("Digite a temperatura da cidade: "))

print(f"Temperatura informada: {temperatura:.1f}°C")

if temperatura > 40:
    print("Alerta especial: Emergência climática.")
elif temperatura > 35:
    print("Calor extremo.")
elif temperatura >= 26:
    print("Calor moderado.")
elif temperatura >= 10:
    print("Temperatura amena.")
else:
    print("Frio intenso.")