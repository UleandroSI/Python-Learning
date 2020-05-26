# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos 
# votos restantes. Você deve fazer um programa que receba o nome do ginasta 
# e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e 
# depois informe a sua média, conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média com as notas 
# restantes). As notas não são informados ordenadas. Um exemplo de saída do 
# programa deve ser conforme o exemplo abaixo:

#Atleta: Aparecido Parente
#Nota: 9.9
#Nota: 7.5
#Nota: 9.5
#Nota: 8.5
#Nota: 9.0
#Nota: 8.5
#Nota: 9.7

#Resultado final:
#Atleta: Aparecido Parente
#Melhor nota: 9.9
#Pior nota: 7.5
#Média: 9,04

#VARIAVEIS
y = 1
media = 0
nome = input("Digite o nome do Atleta: ")
notas = []
validos = []
#PROCESSAMENTO
for x in range(0, 7):
    nota = float(input("Nota: "))
    notas.append(nota)
notas.sort()
while y <6:
    v = notas[y]
    validos.append(v)
    y += 1
soma = sum(validos)
media = soma / 5
#SAIDA
print("Resultado final: ")
print("Atleta: %s" %nome)
print("Melhor nota: ",notas[6])
print("Pior nota: ",notas[0])
print("Media: ",media)