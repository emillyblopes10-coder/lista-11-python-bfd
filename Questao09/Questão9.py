# Questão 9 - Categoria de atleta (natação)
#Usando função
from datetime import datetime


def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def definir_categoria(idade):
    if idade <= 9:
        return "MIRIM"
    elif idade <= 14:
        return "INFANTIL"
    elif idade <= 19:
        return "JÚNIOR"
    elif idade <= 25:
        return "SÊNIOR"
    else:
        return "MASTER"


def main():
    print("=== CATEGORIA DO ATLETA ===")

    try:
        ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
    except ValueError:
        print("Erro: digite um ano válido.")
        return

    ano_atual = datetime.now().year

    if ano_nascimento <= 0 or ano_nascimento > ano_atual:
        print("Erro: ano de nascimento inválido.")
        return

    idade = calcular_idade(ano_nascimento)
    categoria = definir_categoria(idade)

    print("\n--- RESULTADO ---")
    print(f"Ano atual: {ano_atual}")
    print(f"Idade: {idade} anos")
    print(f"Categoria: {categoria}")


if __name__ == "__main__":
    main()
