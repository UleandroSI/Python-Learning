# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
#jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
#telefonistas, para a computação dos votos. Suas equipe foi contratada para desenvolver este programa, utilizando
#a linguagem de programação Python. Para computar cada voto, a telefonista digitará um numero, entre 1 e 23,
#correnpondente ao numero da camisa do jogador. Um numero de jogador igual zero, indica que a votação foi 
#encerrada. Se um numero invalido for digitado, o programa deve ignora-lo, mostrando uma breve mensagem de aviso,
#e voltando a pedir outro numero. Após o final da votação, o programa devera exibir:
#	a) O total de votos computados;
#	b) Os numeros e respectivos votos de todos os jogadores que receberam votos;
#	c) O percentual de votos de cada um destes jogadores;
#	d) O numero do jogador escolhido como o melhor jogador da partida, juntamente com o numero de votos e o
#		percentual de votos dados a ele.

#	Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece
#	ordenado pelo numero do jogador. O programa deve fazer uso de arrays. O programa devera executar o calculo
#	do percentual de cada jogador e o total de votos.A função calculará o percentual e retornará o valor
# 	calculado. Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais proxima possivel
#	ao exemplo. Os dados são ficticios e podem mudar a cada execução do programa. Ao final, o programa deve ainda
#	gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obdecendo a mesma disposição
#	apresentada na tela.

from collections import Counter
def percentual(cont,a):
    calc = (a / cont) * 100
    return calc
#VARIAVEIS    
lista = []
cont = x = melhor = num_melhor = per_melhor = 0
ent = ''

print("Enquete: Quem foi o melhor jogador? \n")
# Receber votos.
while True:
	ent = input("Numero do jogador (0 = fim): ")
	if ent not in '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23':
		print(" Informe um numero entre 1 e 23 ou 0 para sair!\n")
	elif ent == '0':
		break
	else:
		lista.append(int(ent)) # Armazena votos válidos
		cont += 1

print("\nForam computados: %d votos." %cont)
print("Jogador	  Votos		%")
# Saida da enquete.
saida = open ("arquivo.txt","w")
lista.sort()
c = Counter(lista)
for s in c:
    saida = open ("arquivo.txt","a")
    a = c[s]
    retorno_percentual = percentual(cont,a)
    if a > melhor:
        melhor = a #Numero de votos
        num_melhor = s # Numero Jogador
        per_melhor = retorno_percentual #Percentual do melhor
    print("%d           %d         %.1f%%" %(s, a, retorno_percentual))
    saida.writelines("%d           %d         %.1f%%" %(s, a, retorno_percentual))
    saida.write('\n')
saida.close()
print("O melhor jogador foi o número %d, com %d votos, correspondendo a %.2f%% do total de votos."%(num_melhor,melhor,per_melhor))