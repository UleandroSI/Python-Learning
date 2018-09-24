# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

# Entrada
menor = 0
produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

# Execução
if produto1 < produto2 and produto1 < produto3:
    menor = produto1
elif produto2 < produto1 and produto2< produto3:
    menor = produto2
else:
    menor = produto3

print("Comprar produto de valor: %.2f" %menor)