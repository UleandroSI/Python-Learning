# Uma empresa de pesquisas precisa tabular os resultados da seguinte 
# enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#As possíveis respostas são:
#1- Windows Server
#2- Unix
#3- Linux
#4- Netware
#5- Mac OS
#6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da 
# enquete e informe ao final o resultado da mesma. O programa deverá ler os 
# valores até ser informado o valor 0, que encerra a entrada dos dados. 
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá 
# calcular a percentual de cada um dos concorrentes e informar o vencedor 
# da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional	Votos	%
#-------------------	-----	---
#Windows Server	 	 1500	17%
#Unix 		 	 3500	40%
#Linux 			 3000	34%
#Netware			  500	 5%
#Mac OS			  150	 2%
#Outro			  150	 2%
#-------------------	-----
#Total		 	 8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo 
# a 40% dos votos.

from collections import Counter
def percentual(cont,a):
    calc = (a / cont) * 100
    return calc
#VARIAVEIS    
lista = []
cont = x = melhor = per_melhor = 0
ent = ''
num_melhor = ''
sistema = {1:"Windows Server", 2:"Unix", 3:"Linux", 4:"Netware", 5:"Mac OS X", 6:"Outro"}

print("Qual o melhor Sistema Operacional para uso em servidores? \n")
print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS X\n6- Outro")
# Receber votos.
while True:
	ent = int(input("Digite o numero escolhido (0 = fim): "))
	if ent == 0:
		break
	elif ent not in (1,2,3,4,5,6):
		print(" Informe um numero entre 1 e 6 ou 0 para sair!\n")
	else:
		lista.append(ent) # Armazena votos válidos
		cont += 1
#SAIDA
print("\nSistema Operacional	  Votos	    %")
print("-------------------------------")
lista.sort()
c = Counter(lista) # Conta os votos iguais da array lista
for s in c:
    a = c[s] # recebe a key do contador
    retorno_percentual = percentual(cont,a) #Chama funcao para calculo da percentagem
    if a > melhor: # Achar o mais votado
        melhor = a #Numero de votos
        num_melhor = sistema[s] # Numero Jogador
        per_melhor = retorno_percentual #Percentual do melhor
    #print(sistema[s])
    print("%s           %10d         %.1f%%" %(sistema[s], a, retorno_percentual))
print("-------------------------------")
print("Total            %d" %cont)
print("O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f%% do total de votos."%(num_melhor,melhor,per_melhor))