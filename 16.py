# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Entrada
area = float(input("Digite o tamanho da área em m²: "))
lata = 18 * 3
cont = 0
quant = area

# Execuçao
if area > lata:
    cont = 1
    while quant >= lata:
        cont += 1
        quant = quant - lata

else:
    cont += 1
preco = cont * 80

# Saida
print("A quantidade de latas necessarias é: %.f" %cont)
print("O valor a pagar é: R$%.2f" %preco)