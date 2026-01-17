# Questão 10 - Loja de Tintas
#Forma direta
area = float(input("Área em m²: "))

litros = area / 3
latas = litros / 18

latas_inteiras = int(latas)

if latas > latas_inteiras:
    latas_final = latas_inteiras + 1
else:
    latas_final = latas_inteiras

preco = latas_final * 80

print("Latas necessárias:", latas_final)
print("Preço total: R$", preco)
