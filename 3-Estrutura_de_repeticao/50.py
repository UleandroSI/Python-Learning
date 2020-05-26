# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
# Faça um programa que calcule o valor de H com N termos.

#VARIAVEIS
soma = divisao = 0
y = x = 1
lista = [1]
n = int(input("Digite o numero de termos: "))

#PROCESSAMENTO
for i in range(1,n+1):
    divisao = x / y
    lista.append((str(x) + '/' + str(y)))
    soma += divisao
    y += 1
#SAIDA
print(lista)
print("Valor de H= %d" %soma)