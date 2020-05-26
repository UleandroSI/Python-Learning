# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

#VARIAVEIS
vetor = []
numero = 0
#PROCESSAMENTO
for x in range(0,10):
    numero = float(input("Digite o %d numero: " %(x+1)))
    vetor.append(numero)
invertido = vetor[::-1]
#SAIDA
print()
print(invertido)