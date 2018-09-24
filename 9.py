# Faça um programa que leia 3 numeros e mostre na ordem decrescente.

# Entrada
numero = 0
vetor = []
decres = []
y = 2

# Execuçao
for x in range(0,3):
    numero = int(input("Digite o %dº numero: " %(x+1)))
    vetor.append(numero)
vetor.sort()
while y >= 0:
    decres.append(vetor[y])
    y -= 1

# Saida
print(decres)