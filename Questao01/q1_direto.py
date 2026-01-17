#Questão 1: Sistema de Notas do Aluno
#Forma direta
nome = input("Nome do aluno: ")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
