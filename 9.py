# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

# Entrada
farenheit = float(input("Digite a temperatura em Farenheit: "))
# Calculo
celsius = ((farenheit - 32)/ 1.8000)
# Saida
print("A temperatura em Celsius é: %.2f" %celsius)