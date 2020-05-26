#Faça um programa para o cálculo de uma folha de pagamento, sabendo que 
#os descontos são do Imposto de Renda, que depende do salário bruto 
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% 
#do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade 
#de horas trabalhadas no mês. 
#  Desconto do IR:
#  * Salário Bruto até 900  (inclusive)   - isento    
#  * Salário Bruto até 1500 (inclusive)	- desconto de 5%
#  * Salário Bruto até 2500 (inclusive)	- desconto de 10%
#  * Salário Bruto acima de 2500     	- desconto de 20% 
#  Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#  No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#	Salário Bruto: (5 * 220) 	: R$ 1100,00
#     	(-) IR (5%)			: R$   55,00  
#	(-) INSS ( 10%)		        : R$  110,00
#	FGTS (11%)			: R$  121,00
#	Total de descontos		: R$  165,00
#	Salário Liquido	                : R$  935,00

# Variaveis
valor_hora = float(input("Digite o valor da hora: R$"))
horas = int(input("Digite a quantidade de horas: "))
sal_bruto = salario = sindicato = fgts = ir = descontos = 0
# Processamento
sal_bruto = valor_hora * horas
sindicato = sal_bruto * 0.03
fgts = sal_bruto * 0.11
if sal_bruto <= 900:
    ir = 0
elif sal_bruto <= 1500:
    ir = sal_bruto * 0.05
elif sal_bruto <= 2500:
    ir = sal_bruto * 0.1
else:
    ir = sal_bruto * 0.2
descontos = sindicato + ir
salario = sal_bruto - descontos
# Saida
print("")
print("Salario Bruto: R$%.2f" %sal_bruto)
print("         (-) IR: R$%.2f" %ir)
print("         (-) Sindicato: R$%.2f" %sindicato)
print("         (-) FGTS: R$%.2f" %fgts)
print("Total de descontos: R$%.2f" %descontos)
print("Salario Liquido: R$%.2f" %salario)