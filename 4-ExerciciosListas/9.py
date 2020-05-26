# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

#VARIAVEIS
vetor = []
quadrado = []
soma = 0
#PROCESSAMENTO
for x in range(0,10):
    numero = int(input("Digite o %d numero: " %(x+1)))
    vetor.append(numero)
for y in range(0,10,2):
    q = vetor[y] * vetor[y+1]
    quadrado.append(q)
#SAIDA
print("Soma: ", sum(quadrado))