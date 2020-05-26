# Altere o programa de cálculo dos números primos, informando, 
# caso o numero não seja primo, por quais números ele é divisível.

# VARIÁVEIS
i= 1
n = []
numero = int(input('Digite o número: '))

# EXECUÇÃO
if numero == 2:
	print('Número primo.')
elif (numero % 2) == 0:
	print('Não é numero primo.')
	while i <= numero:
		if (numero % i) == 0:
			n.append(i)
			i += 1
		else:
			i += 1
elif (numero % 3) == 0:
	print('Não é numero primo.')
	while i <= numero:
		if (numero % i) == 0:
			n.append(i)
			i += 1
		else:
			i += 1
else:
	print('Número primo.')

# SAÍDA
print('Divisores: %s' %n)