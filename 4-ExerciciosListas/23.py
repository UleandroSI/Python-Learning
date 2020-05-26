# A ACME, uma empresa de 500 funcionarios, esta tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver seu problema, o administrador de rede precisa saber qual o espaço ocupado pelos usuarios,
#e identificar os usuarios com maior espaço ocupado. Atraves de um programa, baixado da internet, ele conseguiu gerar,
#o seguinte arquivo, chamado usuario.txt

# Variáveis
nome = ''
relat = ''
numero = cont1 = mega = total = media = 0
tempN =()

# Funçoes
def converter(numero):
	convertido = numero / 1048576
	#print("%.2f" %convertido)
	return convertido

def percentual(total,mega):
	porc = ((mega/total)*100)
	return porc

#------------------------------------------Separação----------------------------------------------------------

relat = open("relatorio.txt","w")
relat.write("Nr.		Usuário			 Espaço Utilizado		  % de uso\n")
print("ACME INC.				Uso do espaço em disco pelos usuarios \n ---------------------------------------------------------------------------------------- \nNr.		Usuário			Espaço Utilizado		% de uso")
#------------------------------------------Separação----------------------------------------------------------
with open("usuarios.txt","r") as arquivo:
	for linha in arquivo.readlines():
		#Imprimir conteúdo de cada linha do arquivo - print(linha)
		cont1 += 1
		listaNome = []
		for x in range(0,14):
			listaNome.append(linha[x])
			nome = ''.join(listaNome)
		
		#------------------------------------------Separação----------------------------------------------------------
		listaNum = []
		y = 15
		while y < len(linha):
			listaNum.append(linha[y])
			tempN = ''.join(listaNum)
			y += 1
		numero = float(tempN)
		#converter(numero)
		mega = converter(numero)
		total += mega
		#------------------------------------------Separação----------------------------------------------------------
		porcentagem = percentual(total,mega)
		relat = open('relatorio.txt', 'a')
		relat.write("%d		%10s		%10.2f MB		%10.2f"%(cont1, nome, mega, porcentagem))
		relat.write("\n")
		print("%d		%10s		%10.2f MB		%10.2f"%(cont1, nome, mega, porcentagem))
		#------------------------------------------Separação----------------------------------------------------------

# Saída
relat.write("Espaço total ocupado: %.2f" %total)
relat.write("Espaço médio ocupado: %.2f" %(total/cont1))
print("Espaço total ocupado: %.2f" %total)
print("Espaço médio ocupado: %.2f" %(total/cont1))
arquivo.close()
relat.close()