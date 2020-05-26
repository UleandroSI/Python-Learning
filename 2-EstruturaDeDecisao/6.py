#Faça um Programa que leia três números e mostre o maior deles.

# Variaveis
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
# Processamento
if n1 > n2 and n1 > n3:
    print("Maior e o primeiro")
elif n2 > n3:
    print("Maior e o segundo")
else:
    print("Maior e o terceiro")