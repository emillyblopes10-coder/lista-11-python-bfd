#Questão2: Verificador de Par ou Ímpar
#Usando função
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


def main():
    print(" VERIFICAR SE O NÚMERO É PAR OU ÍMPAR ")

    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: digite apenas número inteiro.")
        return

    resultado = verificar_par_ou_impar(numero)

    print(f"O número {numero} é {resultado}.")


if __name__ == "__main__":
    main()
