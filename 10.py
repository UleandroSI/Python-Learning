# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# C = (5 * (F-32) / 9).
# Entrada
celsius = float(input("Digite a temperatura em Celsius: "))

# Calculo
farenheit = ((celsius / 5) *9) + 32

# Saida
print ("Temperatura em Farenheit é: %.fº" %farenheit)