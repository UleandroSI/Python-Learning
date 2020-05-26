# As Organizações Tabajara resolveram dar um aumento de salário aos seus 
#colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

#Faça um programa que recebe o salário de um colaborador e o reajuste 
#segundo o seguinte critério, baseado no salário atual:

#  * salários até R$ 280,00 (incluindo)		: aumento de 20%
#  * salários entre R$ 280,00 e R$ 700,00	: aumento de 15%
#  * salários entre R$ 700,00 e R$ 1500,00	: aumento de 10%
#  * salários de R$ 1500,00 em diante 		: aumento de 5%

#  Após o aumento ser realizado, informe na tela:

#  a. o salário antes do reajuste;
#  b. o percentual de aumento aplicado;
#  c. o valor do aumento;
#  d. o novo salário, após o aumento.

#Variaveis
salario = float(input("Digite o salario: "))
total = b = 0

# Processamento
if salario <= 280:
    total = salario * 1.2
    b = '20%'
elif salario <= 700:
    total = salario * 1.15
    b = '15%'
elif salario <= 1500:
    total = salario * 1.1
    b = '10%'
else:
    total = salario * 1.05
    b = '5%'
print('')

#SAIDA
print("Salario atual: R$%.2f" %salario)
print("Percentual de aumento:",b)
print("Valor do aumento: R$%.2f"%(total - salario))
print("Novo salario: R$%.2f"%total)