# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. Considere que a cobertura da 
# tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
# preços em 3 situações:
#  a. comprar apenas latas de 18 litros;
#  b. comprar apenas galões de 3,6 litros;
#  c. misturar latas e galões, de forma que o preço seja o menor.
#  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

# Variaveis
area = int(input("Area a ser pintada em metros²: "))
cobertura1 = 108
cobertura2 = 21.6
latas = galao = 0
# Processamento
quant_latas = int(area / cobertura1)
so_latas = quant_latas
sobra_latas = int(area % cobertura1)
if (area % cobertura1) > 0:
    so_latas += 1
if sobra_latas >= 21:
    compl_galao = int(sobra_latas / cobertura2)
    
quant_galao = int(area / cobertura2)
so_galao = quant_galao
sobra_galao = int(area % cobertura2)
if (area % cobertura2) > 0:
    so_galao += 1
# Saida
print("Total de latas: %d  R$ %.2f" %(so_latas,(so_latas * 80)))
print("Total de galoes: %d  R$ %.2f" %(so_galao,(so_galao * 25)))
print("Melhor opção: %d latas e %d galao R$ %.2f" %(quant_latas,compl_galao,((quant_latas*80)+(compl_galao*25))))