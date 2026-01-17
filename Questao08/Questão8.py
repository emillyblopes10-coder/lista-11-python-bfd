# Questão 8 - Aprovação de empréstimo bancário


#usando função

def calcular_prestacao(valor_casa, anos):
    meses = anos * 12
    prestacao = valor_casa / meses
    return prestacao


def verificar_emprestimo(prestacao, salario):
    limite = salario * 0.30

    if prestacao <= limite:
        return "Empréstimo Aprovado"
    else:
        return "Empréstimo Negado"


def main():
    print(" SIMULADOR DE EMPRÉSTIMO ")

    try:
        valor_casa = float(input("Digite o valor da casa (R$): "))
        salario = float(input("Digite o salário do comprador (R$): "))
        anos = int(input("Em quantos anos pretende pagar? "))
    except ValueError:
        print("Erro: digite valores numéricos válidos.")
        return

    if valor_casa <= 0 or salario <= 0 or anos <= 0:
        print("Erro: os valores devem ser maiores que zero.")
        return

    prestacao = calcular_prestacao(valor_casa, anos)
    resultado = verificar_emprestimo(prestacao, salario)

    print("\n RESULTADO ")
    print(f"Prestação mensal: R$ {prestacao:.2f}")
    print(f"Limite (30% do salário): R$ {salario * 0.30:.2f}")
    print(resultado)


if __name__ == "__main__":
    main()
