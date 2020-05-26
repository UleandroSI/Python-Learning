#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre 
# a temperatura em graus Celsius. C = (5 * (F-32) / 9).

# VAriaveis
faren = float(input("Digite a temperatura em Farenheit: "))
# Processamento
celci = (5 * (faren-32) / 9)
# SAida
print("Temperatura em Celsius: ", celci)