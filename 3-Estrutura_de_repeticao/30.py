# O sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da 
#tabelinha, que já é um sucesso na sua loja de 1,99. 
#Você foi contratado para desenvolver o programa que monta a tabela de 
#preços de pães, de 1 até 50, a partir do pão informado pelo usuário, 
#conforme o exemplo abaixo:

# Variaveis
c = float(input("Digite o preço do pão: R$ "))

# Execução
print("Preço do Pão: R$ %.2f" %c)
print("Panificadora Pão de Ontem - Tabela de Preço")
print("")

# Saida
for x in range(1,51):
	print("%i - R$ %.2f" %(x, (x*c)))