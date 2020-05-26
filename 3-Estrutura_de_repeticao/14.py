# Faça um programa que peça 10 numeros inteiros, calcule e mostre a quantidade 
#de numeros pares e a quantidade de numeros impares.

par = []
a = 0
impar = []
b = 0

for x in range(1,11):
	n = int(input('Digite o %d° número inteiro: ' %x))
	if n %2 == 0:
		par.append(n)
		a += 1
	else:
		impar.append(n)
		b += 1
print('Entre os 10 números digitados %s são pares %s, e %s são impares %s'%(a,par,b,impar))