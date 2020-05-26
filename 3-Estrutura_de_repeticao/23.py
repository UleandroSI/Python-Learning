# Faça um programa que mostre todos os primos entre 1 e N sendo N um 
# número inteiro fornecido pelo usuário. 
#O programa devera mostrar também o numero de divisões que ele executou 
# para encontrar os números primos. 
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# VARIÁVEIS
i= 1
n = []
numero = int(input('Digite o número: '))

# EXECUÇÃO
if numero == 2:
	print('Número primo é 2.')
elif (numero % 2) == 0:
	print('Não é numero primo.')
	while i <= numero:
		if (numero % i) == 0:
			n.append(i)
		i += 1
			
        
elif (numero % 3) == 0:
	print('Não é numero primo.')
	while i <= numero:
		if (numero % i) == 0:
			n.append(i)
		i += 1

else:
	print('Número primo.')

# SAÍDA
print('Divisores: %s' %n)
print("Divisoes executadas: %i" %i)