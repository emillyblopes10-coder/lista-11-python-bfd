# Questão 6 - Cálculo do IMC


#usando função
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"


def main():
    print(" CÁLCULO DO IMC ")

    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
    except ValueError:
        print("Erro: digite apenas números.")
        return

    if peso <= 0 or altura <= 0:
        print("Erro: peso e altura devem ser maiores que zero.")
        return

    imc = calcular_imc(peso, altura)
    categoria = classificar_imc(imc)

    print("\n RESULTADO ")
    print(f"IMC: {imc:.2f}")
    print(f"Categoria: {categoria}")


if __name__ == "__main__":
    main()
