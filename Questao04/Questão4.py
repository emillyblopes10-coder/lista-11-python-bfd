# Questão 4 - Verificar se três valores formam um triângulo
#usando função
def verificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


def main():
    print(" VERIFICAÇÃO DE TRIÂNGULO ")

    try:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
    except ValueError:
        print("Erro: digite apenas números.")
        return

    if verificar_triangulo(a, b, c):
        print("Os valores informados FORMAM um triângulo.")
    else:
        print("Os valores informados NÃO formam um triângulo.")


if __name__ == "__main__":
    main()
