# Faça um programa que peça um numero inteiro positivo e em seguida mostre 
#este numero invertido.

# Variaveis
numero = int(input("Digite um numero: "))

#PROCESSAMENTO
numeroInvertido = int(str(numero)[::-1])

#SAIDA
print("Numero Invertido: ",numeroInvertido)