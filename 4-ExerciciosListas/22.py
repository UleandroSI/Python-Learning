# Sua empresa acaba de contratar um estagiario para trabalhar no suporte de informatica, com a intenção de 
# fazer um levantamento nas sucatas encontradas nesta área. A tarefa dele é testar todos os cerca de 200
# mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
# verificar o que se pode aproveitar deles.
#	Fazer um programa para registrar esse levantamento. O programa devera receber um numero indeterminado de entradas
#	 cada uma contendo: um numero de identificação do mouse e o tipo de defeito:
#	 necessita da esfera;
#	 necessita de limpeza;
#	 necessita de troca do cabo ou conector;
# 	 quebrado ou inutilizado;
#	Uma entrada igual a zero encerra o sistema. Ao final deve emitir relatorio.

# VARIAVEIS
defeitos = {}
defeitos[1] = 'Necessita esfera'
defeitos[2] = 'Necessita limpeza'
defeitos[3] = 'Necessita troca de cabo ou conector'
defeitos[4] = 'Quebrado ou inutilizado'
numMouse = []
entrada = x = defeito1 = defeito2 = defeito3 = defeito4 = 0

# ENTRADAS
print("Escolha de 1 a 4 - Ou 0 para sair")
print("1 - Necessita esfera.")
print("2 - Necessita limpeza.")
print("3 - Necessita troca de cabo ou conector.")
print("4 - Quebrado ou inutilizado.")

while True:
	entrada = int(input("Tipo de defeito: "))
	if entrada not in defeitos:
		print("Escolha de 1 a 4 - Ou 0 para sair")
	if entrada == 0:
		print("\n")
		break
	else:
		x += 1
		if entrada == 1:
			defeito1 += 1
		elif entrada == 2:
			defeito2 += 1
		elif entrada == 3:
			defeito3 += 1
		else:
			defeito4 += 1
	numMouse.append(int(input("Digite o número de identificação: ")))
	print("\n")

# SAIDAS
print("Quantidade de mouses: %d" %x)
print("\n")
print("Situação							Quantidade			Percentual")
print("1 - Necessita esfera			%10d			%10d" %(defeito1,(defeito1/x)*100))
print("2 - Necessita limpeza 		%10d			%10d" %(defeito2,(defeito2/x)*100))
print("3 - Necessita troca de cabo ou conector %10d			%10d" %(defeito3,(defeito3/x)*100))
print("4 - Quebrado ou inutilizado			%10d			%10d" %(defeito4,(defeito4/x)*100))