''' nome ='Paulo'
profissao = 'estudante'
escola = 'estadual dourado'
idade = 18
print ('Nome: {}\nTrabalho: {}\nEscola: {}\nIdade: {} anos'.format(nome, profissao, escola, idade)) '''

# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000
#ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos 
#vendedores receberam salários nos seguintes intervalos de valores:

# a)$200 - $299
# b)$300 - $399
# c)$400 - $499
# d)$500 - $599
# e)$600 - $699
# f)$700 - $799
# g)$800 - $899
# h)$900 - $999
# i)$1000 em diante

# Desafio crie uma formula para chegar na posição da lista a partir do salario, sem fazer varios IFs aninhados

y = a = b = c = d = e = f = g = h = i = j = valor = salario = 0
x = 1
vetor = []
op = ''

while True:
	print("\n   Vendedor %d" %x)
	x += 1
	comissao = float(input("Digite o valor bruto de vendas: "))
	valor = comissao * 0.09
	salario = valor + 200.00
	vetor.append(salario)
	print(" Deseja digitar um novo vendedor?\n")
	op = input("  Para parar digite SAIR: ")
	if op == 'sair':
		break

j = len(vetor) -1
while y <= j:
	if vetor[y] <= 299:
		a += 1
	elif vetor[y] <= 399:
		b += 1
	elif vetor[y] <= 499:
		c += 1
	elif vetor[y] <= 599:
		d += 1
	elif vetor[y] <= 699:
		e += 1
	elif vetor[y] <= 799:
		f += 1
	elif vetor[y] <= 899:
		g += 1
	elif vetor[y] <= 999:
		h += 1
	else:
		i += 1
	y += 1

print("Salarios entre $200 - $299: %10d"%a)
print("Salarios entre $300 - $399: %10d"%b)
print("Salarios entre $400 - $499: %10d"%c)
print("Salarios entre $500 - $599: %10d"%d)
print("Salarios entre $600 - $699: %10d"%e)
print("Salarios entre $700 - $799: %10d"%f)
print("Salarios entre $800 - $899: %10d"%g)
print("Salarios entre $900 - $999: %10d"%h)
print("Salarios entre $1000 em diante: %10d"%i)