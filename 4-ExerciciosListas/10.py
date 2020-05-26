# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
# compostos pelos elementos intercalados dos dois outros vetores.

#VARIAVEIS
pri_vetor = []
seg_vetor = []
tot_vetor = []

#PROCESSAMENTO
for x in range(0,10):
    p = input("Digite o %d elemento do primeiro vetor: " %(x+1))
    pri_vetor.append(p)
for y in range(0,10):
    s = input("Digite o %d elemento do segundo vetor: " %(y+1))
    seg_vetor.append(s)
for z in range(0,3):
    tot_vetor.append(pri_vetor[z])
    tot_vetor.append(seg_vetor[z])

#SAIDA
print(tot_vetor)