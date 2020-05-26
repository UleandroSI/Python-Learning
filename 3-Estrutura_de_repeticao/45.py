# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve 
#perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular 
#o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve 
#ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido 
#informar:
#		a. Maior e Menor Acerto;
#		b. Total de alunos que utilizaram o sistema;
#		c. A média das notas da turma.
# Apos concluir isto voce poderia incrementar o programa permitindo que o professor digite o gabarito da 
#prova antes dos alunos usarem o programa.

# Variaveis
lista = []
nota = alunos = []
melhor = ' '
pior = ' '
notas = ['A','B','C','D','E', 0]
cont = i = certas = erradas = x = 0

for y in range(0,11):
    gabarito = input("Digite a resposta %d" %(y+1))
    lista.append(gabarito)

# Execução
while True:
	cont += 1
	
	while i != 10:
		n = input("Digite a resposta da pergunta %d: " %(i+1))
		if n not in notas:
			print("Resposta incorreta. Escolha entre A ao E, ou 0 para em branco.")
		else:
			nota.append(n)
			i += 1
	print(nota)
	i -= 1

	while i >= 0:
		if nota[i] == lista[i]:
			certas += 1
			i -= 1
		else:
			erradas += 1
			i -= 1


# Saida
	if certas >= 9:
		print("Resultado nota: A")
		#alunos.append('A')
	elif certas >= 7:
		print("Resultado nota: B")
		#alunos.append('B')
	elif certas >= 5:
		print("Resultado nota: C")
		#alunos.append('C')
	elif certas >= 3:
		print("Resultado nota: D")
		#alunos.append('D')
	else:
		print("Resultado nota: E")
		#alunos.append('E')
	print("Acertos: %d" %certas)

	print(" ")
	x = int(input(" Para sair digite 0(Zero) ou qualquer tecla para continuar.: "))
	if x == 0:
		break
	
if 'A' in alunos:
	melhor = 'A'
elif 'B' in alunos:
	melhor = 'B'
elif 'C' in alunos:
	melhor = 'C'
elif 'D' in alunos:
	melhor = 'D'
else:
	melhor = 'E'

if 'E' in alunos:
	pior = 'E'
elif 'D' in alunos:
	pior = 'D'
elif 'C' in alunos:
	pior = 'C'
elif 'B' in alunos:
	pior = 'B'
else:
	pior = 'A'

print(" ")
print("a. Melhor Nota: %s. Pior Nota: %s" %(melhor, pior))
print("b. Total de alunos: %d" %cont)