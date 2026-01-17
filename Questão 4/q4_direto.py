# Questão 4 - Verificar se três valores formam um triângulo
#Forma direta
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")

