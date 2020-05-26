# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
#que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# Variaveis
altura = float(input("Digite a altura: "))
# Processamento
peso = (72.7*altura) - 58
# Saida
print("Peso ideal: %.1fkg" %peso)