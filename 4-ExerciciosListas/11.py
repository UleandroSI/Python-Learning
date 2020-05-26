# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

#VARIAVEIS
pri_vetor = []
seg_vetor = []
ter_vetor = []
tot_vetor = []

#PROCESSAMENTO
for x in range(0,10):
    p = input("Digite o %d elemento do primeiro vetor: " %(x+1))
    pri_vetor.append(p)
for y in range(0,10):
    s = input("Digite o %d elemento do segundo vetor: " %(y+1))
    seg_vetor.append(s)
for w in range(0,10):
    t = input("Digite o %d elemento do terceiro vetor: " %(w+1))
    ter_vetor.append(t)
for z in range(0,10):
    tot_vetor.append(pri_vetor[z])
    tot_vetor.append(seg_vetor[z])
    tot_vetor.append(ter_vetor[z])

#SAIDA
print(tot_vetor)