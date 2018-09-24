# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Entrada
menor = maior = 0
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

# Execução
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1

# Saida
print("O menor numero é: %.2f" %menor)
print("O maior numero é: %.2f" %maior)