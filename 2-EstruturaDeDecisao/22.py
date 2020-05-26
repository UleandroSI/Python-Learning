# Faça um Programa que peça um número inteiro e determine se 
# ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

#VARIAVEIS
numero = int(input("Digite um numero: "))

#PROCESSAMENTO
if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")