# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores
# para cima, isto é, considere latas cheias.

# Entrada
area = float(input("Digite a área a ser pintada: "))
contLata = 0
contGalao = 0
sobra = 0
quant = 0
lata = float(18.0 * 6)
galao = float(3.6 * 6)

# Execuçao
quant = area
while quant > lata:
	contLata += 1
	quant -= lata
while quant > galao:
	sobra += 1
	quant -= galao

while area > galao:
	contGalao += 1
	area -= galao

# Saida
print("Comprar apenas latas de 18 litros:")
print("Total de latas: %.f" %(contLata + 1))
print("Valor apenas latas: R$%.2f \n" %((contLata + 1)* 80))

print("Comprar apenas galoes de 3,6 litros")
print("Total de galoes: %.f" %(contGalao + 1))
print("Valor apenas galão: R$%.2f \n" %((contGalao + 1) * 25))

print("Comprando latas e galões:")
print("Total de latas: %.f e galões: %.f" %(contLata,sobra))
print("Valor de latas e galões: R$%.2f" %((contLata * 80)+((sobra + 1) * 25)))