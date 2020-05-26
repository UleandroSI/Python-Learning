# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  a. Para homens: (72.7*h) - 58
#  b. Para mulheres: (62.1*h) - 44.7

# Variaveis
altura = float(input("Digite a altura: "))
# Processamento
pesoh = (72.7*altura) - 58
pesom = (62.1*altura) - 44.7
# Saida
print("a). Para homens: %.1f kg" %pesoh)
print("b). Para mulheres: %.1f kg" %pesom)