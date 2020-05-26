# Faça um programa que carregue uma lista com os modelos de cinco carros(FUSCA, GOL, VECTRA, ETC...). 
#Carregue outra lista com o consumo desses carros, calcule e mostre:
#	a) Modelo do carro mais economico;
#	b) Quanto litros de combustivel cada um dos carros cadastrados consome para percorrer uma distancia
#		de 1000 quilometros e quanto isto custará, considerando que a gosolina custe R$2,25 o litro.

# Variaveis
carros = []
consumo = []
menorKm = 0
menorconsumo = ''

print("Comparativo de consumo de veiculos\n")

for x in range(0,5):
	carros.append(input("Veiculo %d \nNome: " %x+1))
	consumo.append(float(input("KM por litro: ")))
	if consumo[x] >= menorKm:
		menorKm = consumo[x]
		menorconsumo = carros[x]

#Saida
print("\nRelatório Final")
for y in range(0,5):
	print("%d - %s 	- %.1f	- %.1f	- R$%.2f" %(y+1, carros[y],consumo[y],(1000/consumo[y]),((1000/consumo[y])*2.25)))

print("O menor consumo é do %s."%menorconsumo)