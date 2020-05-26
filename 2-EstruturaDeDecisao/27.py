# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#  Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
# quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#VARIAVEIS
morango = int(input("Digite a quantidade de kilos de morango: "))
maca = int(input("Digite a quantidade de kilos de maça: "))
valor1 = valor2 = desconto = total = 0
#PROCESSAMENTO
if morango <= 5:
    valor1 = morango * 2.5
elif morango <= 8:
    valor1 = morango * 2.2
else:
    valor1 = (morango * 2.2) - ((morango * 2.2) * 0.1)

if maca <= 5:
    valor2 = maca * 1.8
elif maca <= 8:
    valor2 = maca * 1.5
else:
    valor2 = (morango * 1.5) - ((maca * 1.5) * 0.1)

if (morango <= 8 and maca <= 8) and (valor1 + valor2 > 25):
    desconto = (valor1 + valor2) * 0.1
    total = (valor1 + valor2) - desconto
else:
    total = valor1 + valor2
#SAIDA
print("Valor a pagar: R$%.2f" %total)