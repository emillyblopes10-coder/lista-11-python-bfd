# Questão 9 - Categoria de atleta (natação)
#Forma direta
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")

