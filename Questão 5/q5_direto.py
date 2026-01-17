# Questão 5 - Cálculo de reajuste salarial
#Forma direta
salario = float(input("Salário: R$ "))

if salario <= 1500:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10

print("Novo salário: R$", novo_salario)
