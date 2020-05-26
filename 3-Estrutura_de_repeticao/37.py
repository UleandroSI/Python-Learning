# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais 
#gordo e o mais magro, para isso você deve fazer um programa que pergunte a cada um dos clientes da 
#academia seu codigo, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
#digitar 0 no campo codigo. Ao encerrar o programa também deve ser informados os códigos e valores do 
#cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos 
#clientes.

# Variaveis
i = 0
altura = 0
peso = 0
codigo = 0
pesomais = 0
pesomenos = 999999
altomais = 0
altomenos = 999999
codalto = 0
codbaixo = 999999
codgordo = 0
codmagro = 999999
mediapeso = 0
mediaaltura = 0

# Execução
codigo = int(input("Digite seu codigo, ou 0 para sair: "))
while True:
	if codigo == 0:
		break
	altura = float(input("Digite sua altura: "))
	peso = float(input("Digite seu peso: "))
	
	mediaaltura = mediaaltura + altura
	mediapeso = mediapeso + peso

	if altura >= altomais:
		altomais = altura
		codalto = codigo
	if altura <= altomenos:
		altomenos = altura
		codbaixo = codigo
	if peso >= pesomais:
		pesomais = peso
		codgordo = codigo
	if peso <= pesomenos:
		pesomenos = peso
		codmagro = codigo
	
	i += 1
	print("")
	codigo = int(input("Digite novo codigo, ou 0 para sair: "))


# Saida
print("")
print("O cliente mais alto é: %d com %.2fm" %(codalto, altomais))
print("O cliente mais baixo é: %d com %.2fm" %(codbaixo, altomenos))
print("O cliente mais gordo é: %d com %.2fKg" %(codgordo, pesomais))
print("O cliente mais magro é: %d com %.2fKg" %(codmagro, pesomenos))
print("A media de altura dos clientes foi: %.2fm" %(mediaaltura / i))
print("A media de peso dos clientes foi: %.2fKg" %(mediapeso / i))