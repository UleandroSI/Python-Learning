# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

#VARIAVEIS
notas = media = 0
vetor = []
#PROCESSAMENTO
for x in range(0, 4):
    notas = float(input("Digite a %d nota: " %(x+1)))
    vetor.append(notas)
    media += notas
#SAIDA
print("Notas: ", vetor)
print("Media: ", media/4)