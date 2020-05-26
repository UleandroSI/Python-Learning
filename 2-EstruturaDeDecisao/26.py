# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  - Álcool: 
#  a. até 20 litros, desconto de 3% por litro 
#  b. acima de 20 litros, desconto de 5% por litro
#  - Gasolina: 
#  a. até 20 litros, desconto de 4% por litro
#  b. acima de 20 litros, desconto de 6% por litro
#  Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço 
# do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

#VARIAVEIS
desconto = total = 0
litros = int(input("Digite a quantidade de litros vendidos: "))
combustivel = input("A-álcool, G-gasolina: ")

#PROCESSAMENTO
combustivel = combustivel.lower()
if combustivel == 'a':
    if litros <= 20:
        desconto = ((litros * 0.03)* 1.9)
        total = (litros * 1.9) - desconto
    else:
         desconto = ((litros * 0.05)* 1.9)
         total = (litros * 1.9) - desconto
elif combustivel == 'g':
    if litros <= 20:
        desconto = ((litros * 0.04)* 2.5)
        total = (litros * 2.5) - desconto
    else:
         desconto = ((litros * 0.06)* 2.5)
         total = (litros * 2.5) - desconto
#SAIDA
print("Total a pagar R$%.2f" %total)