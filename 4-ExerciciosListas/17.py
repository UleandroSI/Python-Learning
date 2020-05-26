# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
#determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
#distancias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta.
# 	Atleta: Nome

#	Primeiro Salto: 6.5 m
#	Segundo Salto: 6.5 m
#	Terceiro Salto: 6.5 m
#	Quarto Salto: 6.5 m
#	Quinto Salto: 6.5 m

# Resultado final:
# Atleta: Nome
# Saltos: 6.5 - 6.5 - 6.5 - 6.5 - 6.5
# Media dos Saltos: 6.5 m

#Variaveis
nome = []
notas =[]
resultado = []
op = ''
atletas = nota = cont = y = 0
s = 4

while True:
	media = 0
	nome.append(input("Digite o nome completo do atleta: \n"))
	atletas += 1

	for x in range(0,5):
		nota = float(input("Digite o %dº salto: " %(x+1)))
		notas.append(nota)
		media = media + nota

	media = media / 5
	resultado.append(media)
	print(" Deseja digitar um novo atleta?")

	while True:
		op = input("Digite apenas 'sim' ou 'não': \n")
		if op not in "sim, não":
			print("Digite apenas 'sim' ou 'não'!!!")
		else:
			break

	if op == 'não':
		break
	else:
		pass

y = 0
print(" Resultado Final:\n")
while y < atletas:
	print("Atleta: %s" %nome[y])
	
	while cont <= s:
		print("Salto %d: %.2f" %((cont+1),notas[cont]))
		cont += 1
	s += 5
	
	print("Media dos saltos: %.2f" %resultado[y] \n)
	y += 1