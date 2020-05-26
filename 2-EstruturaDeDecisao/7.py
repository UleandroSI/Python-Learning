#Faça um Programa que leia três números e mostre o maior e o menor deles.

# Variaveis
menor = maior = 0
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
# Processamento
if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 < n3:
            menor = n2
        else:
            menor = n3
    elif n3 > n2:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 < n3:
            menor = n1
        else:
            menor = n3
    else:
        maior = n3
        menor = n1

# Saida
print("Menor numero: ",menor)
print("Maior numero: ",maior)