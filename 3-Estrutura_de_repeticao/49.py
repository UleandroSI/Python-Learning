# Faça um programa que mostre os n termos da Série a seguir:
#      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#    Imprima no final a soma da série.

#VARIAVEIS
soma = divisao = 0
y = 1
lista = []
n = int(input("Digite N: "))
#PROCESSAMENTO
for x in range(1,n+1):
    divisao = x / y
    lista.append((str(x) + '/' + str(y)))
    soma += divisao
    y += 2
#SAIDA
print(lista)
print("A soma é: %d" %soma)