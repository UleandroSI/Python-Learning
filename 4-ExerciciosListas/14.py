# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#	a. Telefonou para a vitima?
#	b. Esteve no local do crime?
#	c. Mora perto da vítima?
#	d. Devia para a vítima?
#	e. Ja trabalhou com a vítima? o programa deve no final emitir uma classificação sobre a participação da 
#		pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
#		"Suspeita", entre 3 e 4 como "Cumplice" e 5 como "Assassino".
#		Como contrario, ele será classificado como "Inocente".

vetor = []
entrada = ''
resp = 0

while True:
	entrada = input("Telefonou para a vítima?")
	if entrada not in "sim, não":
		print("Responda apenas sim ou não.")
		pass
	else:
		vetor.append(entrada)
		vetor.append(input("Esteve no local do crime?"))
		vetor.append(input("Mora perto da vítima?"))
		vetor.append(input("Devia para a vítima?"))
		vetor.append(input("Ja trabalhou com a vítima?"))
		break

for x in range(0,5):
	if vetor[x] == 'sim':
		resp += 1

if resp == 0:
	print("Inocente.")
elif resp <=2:
	print("Classificada como Suspeita.")
elif resp <= 4:
	print("Classificada como Cumplice.")
elif resp == 5:
	print("Classificada como Assassino.")