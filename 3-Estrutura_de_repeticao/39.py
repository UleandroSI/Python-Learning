# Faça um programa que leia dez conjuntos de dois valores, o primeiro 
#representando o numero do aluno e o segundo representando a sua altura 
#em centimetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
#numero do aluno mais alto e o numero do aluno mais baixo, junto com suas alturas.

# Variaveis
maisalto = 0
maisbaixo = 999999
codalto = 0
codbaixo = 0

# Execução
numero = int(input("Digite o numero do aluno 1: "))
altura = float(input("Digite a altura: "))
print("")

for x in range(2,11):
	if altura >= maisalto:
		maisalto = altura
		codalto = numero

	if altura <= maisbaixo:
		maisbaixo = altura
		codbaixo = numero

	numero = int(input("Digite o numero do aluno %d: " %x))
	altura = float(input("Digite a altura: "))


# Saida
print("O aluno mais baixo é: %d com %.2f cm" %(codbaixo, maisbaixo))
print("O aluno mais alto é: %d com %.2f cm" %(codalto, maisalto))