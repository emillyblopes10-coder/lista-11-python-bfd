# Questão 8 - Aprovação de empréstimo bancário
#Forma direta
valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Anos para pagar: "))

prestacao = valor_casa / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    print("Empréstimo Aprovado")
else:
    print("Empréstimo Negado")

