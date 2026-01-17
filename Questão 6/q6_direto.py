# Questão 6 - Cálculo do IMC
# Forma direta
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
else:
    print("Sobrepeso")

