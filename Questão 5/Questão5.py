# Questão 5 - Cálculo de reajuste salarial
#usando função

def calcular_reajuste(salario):
    if salario <= 1500:
        novo_salario = salario * 1.15   # aumento de 15%
    else:
        novo_salario = salario * 1.10   # aumento de 10%

    return novo_salario


def main():
    print(" REAJUSTE SALARIAL ")

    try:
        salario = float(input("Digite o salário do funcionário: R$ "))
    except ValueError:
        print("Erro: digite um valor numérico válido.")
        return

    if salario <= 0:
        print("Erro: salário deve ser maior que zero.")
        return

    novo_salario = calcular_reajuste(salario)

    print("\n RESULTADO ")
    print(f"Salário antigo: R$ {salario:.2f}")
    print(f"Novo salário:    R$ {novo_salario:.2f}")


if __name__ == "__main__":
    main()
