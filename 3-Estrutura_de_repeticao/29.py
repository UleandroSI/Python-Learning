# O sr. Manoel Joaquim possui uma grande loja de artigos de R$1,99, 
#com cerca de 10 caixas. Para agilizar o calculo de quanto cada cliente 
#deve pagar ele desenvolveu uma tabela que contém o número de itens que o 
#cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa 
#precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
#Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
#que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

# VARIAVEIS
i = 1.99

# EXECUÇÃO
print("Loja quase dois - Tabela de Preços")
print('')

for x in range(1,51):
	print("%d - R$ %.2f" %(x, i*x))