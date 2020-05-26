#Faça um programa que pergunte o preço de três  produtos e informe qual 
#produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# Variaveis
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

#Processamento
if produto1 < produto2:
    if produto1 < produto3:
        print("Comprar primeiro produto.")
    else:
        if produto3 < produto2:
            print("Comprar terceiro produto.")
else:
    if produto2 < produto3:
        print("Comprar segundo produto.")
    else:
        print("Comprar terceiro produto.")