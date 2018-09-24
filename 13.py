# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

# Entrada
altura = float(input("Digite a altura: "))

# Execuçao
homem = (72.7* altura) - 58
mulher = (62.1* altura) - 44.7

# Saida
print("Peso ideal para Homem: %.2f" %homem)
print("Peso ideal para Mulher: %.2f" %mulher)