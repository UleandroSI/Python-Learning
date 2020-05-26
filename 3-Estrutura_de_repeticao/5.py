# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
#iniciais. Valide a entrada e permita repetir a operação.

opec = 's' 
while opec == 's':
	while True:
		paisA = int(input('Digite a população do país A: '))
		if paisA <= 0:
			print('Digite a população maior que 0 (zero)!')
		else:
			break
	while True:
		paisB = int(input('Digite a população do país B: '))
		if paisB <= 0:
			print('Digite a população maior que 0 (zero)!')
		else:
			break

	while True:
		taxaA = float(input('Digite a taxa de crescimento do país A: '))
		if taxaA > 0:
			break
		else:
			print('Digite a taxa maior que 0 (zero)!')
	while True:
		taxaB = float(input('Digite a taxa de crescimento do país B: '))
		if taxaB > 0:
			break
		else:
			print('Digite a taxa maior que 0 (zero)!')

	cont = 0
	while paisA < paisB:
		paisA = paisA * (1 + taxaA)
		paisB = paisB * (1 + taxaB)
		cont += 1
	print('Quantidade de anos para A ultrapassar B é: %d' %cont)

	print('')
	print('Deseja fazer a operação novamente?')

	y = ['s', 'n']
	while True:
		opec = input("Digite 's' SIM, ou 'n' NÃO: ")
		if opec not in y:
			print('Escolha somente s ou n!')
		else:
			break