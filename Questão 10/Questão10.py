# Questão 10 - Loja de Tintas
#usando função
import math


def calcular_litros(area):
    return area / 3


def calcular_latas(litros):
    return math.ceil(litros / 18)


def calcular_preco_total(latas):
    preco_lata = 80.0
    return latas * preco_lata


def main():
    print(" LOJA DE TINTAS ")

    try:
        area = float(input("Digite a área a ser pintada (m²): "))
    except ValueError:
        print("Erro: digite um valor numérico válido.")
        return

    if area <= 0:
        print("Erro: a área deve ser maior que zero.")
        return

    litros = calcular_litros(area)
    latas = calcular_latas(litros)
    total = calcular_preco_total(latas)

    print("\n RESULTADO ")
    print(f"Área: {area:.2f} m²")
    print(f"Litros necessários: {litros:.2f} L")
    print(f"Latas a comprar: {latas}")
    print(f"Preço total: R$ {total:.2f}")


if __name__ == "__main__":
    main()
