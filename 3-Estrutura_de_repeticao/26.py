# Numa eleição existe 3 candidatos. Faça um programa que peça o 
# numero total de eleitores. Peça para cada eleitor votar,
# e ao final mostrar o numero total de votos.

# VARIAVEIS
candidato1 = candidato2 = candidato3 = voto = i = 0
eleitores = int(input("Digite o numero de eleitores: "))

#EXECUÇAO
while i < eleitores:
    voto =  int(input("Escolha 1, 2, ou 3 para voto: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Voto invalido.")
        i -= 1
    i += 1
    
#SAIDA
print("Candidato 1: %i" %candidato1)
print("Candidato 2: %i" %candidato2)
print("Candidato 3: %i" %candidato3)
print("Total de votos: %i" %eleitores)