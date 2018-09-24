# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Entrada
valorhora = float(input("Digite o valor hora: "))
horas = float(input("Digite o numero de horas trabalhadas: "))

# Execuçao
salariobruto = valorhora * horas
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
imposto = salariobruto * 0.11
salarioliquido = ((salariobruto - inss) - sindicato) - imposto

# Saida
print("+ Salario Bruto: R$%.2f" %salariobruto)
print("- INSS R$%.2f" %inss)
print("- Sindicato: R$%.2f" %sindicato)
print("= Salário Liquido: R$%.2f" %salarioliquido)