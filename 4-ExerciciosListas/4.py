# Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

#VARIAVEIS
consoantes = 0
vetor = []
#PROCESSAMENTO
for x in range(0,10):
    letras = input("Digite a %s letra: " %(x+1))
    if letras not in 'aeiou':
        vetor.append(letras)
        consoantes += 1
#SAIDA
print("Quantidade de consoantes: ", consoantes)
print(vetor)