# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
#   para um '''n''' informado pelo usuário. Use uma função que receba um valor '''n''' inteiro e imprima até a n-ésima linha.

def imprimir(n):
    for i in range(1, n+1):
        print((str(i)+" ")*i)

#VARIAVEIS
n = int(input("Digite um numero: "))
#PROCESSAMENTO
imprimir(n)