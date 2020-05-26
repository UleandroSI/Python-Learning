# Faça um programa que peça um número inteiro e determine se ele é ou não 
#um número primo. 
#Um numero primo é aquele que é divisivel somente por ele mesmo e por 1.


numero = int(input('Digite um número inteiro: '))

if numero == 2:
	print('Número primo.')
if numero == 3:
    print("Numero primo.")
elif (numero % 2) == 0:
	print('Não é numero primo.')
elif (numero % 3) == 0:
	print('Não é numero primo.')
else:
	print('Número primo.')