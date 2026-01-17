#Questão 1: Sistema de Notas do Aluno
#Usando função
def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media


def verificar_situacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    print(" SISTEMA DE NOTAS DO ALUNO ")

    nome = input("Digite o nome do aluno: ")

    try:
        n1 = float(input("Digite a 1ª nota: "))
        n2 = float(input("Digite a 2ª nota: "))
        n3 = float(input("Digite a 3ª nota: "))
        n4 = float(input("Digite a 4ª nota: "))
    except ValueError:
        print("Erro: digite apenas números nas notas.")
        return

    media = calcular_media(n1, n2, n3, n4)
    situacao = verificar_situacao(media)

    print("\n RESULTADO ")
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()
