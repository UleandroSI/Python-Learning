# O departamento estadual de meteorologia lhe contratou para desenvolver um programa que leia um conjunto
#inderterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a 
#media das temperaturas.

# Variaveis
menor = 99
maior = 0
temp = 0
media = 0
i = 0

# Execução
temp = int(input("Digite a temperatura: "))
while True:
	
	if temp <= menor:
		menor = temp
	if temp >= maior:
		maior = temp
	media = media + temp
	i += 1

	opc = input("Para sair digite s : ")
	if opc == 's':
		break
	temp = int(input("Digite a temperatura: "))

# Saida
print("Menor temperatura foi: %d" %menor)
print("Maior temperatura foi: %d" %maior)
print("Media das temperaturas foi: %d" %(media/i))