# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

#VARIAVEIS
vetor = []

#PROCESSAMENTO
for x in range(0,5):
    numero = int(input("Digite o %d numero: " %(x+1)))
    vetor.append(numero)

#SAIDA
print(vetor)