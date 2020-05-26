# As organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
#alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como
#uma projeção de quanto será gasto com o pagamento deste abono.
#	Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
#laboral, chegou-se a seguinte forma de cálculo:
#		a)Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
#		b)O piso do abono será de 100 reais, isto é, valor mínimo.
#		c)Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa,
#		  descontos, impostos ou outras particularidades.
#	Seu sistema deverá permitir a digitação do salário de um número indefinido de salários. 
#	Um valor de salário igual a 0 encerra a digitação. Após a entrada de todos os dados o programa deverá 
#	calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final o
#	programa deverá apresentar:
#		- O salário de cada funcionário, juntamente com o valor do abono;
#		- O número total de funcionário processados;
#		- O valor total de funcionário,juntamente com o valor do abono;
#		- O valor total a ser gasto com o pagamento do abono;
#		- O número de funcionário que receberá o valor mínimo de 100 reais;
#		- O maior valor pago como abono;

lista = []
salarios = []
cont= totalsalarios= totalabono= x= minAbono= maxAbono= 0

print("---Organizaçoes Tabajara---")
print("Calculo de abono:")

#Receber salários
while True:
    salarioDez = float(input("Digite o salário do funcionário(ou 0 para sair): "))
    if salarioDez == 0:
        break
    else:
        cont += 1
        totalsalarios = totalsalarios + salarioDez
        lista.append(salarioDez)

#Calcular salário + abono
print("\nSalário		- Abono")
while x < cont:
	abono = 0
    if lista[x] <= 500:
    	abono = 100
    	print("%.2f		= %.2f" %(lista[x],abono))
    	minAbono += 1
    else:
        abono = lista[x] * 0.20
        print("%.2f		= %.2f"%(lista[x],abono))
        if abono > maxAbono:
        	maxAbono = abono
    x += 1
    totalabono = totalabono + abono

#Relatório de Saída
print("\n")
print("Foram processados %d colaboradores." %cont)
print("Total gasto com Abonos: R$ %.2f" %totalabono)
print("Total gasto com Salários: R$ %.2f" %totalsalarios)
print("Valor minimo pago a %d colaboradores" %minAbono)
print("Maior valor de abono pago: R$ %.2f " %maxAbono)