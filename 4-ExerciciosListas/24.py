# Faça um programa que simule um lançamento de dados.  
# Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros 
# aleatórios, simulando os lançamentos dos dados.

# VARIAVEIS
import random
from collections import Counter
dado = [1,2,3,4,5,6]
vetor = []

def sorteio(dado):
    global vetor
    for x in range(0,100):
        n = random.choice(dado)
        print("Lançamento %d: %d" %((x+1),n))
        vetor.append(n)

# PROCESSAMENTO
print("Sorteio de 100 numeros:")
sorteio(dado)

#SAIDA
contador = Counter(vetor)
print("------------------")
print(contador)