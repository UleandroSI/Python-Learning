# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# Entrada
litros = float(input("Digite o numero de litros: "))

while True:
    tipo = input("Combustivel A -alcool, G -gasolina.")
    tipo = tipo.lower()

    if tipo == "a":
        if litros <= 20.0:
            valor = litros * 1.90
            valor = valor - (valor * 0.03)
            break
        else:
            valor = litros * 1.90
            valor = valor - (valor * 0.05)
            break
    elif tipo == "g":
        if litros <= 20.0:
            valor = litros * 2.50
            valor = valor - (valor * 0.04)
            break
        else:
            valor = litros * 2.50
            valor = valor - (valor * 0.06)
            break
    else:
        print("Escolha apenas A ou G.")

print("Valor a pagar: R$ %.2f" %valor)