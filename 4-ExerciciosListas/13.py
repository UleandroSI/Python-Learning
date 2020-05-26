# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
#calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês
#elas ocorrem (mostrar o mês por extenso: 1-janeiro, 2-fevereiro)

#VARIAVEIS
janeiro = '1'
fevereiro = '2'
marco = '3'
abril = '4'
maio = '5'
junho = '6'
julho = '7'
agosto = '8'
setembro = '9'
outubro = '10'
novembro = '11'
dezembro = '12'
vetor = []
i = n = media = 0

#ENTRADA
for x in range(0,12):
	vetor.append(float(input("Digite a temperatura do mês de %d: "%(x+1))))

while i <= 11:
	media += vetor[i]
	i += 1
media = media / 12

while n <= 11:
	if vetor[n] >= media:
		print("Média de %.2f no mês de %s"%(vetor[n],(n+1)))
	n += 1	

#SAIDA
