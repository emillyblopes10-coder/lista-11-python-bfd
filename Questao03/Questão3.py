# Questão 3 - Controle de acesso por idade
#usando função

def verificar_acesso(idade):
    if idade >= 18:
        return "Acesso Liberado"
    else:
        return "Acesso Negado"


def main():
    print(" CONTROLE DE ACESSO ")

    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: digite uma idade válida (número inteiro).")
        return

    resultado = verificar_acesso(idade)

    print(resultado)


if __name__ == "__main__":
    main()
