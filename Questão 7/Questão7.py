# Questão 7 - Verificar se o ano é bissexto
#usando função

def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


def main():
    print(" VERIFICAÇÃO DE ANO BISSEXTO ")

    try:
        ano = int(input("Digite um ano: "))
    except ValueError:
        print("Erro: digite um ano válido (número inteiro).")
        return

    if ano <= 0:
        print("Erro: o ano deve ser maior que zero.")
        return

    if verificar_bissexto(ano):
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")


if __name__ == "__main__":
    main()
