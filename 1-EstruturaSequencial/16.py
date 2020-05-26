# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas 
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas 
# de tinta a serem compradas e o preço total.

# Variaveis
area = int(input("Area a ser pintada em metros²: "))
cobertura = 54
# Processamento
if (area % cobertura) != 0:
    latas = int(area / cobertura) + 1
preco = latas * 80
# Saida
print("Total de latas: ",latas)
print("Preço: R$ %.2f" %preco)