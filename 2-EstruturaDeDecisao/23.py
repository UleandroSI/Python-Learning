# Faça um Programa que peça um número e informe se o número é inteiro 
# ou decimal. Dica: utilize uma função de arredondamento.

#VARIAVEIS
numero = float(input("Digite um numero: "))

#PROCESSAMENTO
if numero == round(numero):
    print("Numero inteiro.")
else:
    print("Numero decimal")