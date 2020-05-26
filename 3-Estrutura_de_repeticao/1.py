# Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até
#que o usuário informe um valor válido.

nota = 11

while nota not in range(0,11):
	if nota not in range(0,11):
		nota = int(input('Digite uma nota de 0 a 10: '))

print('Nota digitada: %d' %nota)