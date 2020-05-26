# Os numeros primos possuem varias aplicaçoes dentro da computaçao, por exemplo
# a criptografia. Um numero primo é aquele divisivel apenas por 1 ou ele mesmo.
# Faça um programa que peça um numero inteiro e determine se ele é ou não
# um numero primo.

numero = int(input('Digite um número inteiro: '))

if numero == 2:
	print('Número primo.')

elif (numero % 2) == 0:
	print('Não é numero primo.')
elif (numero % 3) == 0:
	print('Não é numero primo.')
else:
	print('Número primo.')    